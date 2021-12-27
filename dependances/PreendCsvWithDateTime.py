
# adding DateTime to the second colum of the csv file
# ONLY WORKS IF THE FIRST COLUM IS TIME IN SECONDS
import logger


####SETUP####
FILE_PATH = "D:\Personal - GDrive\Cron Jobs\General-Web-Scrapping\\Nicehash_logger\\NiceHashBalance.csv"
#############


output_file = FILE_PATH[:-4] + "_DateTimeUpdate.csv"

temp = []
output = []
with open(FILE_PATH, 'r') as f:
    lines = f.readlines()
    for i in lines:
        temp.append(i.split(','))

for i, l in enumerate(temp):
    if i == 0:
        l.insert(1, '"DateTime"')
    else:
        l.insert(1, f'"{logger.get_human_date_time(float(l[0][1:-1]))}"')
    
    output.append(','.join(l))


with open(output_file, 'w') as f:
    f.writelines(output)


