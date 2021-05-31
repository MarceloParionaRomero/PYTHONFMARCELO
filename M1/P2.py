
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cl=input("Ingrese patrón clave ..")
cypher=""
c3=cl.upper()
if(len(cl)==26 and cl.isalpha()==True and len(cl)==len(set(list(cl.upper()))) ):
     plain=input("Ingrese texto plano ")
     for i in range(0,len(plain),1):
         if plain[i].isupper():
            cypher=cypher+c3[a.index(plain[i])]
         else:
            cypher=cypher+c3[a.index(plain[i].upper())].lower()
     print("cifrado :"+cypher +"\n 0")         
else:
    print("ERROR \n"+" 1")
