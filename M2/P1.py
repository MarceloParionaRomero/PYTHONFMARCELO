
j=int(input("Ingrese altura "))

while j==2 or j==9 or  j<1 or j>8:
         j=int(input("Inválido ingrese otra altura "))   

for i in range(1,j+1,1):
       print(" "*(j-i)+"#"*i)

