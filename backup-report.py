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
    ix = inar.find("building file list")
#    if inar[28:46] == "building file list":
    if ix != -1:
        start_msg = ix
#        seq = inar[20:27]
        start_seq = inar.find('[') + 1
        if start_seq == -1:
            print("Error - unable to find '['")
        end_seq = inar.find("]")
        if end_seq == -1:
            print("Error - unable to find ']'")
#        seq = inar[20:27]
        seq = inar[start_seq:end_seq]
#        print("-->" + seq + "<--")
#        print("-->" + inar[start_seq:end_seq] + "<--")
        backup += 1
        if backup != 0:
            report.write('\n')
        report.write(seq + " Backup of " + backups[backup] + '\n')
#    elif inar[20:27] == seq and (inar[28] != '>' and inar[28] != '.' and inar[28:30] != "cd"):
    elif inar[start_seq:end_seq] == seq and (inar[start_msg] != '>' and inar[start_msg] != '.' and inar[start_msg + 1] != 'd'):
        # Message about this run
#        print("Message about this run")
#        report.write(inar[28:] + '\n')
        report.write(inar[start_msg:] + '\n')
#    elif inar[20:27] == seq and inar[26:30] == "] >f":
    elif inar[start_seq:end_seq] == seq and inar[start_msg:start_msg + 2] == ">f":
        # file backup found
#        print("File backup found")
#        report.write(inar[40:] + '\n')
        report.write(inar[start_msg + 12:] + '\n')

print('Backup Report Complete')
report.close()
log_file.close()
prompter()
