# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 01:52:40 2019

@author: power
"""

import numpy as np
import os
import csv
import glob



class Version:
    def __init__(self, name, label):
        self.name = name
        self.label = label
        self.x = []
        self.y = []
        self.slope = []
        self.smoothslope = []

print('case?')
case=str(input())  
os.chdir("c:\\Users\\power\\Desktop\\python\\"+case)
cdic = {'xtip':'xtip_','WHF_area':'WHFarea','shapeWall':'RAVE','P_SCH':'SCHMASS','p_dpdt':'p_fuel','allWHF':'log'}
'''main'''
namelist = []
namelist = glob.glob('./*'+cdic[case]+'*.csv')
#LES_2017after内のWallHF_ave_time~~~.csvを読み出したい
#それはやめとく　GP4と他を区別するのが面倒
#こうやって、そのフォルダ内のｃｓｖを読み出すのは共通の機能にしておく
'''
xtip_190527a_single_ss.csvといったファイル名
同じRのファイルをフォルダに突っ込む→グラフを作成
'''

namet=[]
for name in namelist:
    namet.append(name[2:])
#print(namet)



casedic = {'xtip':13,'WHF_area':8,'shapeWall':15,'P_SCH':20,'p_dpdt':15,'allWHF':19}
rowdic = {'xtip':2,'WHF_area':7,'shapeWall':1,'P_SCH':3,'p_dpdt':3,'allWHF':2}

trimedname = map(lambda x : x[2:], namelist)
#print(list(trimedname))
width = 0.5000000E-04
inslist =[]
length = []
for name in namet:
    labelname = name[casedic[case]:-4]
    ins = Version(name,labelname)
    
    with open(name, newline='') as name:

        reader = csv.reader(name)
        readerlist = list(reader)
        readerlist = readerlist[1:]
        
        for row in readerlist:
            ins.x.append(float(row[1]))
            ins.y.append(float(row[rowdic[case]]))

        inslist.append(ins)
        length.append(len(ins.y))
    


os.chdir("c:\\Users\\power\\Desktop\\python")

with open('all'+case+'.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(['count']+[ins.label for ins in inslist])
    for i in range(min(length)):
        spamwriter.writerow([i]+[ins.y[i] for ins in inslist])

         