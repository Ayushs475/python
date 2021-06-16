def addNewVehicle(personName,vehicle):
    v=vehcileDictionary.get(personName,-1)
    if v==-1:
        vehcileDictionary[personName]=vehicle
        return 0
    else:
        ch=input("Dou want to overwrite existing value? (Y/N)")
        if ch.upper()=='Y':
            vehcileDictionary[personName]=vehicle
            return 1
        else:
            return 2

def removePerson(personName):        
    v=vehcileDictionary.get(personName,-1)
    if v==-1:
        return 0
    else:
        ch=input("Dou want to delete existing value? (Y/N)")
        if ch.upper()=='Y':
            v=vehcileDictionary.pop(personName,-1)
            return 1
        else:
            return 2

def modifyVehicle(personName,newVehicle):
    v=vehcileDictionary.get(personName,-1)
    if v==-1:
        return 0
    else:
        ch=input("Dou want to modify existing value? (Y/N)")
        if ch.upper()=='Y':
            vehcileDictionary[personName]=newVehicle
            return 1
        else:
            return 2        

def searchVehicle(personName):
    if personName in vehcileDictionary.keys():
        return vehcileDictionary[personName]
    else:
        return ("Person does not exist")

def searchPerson(vehicle):
    personList=[]
    for key,value in vehcileDictionary.items():
        if vehicle==value:
            personList.append(key)
    return personList

def getPersonList():
    personList= list(vehcileDictionary.keys())
    return personList

def getVehicleList():
    vehicleList= list(vehcileDictionary.values())
    return vehicleList

import sys
choice=0
vehcileDictionary={"JK":"BMW"}
while choice!=8:
    print("1. add new person and vehicle\n2. delete person name and vehicle\n3. Modify vehicle name for the person")
    print("4. Search vehicle for the given person’s name.\n 5.Search list of people, who have given a vehicle\n")
    print("6. Display all person names.\n7.Display all vehicle names.\n 8.exit")
    choice=int(input("enetr choice"))
    if choice==1:
        personName=input("Enter person's name")
        vehicle=input("Enter vehicle's name")
        result= addNewVehicle(personName,vehicle)
        if result==0:
            print("New value is added to dictionary")
        elif result==1:
            print("Already existing value is overwritten")
        elif result==2:
            print("data is not overwritten")
    
    elif choice==2:
        personName=input("Enter person's name to be removed")
        result=removePerson(personName)
        if result==0:
            print("person and vehicle does not exist")
        elif result==1:
            print("person and vehicle is removed")
        else:
            print("Person and vehicle is not removed")

    elif choice==3:
        personName=input("Enter person's name for which vehicle is to be modified")
        newVehicle = input("Enter new vehicle name")
        result=modifyVehicle(personName,newVehicle)
        if result==0:
            print("Person does not exist")
        elif result==1:
            print("Vehicle details are modified")
        else:
            print("Vehicle is not modified")

    elif choice==4:
        personName=input("Enter person's name for which vehicle is to be searched")
        result=searchVehicle(personName)
        print(result)

    elif choice==5:
        vehicle=input("Enter vehicle name for which persons to be searched")
        result=searchPerson(vehicle)
        if(len(result)>0):
            print(result)
        else:
            print("Vehicle does not exist")

    elif choice==6:
        result=getPersonList()
        if(len(result)>0):
            print(result)
        else:
            print("Dictionary is empty")

    elif choice==7:
        result=getVehicleList()
        if(len(result)>0):
            print(result)
        else:
            print("Dictionary is empty")

    elif choice==8:
        sys.exit(0)

    else:
        print("Wrong Choice")
 
