#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:39:20 2018

@author: fiction
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import glob
namelist = []
namelist = glob.glob('./*.csv')
#LES_2017after内のWallHF_ave_time~~~.csvを読み出したい
#それはやめとく　GP4と他を区別するのが面倒
#こうやって、そのフォルダ内のｃｓｖを読み出すのは共通の機能にしておく
'''
p_fuel_180118a_single_L.csvといったファイル名
同じRのファイルをフォルダに突っ込む→グラフを作成
'''
#print(namelist)

namet=[]
for name in namelist:
    namet.append(name[2:])
print(namet)

trimedname = map(lambda x : x[2:], namelist)
#print(list(trimedname))


class Version:
    def __init__(self, name, label):
        self.name = name
        self.label = label
        self.x = []
        self.y = []
        self.slope = []
        self.smoothslope = []
        

width = 0.5000000E-04
inslist =[]
for name in namet:
    labelname = name[15:-4]
    ins = Version(name,labelname)
    
    with open(name, newline='') as name:

        reader = csv.reader(name)
        readerlist = list(reader)
        readerlist = readerlist[1:]
        
        for row in readerlist:
            ins.x.append(float(row[1]))
            ins.y.append(float(row[3]))
            
            
#        print(ins.name)
#        print(ins.label)
#        print(ins.x)
#        print(ins.y)
#        print(ins.cumulative)
        inslist.append(ins)

for ins in inslist:
    for i in range(len(ins.y)-1):
        ins.slope.append(float(ins.y[i+1]-ins.y[i])/width)
    ins.slope.append(ins.slope[len(ins.y)-2])

#param_aveは移動平均近似のパラメータ
param_ave = 501
half_param_ave = int((param_ave - 1)/2)

c = np.array(1)


for ins in inslist:
    a = np.array(list(ins.slope))
    b = np.ones(param_ave)/float(param_ave)
    c = np.convolve(a,b,'valid')
    ins.smoothslope = c.tolist()
       


for ins in inslist:
    print(ins.label)
    
plt.figure()
ax1 = plt.subplot(211)
plt.title("p_ambient")
for ins in inslist:
    plt.plot(ins.x,ins.y,label=ins.label)
#plt.xlabel('time(ms)')
plt.ylabel('Pressure(bar)')
plt.setp(ax1.get_xticklabels(), visible=False)
#plt.legend()
plt.grid()
#plt.show()

#plt.subplot(312)
#plt.title("dp/dt")
#for ins in inslist:
#    plt.plot(ins.x,ins.slope,label=ins.label)
#plt.xlabel('time(ms)')
#plt.ylabel('dp/dt')
#plt.legend()
#plt.grid()
#plt.show()
ax2 = plt.subplot(212, sharex=ax1)
plt.subplot(212)
plt.title("dp/dt_movingAve")
for ins in inslist:
    xfixed = ins.x[half_param_ave:-half_param_ave]
    plt.plot(xfixed,ins.smoothslope,label=ins.label)
plt.xlabel('time(ms)')
plt.ylabel('dp/dt')
plt.legend()
plt.grid()
plt.show()