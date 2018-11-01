#!/usr/bin/env python
# Author Dario Clavijo 2018
# GPLv3
# POC: strcmp timing attack
# -*- coding: utf-8 -*-

target = "My super secret passphrase..."
print ("Size: %d" % len(target))
print ("Target: %s" % target)

def strcmp(a,b):
	if len(a) != len(b):
		return 1
	for i in range(0,len(a)):
		if a[i] != b[i]:
			return 1
	return 0


def strcmp2(a,b):
	return a == b

import time
def gettime():
	return time.time()

def measure(candidate):
	res = 10000
	#res = 10000
	t0 = gettime()
	for k in range(0,res):
        	strcmp(target,candidate)
		#strcmp2(target,candidate)
	t1 = gettime()
	return (t1-t0)

def guess_len():
	best = 0.000000000000000000000
	for i in range(1,30):
		t = measure("A" * i)
		print ("%d,%2.10f" % (i,t))
		if t >= best:
			best = t
			best_i = i
	#print ("best: %d,%2.10f" % (best_i,best))
	return best_i

def chargen(alpha=False):
	if alpha:
		for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. ":
			yield c
	else:
		for i in range(0,255):
			yield chr(i)

def pwnOracle():
	l =  guess_len()
	print ("guess_len: %d" % l)
	candidate = list(" " * l)
	tmp = ""
	for i in range(0,l):
		print("pos: %d" % (i+1))
		best = 0.00000000000000000
		best_c = ""
		for c in chargen(True):
			candidate[i] = c
			d = measure("".join(candidate))
			if d > best:
				best = d
				best_c = c
			print ("%s %2.10f" % (candidate,d))
		candidate[i] = best_c
		tmp += best_c
		print ("Best: %s" % tmp)

pwnOracle()
