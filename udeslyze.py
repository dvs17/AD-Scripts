#!/usr/bin/python
import sys
import os
import re
import getopt
try:
    opts, args = getopt.getopt(sys.argv[1:], 'c:h:', ['common','help'])
except getopt.GetoptError:
    print "Usage: ./udeslyze [user description file] [company name]"
    sys.exit(2)
companyname = sys.argv[2]

file = open(sys.argv[1], "r")
for line_1 in file:
	line_1 = line_1.strip()
	if re.findall("password|training|trainer|printer|scanner|parking|pwd|passwd|psswd|p455|pa55|p4ss|pa$$|p4$$|pa$$|pa55|p@55|p@ss|P@$$|account|login|logon|creds|qwerty", line_1, re.IGNORECASE):
		passw = line_1
		print "\033[91m" + passw + "\033[91m"
	if re.findall("summer|autumn|winter|spring", line_1, re.IGNORECASE):
		summ = line_1
		print '\033[94m' + summ + '\033[94m'
	if re.findall("monday|tuesday|wednesday|thursday|friday|saturday|sunday", line_1, re.IGNORECASE):
		days = line_1
		print '\033[92m' + days + '\033[92m'
	if re.findall ("january|february|march|april|may|june|july|august|september|october|november|december", line_1, re.IGNORECASE):
		mon = line_1
		print '\033[93m' + mon + '\033[93m'
	if re.findall ("abc([0-9])", line_1, re.IGNORECASE):
		ab = line_1
		print '\033[90m' + ab + '\033[90m'
	if re.findall ("\b\d+\b", line_1, re.IGNORECASE):
		numb = line_1
		print '\033[95m' + numb + '\033[95m'
	if re.findall (companyname+"([0-9])", line_1, re.IGNORECASE):
		company = line_1
		print '\033[96m' + line_1 + '\033[96m'


