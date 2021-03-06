# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import time

N = 100000 # number of MC events
N_run = 100 # number of runs

start_time = time.time() # start clock 

pi=np.mean(np.mean(np.where(np.sum(pow(np.random.rand(N_run,2,N),2),axis=1)<1,1,0),axis=0)*4)

run_time = time.time()

print("pi with ", N, " steps for ", N_run, " runs is ", pi, " in ", run_time-start_time, " sec")
print("Precision computation : ", np.abs(pi-np.pi))



