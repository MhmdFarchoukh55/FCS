#nb=64211
#ct=0
#while nb>1:
#   nb=nb/10
#    ct=ct+1        
#print(ct)


def numero_digits(nb, ct=0):
    if nb<0:
        nb=abs(nb)
    if nb>1:
        nb=nb/10
        return numero_digits(nb,ct=ct+1 )
    else:
        return ct
#print(numero_digits(64088))

#l=[1, 6, -3, 1, 14, 9, 12, 24]
#m=l[0]
#for i in range(1,len(l)):
#    if m<l[i]:
#        m=l[i]
#print(m)

def numero_max(liste1,i=1,max_nb=None):
    if len(liste1)==0:
        return 0
    
    if max_nb is None:
        max_nb=liste1[0]
    
    if i<len(liste1):
        if liste1[i]>max_nb:
            max_nb=liste1[i]
        return numero_max(liste1 , i=i+1 , max_nb=max_nb)
    else:
        return max_nb
#print(numero_max([1, 6, -3, 1, 14, 9, 12, 24]))


def count_tags(html, tag):
    opening_tag = f"<{tag}>"
    closing_tag = f"</{tag}>"
    
    if (opening_tag not in html) or (closing_tag not in html):
        return 0
    open_index = html.find(opening_tag)
    close_index = html.find(closing_tag, open_index) + len(closing_tag)
   
    html2 = html[close_index:]
    return 1 + count_tags(html2, tag)
        
enter_nb=int(input("entrez un nb positive entre 1 et 4"))
while enter_nb!=4:
    
    possible=[1,2,3,4]
    if enter_nb not in possible:
        enter_nb=int(input("entrez un nb positive entre 1 et 4"))
    
    
    if enter_nb==1:
        enter_nb2=int(input("entrez un nb "))
        print(numero_digits(enter_nb2))
        enter_nb=int(input("entrez un nb positive entre 1 et 4"))
        
    elif enter_nb==2:
        nb_liste=int(input("combien d element vous vouler enterz dans votre liste"))
        l=[]
        for i in range(nb_liste):
            entrez_nb3=int(input("entrez un nb  "))
            l.append(entrez_nb3)
        print(numero_max(l))
        enter_nb=int(input("entrez un nb positive entre 1 et 4"))
    
    elif enter_nb==3:
        enter_html_code=str(input("enter un code html"))
        enter_tag=str(input("entrez le tag "))
        print(count_tags(enter_html_code,enter_tag))
        enter_nb=int(input("entrez un nb positive entre 1 et 4"))
    
    elif enter_nb==4:
        print()

        
        