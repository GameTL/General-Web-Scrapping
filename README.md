
# General-Web-Scrapping

> Collection of all my web scrapping projects that are pretty small.

- [General-Web-Scrapping](#general-web-scrapping)
  - [2021/12/28](#20211228)
  - [2021/12/21](#20211221)
  - [2021/12/18](#20211218)
  - [2021/12/17](#20211217)
  - [2021/09/10](#20210910)
  - [**How to run a batch file with windows**](#how-to-run-a-batch-file-with-windows)

## 2021/12/28

- ### **General CleanUp**

  - Update the README.md file, so it's more readable.
  - logger function files are moved to the dependancy folder.
  - All of the python files that uses the logger file has their import changed from "import logger" to "import dependances.logger as logger"

- ### **1.0 - Preend Csv With DateTime**

  - Add Human readable date time to the second column of the csv file, given the first column is time in seconds.

## 2021/12/21

- ### **1.1 - Logger Library**

  - added function log2csv() for use for all logging has try and except function
  - added support for and only Windows notification for failed logging

- ### **v3.4 - Cryptocurrency price logging**

  - Use Logger.py function log2csv(), this decrease repition of code

- ### **v1.4 - Nicehash balance logging**

  - Use Logger.py function log2csv(), this decrease repition of code

## 2021/12/18

- ### **v3.2 - Cryptocurrency price logging**

  - added support for and only Windows notification for failed logging

- ### **v1.2 - Nicehash balance logging**

  - added support for and only Windows notification for failed logging

## 2021/12/17

- ###  **v3.0 - Cryptocurrency price logging**

  - using API
  - more efficient, using less CPU Time

- ### **v1.1 - Nicehash balance logging**

  - using Nicehash API

## 2021/09/10

- ### **v2.0 - Cryptocurrency price logging**

  - The python code now runs more efficiently

-----

## **How to run a batch file with windows**

1. select the disk which the python file is on
2. change directory to the folder with python file
3. run the python file with the interpreter. {interpreter absolute path} .\\{python file relative path}

>e:\
cd "E:\Personal - GDrive\Cron Jobs\Logging Crypto Prices - 2021.05(May). 24"\
C:\Anaconda3\python.exe .\Log_Prices.py

Invisible CMD
<https://www.howtogeek.com/tips/how-to-run-a-scheduled-task-without-a-command-window-appearing/>
