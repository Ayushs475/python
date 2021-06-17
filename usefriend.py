# -*- coding: utf-8 -*-
import sys
from Friendservice import*
choice=0
while choice!=7:
    print("1.add new Friend\n 2.delete friend details\n 3. search by name\n")
    print(" 4. search by mobile\n5. modify mobile\n 6. Display all 7.exit")
    choice=int(input("enetr choice"))
    if choice==1:
        add_new_friend()
    elif choice==2:
         nm=input("enetr name")
         ans=deletefriend(nm)
         if ans==True:
             print("deleted")
         else:
             print("not found")
    elif choice==3:
        nm=input("enetr name")
        f=searchbyname(nm)
        if f!=None:
            print(f)
        else:
            print("not found")
    elif choice==4:
        mob=input("Enter the mobile no")
        f=searchbymobile(mob)
        if f!=None:
             print(f)
        else:
            print("mob not found")
    elif choice==5:
        nm=input("enter the name")
        nmob=input("enetr new mobile")
        f=modifymobile(nm,nmob)
        if f!=None:
            print(f)
            print("modification done")
        else:
            print("not found")
    elif choice==6:
        display_all()
    elif choice==7:
       sys.exit(0)
