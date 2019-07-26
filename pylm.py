#!/usr/bin/python
global str
import sys
import os
import re


file_DC = open("DC-Hashes.txt", "r")

for line_2 in file_DC:
        line_2 = line_2.strip()
        line_2_split = line_2.split(':')
        if line_2_split[2] != "aad3b435b51404eeaad3b435b51404ee":
                print line_2_split[0]

