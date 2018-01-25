# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
print(namelist)

namet=[]
for name in namelist:
    namet.append(name[2:])
print(namet)

trimedname = map(lambda x : x[2:], namelist)
print(list(trimedname))

glob.glob('./*/*.csv')

class Version:
    def __init__(self, name, label):
        self.name = name
        self.label = label
        self.x = []
        self.y = []
        self.cumulative = []
        
label=[]
for name in namet:
    label.append(name[27:-4])
print(label)

inslist =[]
for name in namet:
    labelname = name[27:-4]
    ins = Version(name,labelname)
    cumulative = 0
    with open(name, newline='') as name:

        reader = csv.reader(name)
        for row in reader:
            ins.x.append(float(row[0]))
            ins.y.append(float(row[1]))
            cumulative = cumulative + float(row[1])
            ins.cumulative.append(cumulative)
        print(ins.name)
        print(ins.label)
        print(ins.x)
        print(ins.y)
        print(ins.cumulative)
        inslist.append(ins)
print(inslist)
for ins in inslist:
    print(ins.label)
    
plt.title("wall_heat_flux")
for ins in inslist:
    plt.plot(ins.x,ins.y,label=ins.label)

plt.title("cumulative_wall_heat_flux")
for ins in inslist:
    plt.plot(ins.x,ins.cumulative,label=ins.label)

        