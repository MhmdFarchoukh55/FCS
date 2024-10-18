#liste1=[1,2,3,5]
#liste2=liste1
#if liste1 is liste2:
 #   print("al")
#else:
 #   print("no")
    
#liste2.append(7)
#print(liste1)
#print(liste2)

m2d= [ [1,2,3] , [4,5,6] , [7,8,9] ]
tup1=(1,2,3,5,6)
tup2=(99,66,55,88,77)
print(tup1)
print(tup2)

#tup1.sort(99) erreur
print(tup1[1])

#tup2[0]=100 errur
#2 methode kermel zid 3al tUple
#b7awela list appenf puit b7awela la tuple

#1ere methode
liste7=list(tup2)
print(liste7)
liste7.sort()
new_tup2=tuple(liste7)
print(new_tup2)

#2eme methode
tup3=tup2+tup1
print(tup3)
#set
set={4,"je",9}
set.add(8)
print(set)
#dict
dic1={ 0 : ["jonnu","ali"], 10:True ,2:"hello" }
print(dic1[10])

for i in dic1:
    print("keys",i)
    print("values",dic1[i])

dic1["12345"]=["bilal",4,"190"]
print(dic1)#add an item to a dictinary

