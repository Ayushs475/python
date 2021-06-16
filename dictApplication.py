
'''Write a program to display following menu and do the following:
1. Add new city and trees commonly found in the city.
2. Display all cities and the list of trees for all cities.
3. Display list of trees of a particular city.
---- Accept a city from user search city and if found display list of trees otherwise
---- Display message not found
4. Display cities which have the given tree.
---- Accept a tree name from user and display all cities in which the tree is found.
5. Delete city
---- Accept city from user and delete the city if found.
---- Prompt user before deletion
6. Modify tree list
---- Accept city and trees to be added in the city. if city exist add trees at the end
of the list
---- Otherwise add city and list
7. Exit'''

dict={}
print("Welcome to Green city ")
while True:
    print("Enter choice \n1. Add new city and trees commonly found in the city \n2. Display all cities and the list of trees for all cities.\n3. Display list of trees of a particular city.\n4. Display cities which have the given tree.\n5. Delete city\n6. Modify tree list\n7. Exit")
    choice=input("Enter choice")
    if choice==1:
        print("Please enter the city name ")
        city=input()
        print("Please enter the name of trees to be searched in the city ")
        tree=input().split()
        dict[city]=tree
    if choice==2:
       print("Displaying all the trees found in all the cities")  
       for city in dict.keys():
           print("City name",city) 
           for tree in dict[city]:
               print(tree,end=" ")
    if choice==3:
        city=input("Enter the city to be searched")
        if( city not in dict.keys()):
            print("City not found ")
        else:
            for tree in dict[city]:
                print(tree,end=",")
                print()
    if choice==4:
        print("Enter all trees name for displaying all cities ")
        tree=input().split()
        for city in dict.keys():
            print("tree in city",city)
        if tree in dict.keys[city]:
            print(city,end=",")
    if choice==5:
        print("Enter the city to be searched /deleted")
        city=input()
        if(city in dict.keys()):
            print("Do you want to delete the city ? Y/N")
            if choice == 'Y':
                del dict[city]
            else:
                print("Enter the wrong choice")
        else:
            print("City not found")
    if choice==6:
        print("Enter the city to be added")
        city=input()
        print("Enter the tree in a list ,separated by space")
        if(city in dict.keys()):
            dict[city].extends(tree)
        else:
            dict[city]=tree
    if choice==7:
        print("wrong choice")
        break

    
