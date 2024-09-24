def factorial(nombre):
    f=1
    char=""
    for i in range(1,nombre+1):
        f=f*i
        char=char+str(i)+"*"
    return f,char
print(factorial(4))