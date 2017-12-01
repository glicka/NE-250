#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:14:02 2017

@author: glicka
"""

import numpy as np
import scipy as sp
import random as rand
import matplotlib.pyplot as plt
import math
import matplotlib.mlab as mlab
from scipy.stats import norm
#f(x) = np.exp(-x)


m = np.array([10,40,160])
for n in m:
    a = []
    b = 0
    c = []
    for i in range(0,n-1):
        b = rand.random()
        c += [b]
        a += [-np.log(b)]
    
#print('a = ',a)
#print('c = ',c)
    a = np.array(a,dtype = 'float')
    a.sort()
    c = np.array(c,dtype = 'float')
    c = sorted(c,reverse = True)
    if n == 10:
        plt.plot(c,a)
        plt.title('iterations = 10')
        plt.show()
    if n == 40:
        plt.plot(c,a)
        plt.title('iterations = 40')
        plt.show()
    if n == 160:
        plt.plot(c,a)
        plt.title('iterations = 160')
        plt.show()
    avg = np.mean(c)
    var = np.var(c)

    print(avg)
    print(var)
    
avg = []
var = []
for i in range(0,100):
    d = []
    e = []
    f = 0

    for m in range(0,100):
        f = rand.random()
        e += [f]
        d += [-np.log(f)]
    
#print('a = ',a)
#print('c = ',c)
    d = np.array(d,dtype = 'float')
    d.sort()
    e = np.array(e,dtype = 'float')
    e = sorted(e,reverse = True)      
    avg += [np.mean(d)]
    var += [np.var(d)]
    #print(avg)
    
avg = np.array(avg,dtype = 'float')
var = np.array(var,dtype = 'float')
aHist, aBins = np.histogram(avg,bins=10)
aB = aBins[0:10]
aHist = aHist/max(aHist)#aHist/max(aHist)
print(sum(aHist))
mu = 1
variance = np.var(avg)
sigma = np.sqrt(variance)

x = np.linspace(min(aB), max(aB), 1000)
plt.plot(x,mlab.normpdf(x, mu, sigma)/4)
plt.scatter(aB,aHist)
plt.show()
     
    
    

