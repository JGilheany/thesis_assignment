#name: trim_sequences.py

#author: Josh
#date: 22/11/2022

#description: Script to run trimmomatic on everything in a given folder, 


#import modules

import os

import subprocess


# set up directory variables
print("Welcome to the humble script: Please ensure you are running in the directory above your target directory")
print("Directories below:")
directorycommand = "ls -d */" #prints a list of dirs in working dir
os.system(directorycommand)

seq_dir =input("Please enter the name of the directory to trim: ")
trim_dir = input("Please enter the name of the new directory: ")# create output directory


    # get list of FASTQ files
try:
    file_list = os.listdir(seq_dir)
    print ('# got list of files in: ' + seq_dir)

    os.mkdir(trim_dir)
    print ('# created subdir: ' + trim_dir)
    # create the command string for each sequence
    # & implement it
    for seq in file_list:
        print(seq)
        command = 'trimmomatic '+'SE '+'-phred33 ' + seq_dir + '/' + seq +' Trimmed'+seq+ ' ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36'
        print(command)
        os.system(command)

        command1 = 'mv ' + 'Trimmed'+seq + ' ' + trim_dir
        print (command1)# mv trimmed files out of sequence directory
        os.system(command1)

except:
    print("Error, did you enter valid directories?")




print ('#done')
