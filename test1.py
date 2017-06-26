#!/usr/bin/env python
#coding=utf-8
import numpy as np
import csv
import os
import time
from help import *
from getdataonp import *
import math
from argu import *
#start=time.clock()
#f1=open('/Users/puyeqing/Documents/bigdata/fresh_comp_offline/tianchi_fresh_comp_train_user.csv')
#
#f2=open('/Users/puyeqing/Documents/bigdata/fresh_comp_offline/tianchi_fresh_comp_train_item.csv')
#
#content1=f1.readlines()
#content2=f2.readlines()
#######################################################################################
def test1():
    fr=open('/Users/puyeqing/Documents/bigdata/dataonp.csv')
    content3=fr.readlines()
    #print1info(content3)
    #get day 2,3,4 add cart and day 5 buy data
    adduseritemcatset=set()
    buyuseritemset=set()
    totaluseritemset=set()
    usercatdict={}
    adduseritemset=set()
    #先得出每个类中的商品ID特征
    for line in content3:
        array=line.split(',')
        str1=array[5].split()[0]
        if(str1==day1 or str1==day2 or str1==day3):
            uid=(array[0],array[1],array[4])
            totaluseritemset.add((array[0],array[1]))
            if(array[2]=='3'):
                #adduseritemset.add((array[0],array[1]))
                adduseritemcatset.add((array[0],array[1],array[4]))
                uid2=(array[0],array[4])
                if(not(uid2 in usercatdict)):
                    usercatdict[uid2]=1
                else:
                    usercatdict[uid2]=usercatdict[uid2]+1    
    for u in adduseritemcatset:
        usercat=(u[0],u[2])
        if(not(usercat in usercatdict) or (usercatdict[usercat]<=minus)):
            useritem=(u[0],u[1])
            adduseritemset.add(useritem)

                            
                        
    for line in content3:
        array=line.split(',')
        str1=array[5].split()[0]
        if(str1==day4): 
            uid=(array[0],array[1])
            if(uid in totaluseritemset):
                if(array[2]=='4'):
                    buyuseritemset.add(uid)   
    print len(adduseritemset)
    print len(buyuseritemset)
    print len(totaluseritemset)
    print len(usercatdict)
    count=0
    for s in adduseritemset:
        if(s in buyuseritemset):
            count=count+1
    print count

    printf1(count,len(buyuseritemset),len(adduseritemset))
#X=np.zeros((len(totaluseritemset),1))
#printf1(58,143,5044)
#Y=np.zeros((len(totaluseritemset)),)
#totaluseritemlist=list(totaluseritemset)
#id=0
#for ui in totaluseritemlist:
#    if(ui in adduseritemset):
#        X[id][0]=math.log1p(1)
#    if(ui in buyuseritemset):
#        Y[id]=1
#
#from sklearn.linear_model import LogisticRegression
#model=LogisticRegression()
#model.fit(X,Y)        

#count=0
#for s in buyuseritemset:
#    if(not(s in adduseritemset)):
#        count=count+1
#print count 
#print len(adduseritemset)
#print len(totaluseritemset)
#print len(buyuseritemset)   
#X=np.zeros(len(totaluseritemset),1)     

