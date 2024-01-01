# User-Defined Module----------------------------------------------------->
import module1
print(module1.sum(10,20))

from module1 import sum
print(sum(20,40))

from module1 import mul as m
print(m(10,20))

import module1 as m
print(m.mul(10,20))
print(m.sum(10,20))

from module1 import *
print(sum(100,200))
print(mul(100,200))

import SortSearch as ss
#print(dir(SortSearch))
ss.selection_sort([10,50,70,40,12])
ss.binary([10,20,40,50], 40)



# Built-in Module------------>

# Math ---------------->
import math as m
#print(dir(math))
print(m.ceil(10.2))
print(m.ceil(-10.2))

print(m.fabs(-10.2))

print(m.factorial(5))

print(m.floor(10.8))
print(m.floor(-10.8))

print(m.fsum([10,20,30,40]))
print(m.fsum({10,20,30,40,70}))
print(m.fsum((10,20,40)))

print(m.sqrt(9))
print(m.sqrt(10))

# Random Module---------
import random as r
#print(dir(random))

n1=r.randint(2,8)
print(n1)

n2=r.randrange(2,5)
print(n2)

l=[10,20,30,40]
n3=r.choice(l)
print(n3)

print(r.random()) # 0 to 1 float value

l=[10,20,30,40]
r.shuffle(l)
print(l)

print(r.uniform(3, 9)) # floot value between 3 and 9

# datetime module

import datetime as dt
print(dt.datetime.now())

print(dt.datetime(2022,7,15))

x=dt.datetime.now()
m=x.strftime("%y")
print(m)
