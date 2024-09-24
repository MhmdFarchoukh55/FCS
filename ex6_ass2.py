def ipv4(string):
    s=string.split(".")
    l=[]
    for i in s:
        if (int(i)>=0 and int(i)<=255):
            l.append(int(i))
    if len(l)==4:
        print(f' {".".join(map(str, l))} est un ipv4')
    else:
        print(f' {".".join(map(str, l))} n est un ipv4')

ipv4("10.0.0.01")