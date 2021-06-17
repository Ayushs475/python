# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:54:49 2021

@author: nikku
"""

from Friendclass import Friend
flist=[]
def add_new_friend():
    fid=int(input("enetr fid"))
    nm=input("enetr name")
    m=input("enter mobile")
    f=Friend(fid,nm,m)
    flist.append(f)
    
def display_all():
    for f in flist:
        print(f)
        
def searchbyname(nm):
    for f in flist:
        if f.getName() == nm:
            return f
    return None


def searchbymobile(mob):
    for f in flist:
        if f.getMobile()==mob:
            return f 
    else:
        return None

def deletefriend(nm):
    f=searchbyname(nm)
    if f!=None:
        flist.remove(f)
        return True
    return False
def modifymobile(nm,nmob):
    f=searchbyname(nm)
    if f!=None:
        f.setMobile(nmob)
        return f
    else:
        return None