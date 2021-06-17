# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:53:32 2021

@author: nikku
"""

class Friend:
    location='Deccan'
    def __init__(self,pid=0,nm='',mob=''):
        self.__pid=pid
        self.__name=nm
        self.__mobile=mob
        
        
    def __str__(self):
        return "Id: "+str(self.__pid)+"\nName: "+self.__name+"\nMobile : "+self.__mobile
    
    def getPid(self):
        return self.__pid
    def getName(self):
        return self.__name
    def getMobile(self):
        return self.__mobile
    
    def setPid(self,pid):
        self.__pid=pid
        
    def setName(self,nm):
        self.__name=nm
        
    def setMobile(self,mob):
        self.__mobile=mob
       
    @staticmethod
    def method1(a):
        print("this is static method",a)
        
    
if __name__=='__main__':
    p=Friend(12,'Kishori','11111')
    print(p)
    print(p.getMobile())
    print("location :",Friend.location)
    Friend.method1('XXX')