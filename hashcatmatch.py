#!/usr/bin/python
'''
For matching cracked hash and username for hashcat NTLM
Created by DVS
'''
import sys
import getopt
try:
    opts, args = getopt.getopt(sys.argv[1:], 'h:', ['help'])
except getopt.GetoptError:
    print("Usage: hashcatmatch [DC hashes file] [cracked hash file]")
    sys.exit(2)

for opt, arg in opts:
	if opt in ('-h', '--help'):
		print("Usage: hashcatmatch [DC hashes file] [cracked hash file]")

file_1 = str(sys.argv[1])
file_2 = str(sys.argv[2])

for line_1 in open(file_1):
	line_1 = line_1.strip()
	line_1_split = line_1.split(':')
	#print line_1_split[3]
	for line_2 in open(file_2):
		line_2 = line_2.strip()
		line_2_split = line_2.split(':',1)
		#print line_2_split[0]
		if line_1_split[3] == line_2_split[0]:
			print(line_1_split[0]+":"+line_2_split[1])
