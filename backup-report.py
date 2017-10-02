# Note that this uses Python 3

from datetime import date
#import os
#from os.path import join, getsize
#from shutil import copy, copy2
#import sys

def prompter():
    # wait for user input - at the end of the program and for debugging
    input("Press ENTER to continue...")

# M A I N L I N E
# convert date into a form suitable for the report file
today_date = date.today()
today_date = today_date.strftime("%d%b%Y")

backup = -1
backups = ["NTI50-C", "NTI50-D", "Nspire-pat-C", "RPi3-5-pihome"]
seq = None
log_file = open('D:\\users\\vinntec\\Downloads\\rsync', 'r')
report = open("reports\\backup " + today_date + ".txt", 'w')
for inar in log_file:
    inar = inar[:len(inar)-1] # remove newline
    if inar[28:46] == "building file list":
        seq = inar[20:27]
        backup += 1
        if backup != 0:
            report.write('\n')
        report.write(seq + " Backup of " + backups[backup] + '\n')
    elif inar[20:27] == seq and (inar[28] != '>' and inar[28] != '.' and inar[28:30] != "cd"):
        # Message about this run
        report.write(inar[28:] + '\n')
    elif inar[20:27] == seq and inar[26:30] == "] >f":
        # file backup found
        report.write(inar[40:] + '\n')

print('Backup Report Complete')
report.close()
log_file.close()
prompter()
