#! /usr/bin/env python3

import time
import sys
seconds = time.time()

def is_prime_1(x):
	result = True
	for i in range(2,x):
		if x%i == 0:
			result = False
			break
	return result

def is_prime_2(x):
	result = True
	for i in range(2,int(x**(0.5)+1)):
		if x%i == 0:
			result = False
			break
	return result

def num_of_prime(n,metodo):
	prime_list = [1,2]
	if metodo == '1':
		for x in range(3,n+1):
			if is_prime_1(x):
				prime_list.append(x)
	if metodo == '2':
		for x in range(3,n+1):
			if is_prime_2(x):
				prime_list.append(x)
	print(prime_list)

num_of_prime(int(sys.argv[1]),sys.argv[2])
print(time.time()-seconds)
