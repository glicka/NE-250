#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:17:53 2017

@author: glicka
"""

#### This code answers problem 4 parts a and b but I generate my own random
#### numbers rather than what is given in the problem definition.

import numpy as np
import scipy as sp
import random as rand
import matplotlib.pyplot as plt
import math
import matplotlib.mlab as mlab
from scipy.stats import norm
import time


sigT1 = 1
sigS1 = 0.5
sigA1 = sigT1-sigS1
sigT2 = 0.9
sigS2 = 0.75
sigA2 = sigT2-sigS2

# PDF = 1 - np.exp(-sigT*x)
# x = -ln(1-xiT)/sigT = -ln(xiT)/sigT

noSamples = 1000
colTally1 = 0
scatterTally1 = 0
absTally1 = 0
colTally2 = 0
scatterTally2 = 0
absTally2 = 0
angScatter = 0
R1 = 1 #distance to first boundary [cm]
R2 = 500 #distance to second boundary [cm]
distTraveled = 0
wnom1 = 1
wmax1 = wnom1*2.5
wmin1 = wnom1/2.5
wnom2 = 2
wmax2 = wnom2*2.5
wmin2 = wnom2/2.5

for i in range(0,int(noSamples)):
    distTraveled = 0
    noGo = 0 #Switch to determine if second 
    rand.seed(time.time())
    counter1 = 0
    counter2 = 0
    #determining direction particle is born in phi [0,2pi]
    phi0 = 2*np.pi*rand.random()
    #determining direction particle is born in mu [-1,1]
    mu0 = 2*rand.random() - 1 
    #Particles are born with weight 1
    w0 = 1 
    if i%10000 == 0:
        print('i = ',i)
    #random number (probability) for determining distance particle travels
    xiX = rand.random() 
    #inverting PDF to determine distance particle traveled before collision
    x = -math.log(xiX)/sigT1 
    distTraveled += x
    Rupdated1 = R1/(np.sin(phi0)*mu0)
    Rupdated2 = R2/(np.sin(phi0)*mu0)
    #random number for Rouletting Ratio comparison in region 1
    xiRR1 = rand.random() 
    RR1 = w0/wnom1
    if RR1 > xiRR1:
        while Rupdated1 >= 0:
    #random number (probability) for determining distance particle travels
            xiX = rand.random() 
    #inverting PDF to determine distance particle traveled before collision
            x = -math.log(xiX)/sigT1 
            distTraveled += x
    #print(distTraveled)
            colTally1 += 1
            if x <= Rupdated1:
    #random number (probability) to determine which collision occured
                xiS1 = rand.random() 
                if 0 < xiS1 <= sigS1:
                    scatterTally1 += 1
    #determining direction of scatter in phi [0,2pi]
                    phi = 2*np.pi*rand.random() 
    #determining direction of scatter in mu [-1,1]
                    mu = 2*rand.random() - 1 
                    Rupdated1 = (Rupdated1-x)/(np.sin(phi)*mu)
                    #print(Rupdated1)
                else:
                    absTally1 += 1
                    noGo = 1
                    break
            else:
                break
    #random number for Rouletting Ratio comparison in region 2
    xiRR2 = rand.random() 
    RR2 = w0/wnom2
    #Roulette comparison to determine if particle is killed or not (variance reduction method)
    if RR2 > xiRR2: 
        while Rupdated2 >= 0 and noGo == 0:# distTraveled:
    #random number (probability) for determining distance particle travels
            xiX = rand.random() 
    #inverting PDF to determine distance particle traveled before collision
            x = -math.log(xiX)/sigT2 
            colTally2 += 1
            if x <= Rupdated2:
                print(distTraveled)
                xiS2 = rand.random()
                distTraveled += x
                if 0 < xiS2 <= sigS2:
                    scatterTally2 += 1
    #determining direction of scatter in phi [0,2pi]
                    phi = 2*np.pi*rand.random() 
    #determining direction of scatter in mu [-1,1]
                    mu = 2*rand.random() - 1 
                    Rupdated2 = (Rupdated2-x)/(np.sin(phi)*mu)
                else:
                    absTally2 += 1
                    break
            else:
                break
        
print('collision tally1 = ',colTally1)
print('collision tally2 = ',colTally2)
print('absorption tally1 = ',absTally1)
print('scatter tally1 = ',scatterTally1)
print('absorption tally2 = ',absTally2)
print('scatter tally2 = ',scatterTally2)

