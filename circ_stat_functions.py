#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('cd', 'C:\\Users\\MooreLab\\spatial memory')


# In[3]:


import numpy as np
import math
import sympy
import scipy
import matplotlib.pyplot as plt
from scipy import special
from sympy import *


# In[ ]:


# In[ ]:


# Define some parameters
binsize_generative = 2*np.pi/8
binsize_fit        = 2*np.pi/100

# generate x values
theta_generative = np.arange(-np.pi, np.pi - binsize_generative, binsize_generative)
theta_fit = np.arange(-np.pi, np.pi - binsize_fit, binsize_fit)

theta_generative = np.append(theta_generative, 2.35619449)
theta_fit = np.append(theta_fit, 3.0787608100000003)


# In[ ]:


def cresultant(X, Y):
    R = sum(Y * np.exp(1j*X)) / sum(Y)
    return R 


# In[ ]:


def cmean(X, Y):
    M = np.angle(cresultant(X,Y))
    return M


# In[ ]:


def cstd(X, Y):
    R = np.abs(cresultant(X,Y))
    S = np.sqrt(-2 * np.log(R))
    return S


# In[ ]:


def sd2k(S):
    R = np.exp((-np.power(S,2))/2)
    K = fastAlinv(R)
    return K 


# In[2]:


def fastAlinv(R):
    R = np.asarray(R)
    R = R.flatten()
    #print(R)
    length = len(R)
    K = np.zeros(length)
    
    index = np.where((R >= 0) & (R < 0.53))
    K[index] = 2 * R[index] + np.power(R[index],3) + ((5 * np.power(R[index], 5))/6)
    
    index = np.where((R >= 0.53) & (R < 0.85))
    K[index] = -0.4 + 1.39 * R[index] + np.divide(0.43, (1-R[index]))
    
    index = np.where((R >= 0.85) & (R <= 1))
    K[index] = np.divide(1, (np.power(R[index], 3) - 4 * np.power(R[index], 2) + 3 * R[index]))
    
    return K 


# In[ ]:


def besseliln(nu, z):
    w = np.log(scipy.special.ive(nu,z)) + np.abs(z.real)
#     print(w)
    return w 


# In[ ]:


def vonmisespdf(x, mu, k):
    p = np.exp(np.multiply(k, np.cos(x-mu)) - np.log(2*np.pi) - besseliln(0,k))
    return p


# In[ ]:

def objective(x, alpha, k, mu):
    return alpha * np.exp(k * np.cos(x-mu))

def peakConfidence(x, alpha, k, mu):
#     peakConfidence_fit = vonmisespdf(mu, mu, k) * binsize_generative
    peakConfidence_fit = objective(x, alpha, k, mu) * binsize_generative
    return peakConfidence_fit


# In[ ]:


# plt.plot(theta_fit, pdf_fit)

