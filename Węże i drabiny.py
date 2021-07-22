#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats


# In[4]:


def rzutkostka(b): #b-liczba ścian kostki
    a=np.random.randint(1,b+1)
    return a


# In[5]:


def gra(b): #b-liczba ścian kostki
    X=[0]
    while X[-1]<24:
        c=rzutkostka(b)
        x=c+X[-1]
        if x==4:
            X.append(16)
        elif x==12:
            X.append(14)
        elif x==18:
            X.append(9)
        elif x==23:
            X.append(3)
        else:
            X.append(x)
    return X


# In[6]:


def pred(b,n,N): #b-liczba ścian kostki, n-liczba rzutów kostki, N-wielkość próby do obliczenia populacji
    ln=[]
    for i in range(1,N):
        if len(gra(b))==n:
            ln.append(1)
    return(len(ln)/N)


# In[10]:


pred(6,8,1000)


# In[ ]:




