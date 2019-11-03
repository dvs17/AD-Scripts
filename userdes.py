##!/usr/bin/python

import subprocess, os, argparse, time, datetime, socket, base64, threading, Queue, hashlib, binascii, signal, sys, getpass, multiprocessing, struct

file = "allinfo"
user = []
open_file = open(file, 'r')
count = 0
nextUser = False
userTemp = ""
groupTemp = ""
x = 0
y = 1
user.append([])
user.append([])

for line in open_file.readlines():
	if line == "\n":
		if nextUser:
			count += 1
			x += 2
			y += 2
			user.append([])
			user.append([])
			nextUser = False
	elif "sAMAccountName" in line:
		if not nextUser:
			nextUser = True
		user[x].append(line.strip().split(":")[1])
	elif "description" in line:
		user[y].append(line.strip().split(":")[1])

length = len(user)
length -= 1
x = 0
y = 1
while y != length:
	if len(user[y]) == 0:
		#print "The user \'" + user[x][0].strip() + "\' does not belong to any groups"
		pass
	else:
		for g in user[y]:
			print user[x][0].strip() + ":" + g
	x += 2
	y += 2



