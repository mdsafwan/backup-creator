# -*- coding:utf-8 -*-
__version__ = 1.0
__author__ = 'Mohamed Safwan'
'''Create a backup for a directory'''



import os
import time
import extract_folder

print "\n****BACKUP CREATER 1.0****"

source_dir = raw_input("\nEnter the source directory path:\n")
target_dir = raw_input("\nEnter the target directory path:\n")

#Extract folder name from source directory path
folder = extract_folder.extract(source_dir)	

target = target_dir + "(backup)" + folder + ".zip"

if not os.path.exists(target_dir):
	os.mkdir(target_dir)
	
zip_command = "zip -r {0} {1}" .format(target,source_dir)

print "\nCreating backup in a zip file..."
if os.system(zip_command) == 0:
	time.sleep(2)
	print "Backup created successfully\n"
	print "The backup is stored at:", target
else:
	print "Backup Failed!!!"
