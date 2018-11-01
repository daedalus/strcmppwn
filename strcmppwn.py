#!/usr/bin/env python
# Author Dario Clavijo 2018
# GPLv3
# POC: strcmp timing attack
# -*- coding: utf-8 -*-

target = "My super secret passphrase."
print ("Real: %d" % len(target))

def strcmp(a,b):
	if len(a) != len(b):
		return 1
	for i in range(0,len(a)):
		if a[i] != b[i]:
			return 1
	return 0

import time
def gettime():
	return time.time()

def measure(cand):
	res = 5000
	#res = 10000

	t0 = gettime()
	for k in range(0,res):
        	ret = strcmp(target,cand)
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
	print ("best: %d,%2.10f" % (best,best_i))
	return best_i

def pwnOracle():
	l =  guess_len()
	print ("guess_len: %d" % l)
	candidate = list("A" * l)
	tmp = ""
	for i in range(0,l):
		best = 0.00000000000000000
		best_c = ""
		#for j in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. ":
		for c in range(0,255):
			#c = ord(j)
			candidate[i] = chr(c)
			d = measure("".join(candidate))
			if d > best:
				best = d
				best_c = chr(c)
			print ("%s %2.10f" % (candidate,d))
		candidate[i] = best_c
		tmp += best_c
		print ("Best: %s" % tmp)

pwnOracle()
