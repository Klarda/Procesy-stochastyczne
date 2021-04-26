#!/usr/bin/env python
# coding: utf-8

# # Zadanie 3

# Stosując metodę Monte Carlo obliczyc wartość całki z podanej funkcji
# w granicach wzynaczonych przez jej miejsca zerowe. Porównać wyniki
# z wartością rzeczywistą (wykonaj odpowiedni test statystyczny).
# Wykonać odpowiednie ilustracje graficzne. Obliczenia powtórzyc przy
# samej i zmienionej liczbie losowych punktów

# a) $f(x)= 2x^2 - 17x + 21$

# In[13]:


#import bibliotek
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats
import math
import scipy


# In[2]:


# definicja liczby punktów i funkcji
N=1000
def funkcja1(x):
    return 2*x**2 - 17*x + 21


# In[3]:


# definicja funkcji pierwotnej
def funkcja2(x):
    return 2*x**3/3 - 17*x**2/2 +21*x


# In[4]:


# definujemy miejsca zerowe
x1=3/2
x2=7


# In[5]:


# definiujemy zakres y
#wierzchołek funkcji kwadratowej jest pomiędzy miejsacmi zerowymi
y1=funkcja1((x1+x2)/2)
y2=0


# In[6]:


# wynik teoretyczny
print(funkcja2(x2)- funkcja2(x1))


# In[16]:


pole=[]
for j in range(0,N):
    X=np.random.uniform(x1,x2,N)
    Y=np.random.uniform(y1,y2,N)
    p=0
    z=0
    for i in range(0,N):
        if Y[i]>=funkcja1(X[i]):
            p=p+1
        else:
            z=z+1
    pole.append((p/(p+z))*(x2-x1)*(y2-y1))
print(pole)


# # Zadanie domowe

# Dana jest funkcja $f\left(x\right)=\sqrt{-5x}-5$ oraz granice przedziału a=-5 i b=0. Używając metody MC wielokrotnie wynzacz wartość.

# In[17]:


#import bibliotek
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats
import math
import scipy


# In[19]:


# definicja liczby punktów i funkcji
N=1000
def f(x):
    return math.sqrt(-5*x) -5


# In[20]:


# definicja funkcji pierwotnej
def fp(x):
    return ((2/3)* math.sqrt(5)*math.sqrt(-x)-5)*x


# In[21]:


# definujemy miejsca zerowe
x1=-5
x2=0


# In[22]:


# definiujemy zakres y
#wierzchołek funkcji kwadratowej jest pomiędzy miejsacmi zerowymi
y1=0
y2=-5


# In[24]:


# wynik teoretyczny
print(fp(x2)- fp(x1))


# In[31]:


# definiowanie metody monte carlo
def Calka_MC(N,x1,x2,y1,y2,):
    pole=[]
    for j in range(0,N):
        X=np.random.uniform(x1,x2,N)
        Y=np.random.uniform(y1,y2,N)
        p=0
        z=0
        for i in range(0,N):
            if Y[i]>=f(X[i]):
                p=p+1
            else:
                z=z+1
        pole.append((p/(p+z))*(x2-x1)*(y2-y1))
    return pole


# In[33]:


Calka_MC(1000,-5,0,0,-5)


# In[40]:


# sprawdzanie czy rozkład jest normalny
normalny=scipy.stats.norm(np.mean(pole),np.std(pole))


# In[41]:


# testowanie hipotezy
print(scipy.stats.kstest(pole,normalny.cdf))


# In[47]:


#różnica pomiędzy wartością teoretyczną a średnia
print((fp(x2)- fp(x1))-np.mean(pole))


# In[46]:


#różnica pomiędzy wartością teoretyczną a mediana
print((fp(x2)- fp(x1))-np.median(pole))


# In[53]:


print(((fp(x2)- fp(x1))-np.mean(pole))/abs((fp(x2)- fp(x1)))*100)


# In[54]:


print(((fp(x2)- fp(x1))-np.median(pole))/abs((fp(x2)- fp(x1)))*100)


# In[ ]:





# In[ ]:




