#!/usr/bin/python
#------------------------------------------------------------------------#
import subprocess
import sys
def rf_check():
	rf="hello"
	try:
		rf = subprocess.Popen("ncli cluster get-redundancy-state | grep Desired | awk {'print $5'}", shell=True, stdout=subprocess.PIPE).stdout.read()
		print "Desired RF", rf
	except:
		sys.exit()
	return rf

def space_check(rf):
	try:
		print "Desired RF", rf
	except:
		sys.exit()

def main():
	rf = rf_check()
	space_check(rf)
