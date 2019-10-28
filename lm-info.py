#!/usr/bin/python
'''
For extracting users stored in LM Hash and the password last set time
Created by DVS
'''
import sys
import getopt
try:
    opts, args = getopt.getopt(sys.argv[1:], 'h:', ['help'])
except getopt.GetoptError:
    print("Usage:python lm-info.py [DC-Hashes.ntds from secretsdump]")
    sys.exit(2)

for opt, arg in opts:
	if opt in ('-h', '--help'):
		print("Usage:python lm-info.py [DC-Hashes.ntds from secretsdump]")

file_1 = str(sys.argv[1])
users = ""
print "Username\tPassword Last Set"
for line_1 in open(file_1):
	line_1 = line_1.strip()
	line_1_split = line_1.split(":")
	if line_1_split[2] != "aad3b435b51404eeaad3b435b51404ee":
		line_1 = line_1.strip()
		userlm = line_1.split(":")[0]
		passlastset = line_1.split("=")[1].split(" ")[0].split(")")[0]
		if "status=Enabled" in line_1:
			print userlm+"\t"+passlastset