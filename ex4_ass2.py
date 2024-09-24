def evenNumber(liste):
    new_List=[]
    for i in liste:
        if i%2==0:
            new_List.append(i)
    return new_List
print(evenNumber( [1,2,3,4,5,6] ))