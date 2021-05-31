a=int(input("Ingrese tarjeta "))
cad=str(a)
l=len(cad)
sum=0
if len(cad)%2==0:
  for i in range(0,len(cad),1):
      x=cad[i] 
      if i%2==0 and i!=1 :
         if len(str(int(x)*2))>1:
            m=int(x)*2
            sum=sum+int(str(m)[0])+int(str(m)[1])  
         else:
            sum=sum+int(x)*2   
      else:       
         sum=sum+int(x)                               
else:
    for i in range(0,len(cad),1):
      x=cad[i] 
      if i%2==0 and i!=1 :
         sum=sum+int(cad[i])  
      else:       
         
         if len(str(int(x)*2))>1:
            m=int(x)*2
            sum=sum+int(str(m)[0])+int(str(m)[1])  
         else:
            sum=sum+int(x)*2                                    
if str(sum)[-1]=="0":
     if (cad[0:2]=="34" or cad[0:2]=="37") and l==15:
         print("AMEX")
     elif l==16 and 51<=int(cad[0:2])<=55:
         print("MASTERCARD")     
     elif cad[0:1]=="4" and 13<=len(cad)<=16:
         print("VISA")
     else:
         print("INVALID")    
else:
  print("INVALID")  


 

#else:
 #american express 15d 34 o 37
 # mastercad 16d 51-55
 # visa  13-16d 4