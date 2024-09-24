def find(nombre):
    liste1=[]
    for i in range(1,nombre+1):
        if nombre%i==0:
            liste1.append(i)
    return liste1

print( find(10) )