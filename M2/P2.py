a="ABCDEFGHIJKLMNOPQRSTUWVXYZ"
ext=a+a
b=input("Ingrese texto plano.. ")
k=int(input("Ingrese valor de rotación: "))
r=k%26
c=b.upper()
cad=""
for i in range(0,len(b)):
    if c[i].isalpha():
     if r<=25-a.index(c[i]):
         if b[i].isupper():     
           cad=cad+a[a.index(c[i])+k]
         else:
          cad=cad+a[a.index(c[i])+k].lower() 
     else:
         if b[i].isupper():     
          cad=cad+ext[ext.index(c[i])+k]
         else:
          cad=cad+ext[ext.index(c[i])+k].lower()    
    else:
       cad=cad+c[i]
print("Texto cifrado " +cad+"\nTexto original "+b)

