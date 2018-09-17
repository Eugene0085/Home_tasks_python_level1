# -*-  coding: Utf-8 -*-
import math
import os
import sys

# Задача1 Easy
def m_round(n,c):
    m=str(n).split(".")
    ss=m[1]

    k=1
    d=0
    s=str(n)
    n_s=str(n)+'  round =  '
    for i in range(0, len(s)):
        # print(s[i])
        sim = s[i]
        if s[i] == '.':
            d = k
        if k-d == c and d != 0:
            if i+1<=len(s)-1:
                if int(s[i+1])>=5:
                    sim=int(sim)+1
                    sim=str(sim)
                n_s = n_s + sim
                print(n_s)
                return
            # print()
        n_s=n_s+sim
        k += 1
    print(n_s)


   # Задача2 Easy
def luky_tic():
    b = str(input())
    if len(b)==6 and  b.isdigit():
        if int(b[0]) + int(b[1]) + int(b[2]) == int(b[3]) + int(b[4]) + int(b[5]):
            print("happy")
    else:
        print("ooops")





