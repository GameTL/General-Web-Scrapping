""" 
Based on this https://towardsdatascience.com/e-mails-notification-bot-with-python-4efa227278fb

NOTE 1: for gmail account allow [Less secure app access] at https://myaccount.google.com/u/1/lesssecureapps?pli=1&rapt=AEjHL4PaTVQF1377FxI9z3Wczl97_20c1ZyMFb2uZClbiQnDFzKAfx39YJ-YQ68LjddzNx_-3um5Hv8CEkD-5MJ5vXTVVUCBSQ
gmail prevent smtp login as its less secure, therefore allow it manually
"""

#%%
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import path
from clearterminal import *
import requests
from bs4 import BeautifulSoup
from csv import writer
import pytz
import datetime
SiteList = []

class Site:
    def __init__(self, name, link, file_compare, parent_link):
        self.Name = name
        self.Scrape_Link = link
        self.File_Compare = file_compare
        self.Parent_Link = parent_link
ise = Site("Chula ISE", "http://www.ise.eng.chula.ac.th/news?gid=1-008-002-001&pn=1", "Chula_Recent_Compare.txt", "http://www.ise.eng.chula.ac.th/")
SiteList.append(ise)

for site in SiteList:
    print(site.Name)

###############################################################################################
###############################################################################################
# SETTINGS

RECEPIENTS = ["limsila.limsila@gmail.com"]

TIMEZONE = 'Asia/Bangkok'



###############################################################################################
###############################################################################################
# %%

def __init_account_from_file():
    global SENDER_EMAIL, SENDER_PASSWORD
    MODE = 'file_based'
    if MODE == "hard_code":
        SENDER_EMAIL = "" ### ENTER USERNAME ###
        SENDER_PASSWORD = "" ### ENTER PASSWORD ###
    elif MODE == "file_based":
        # Go to README.txt for how enter Absolute Path
        with open('C:/Users/Game/Documents/GitHub/account for Chula Newsletter.txt', "r") as account_file:
            CONTENT = account_file.read().splitlines() # .splitlines() for deleting the /n
            SENDER_EMAIL = CONTENT[0]
            SENDER_PASSWORD = CONTENT[1]


def sending_email(subject, body, sender_email, sender_password):
    """
    input: 
        subject is the subject of the email being sent
        body is the content in the email, such as links or images or text
        recepient is the email for the receiver
    output:
        email sent
    """
    SMTP_SERVER = "smtp.gmail.com" # default for Google
    SMTP_PORT = 587 # default for Google

    #login to email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login(sender_email, sender_password) # NOTE 1

    #For loop, sending emails to all email recipients
    for recipient in RECEPIENTS:
        print(f"Sending email to {recipient}")
        message = MIMEMultipart('alternative')
        message['From'] = sender_email
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'html'))
        text = message.as_string()
        server.sendmail(sender_email,recipient,text)

    #All emails sent, log out.
    server.quit()
    print(f"""
    Email sent to {recipient} from {sender_email}

    Subject: {subject}

    body: {body}""")


#%%

def check_for_page_update(site):
    global update
    update = False
    if path.exists(site.File_Compare):
        with open(site.File_Compare, "r") as Compare_File:
            if Compare_File.read() == str(page_section):
                print("No update")
            else:
                with open(site.File_Compare, "w") as Overwrite_File:
                    Overwrite_File.write(str(page_section))
                    print("File updated")
                    update = True
    else:
        with open(site.File_Compare, "w") as Compare_File:
            print('{0} is created'.format(site.File_Compare))
            check_for_page_update(site)


def make_hyperlink():
    global body_hyperlink
    link1 = BeautifulSoup(str(page_section), "html.parser").find_all("li")
    for a in BeautifulSoup(str(link1[0]), features="lxml").find_all('a', href=True):
        body_hyperlink = site.Parent_Link + a['href']
    print("created ", body_hyperlink)


def body_constructor(subject, body_hyperlink):
    global body
    subtitle1 = BeautifulSoup(str(page_section), "html.parser").find_all("span", class_ = "title2 trim")[0].text

    body = f"""<div>This email is sent by a Python bot made by DirtyRat<div>
    <div><h2>News date: {date1}<h2/><div>
    <div><h3>{subtitle1}<h3/><div>
    <div>Link to the news<div>
    <div>{body_hyperlink}<div>
    <div>Have a Nice Day ;)<div>
    """

def log_to_csv(site):
    if path.exists('main_log.csv'):
        with open("main_log.csv", "a") as Log_File:
            Log_File_writer = writer(Log_File)
            string_list = [site.Name, title1, str(datetime.datetime.now(pytz.timezone(TIMEZONE)))]
            Log_File_writer.writerow(string_list)
            print('Log successful')
            print(string_list)
    else:
        with open("main_log.csv", "w") as Log_File:
            Log_File_writer = writer(Log_File)
            Log_File_writer.writerow(["Site", "Title", "Date&Time"])
            print('A new CSV is made')
        log_to_csv(site)


# //div[contains(@class, "")]
#Set the endpoint: Worldometers
clear()
__init_account_from_file()
for site in SiteList:
    req = requests.get(site.Scrape_Link,'features="lxml"')
    page_section = BeautifulSoup(req.text, "html.parser").find_all("ul", class_ = "documents-list")
    check_for_page_update(site)
    if update:
        date1 = BeautifulSoup(str(page_section), "html.parser").find_all("span", class_ = "date")[0].text
        title1 = BeautifulSoup(str(page_section), "html.parser").find_all("span", class_ = "title trim")[0].text
        subject = title1 + "[Python Bot]"
        make_hyperlink() # returns body_hyperlink
        body_constructor(subject, body_hyperlink)
        sending_email(subject, body, SENDER_EMAIL, SENDER_PASSWORD)
        log_to_csv(site)
