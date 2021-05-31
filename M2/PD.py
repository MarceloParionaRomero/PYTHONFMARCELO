#1
def lista_alumnos(num_alumnos):
    alumnos=[]
    for n in range(num_alumnos):
        alumno = {}
        
        alumno['Nombre'] = input('Ingrese el nombre completo.. ')
        alumno['Nota1'] = float(input('Ingrese nota 1 '))
        alumno['Nota2'] = float(input('Ingrese nota 2 '))
        alumno['Nota3'] = float(input('Ingrese nota 3 '))
        
        alumnos.append(alumno)
    return alumnos

num_alumnos = int(input('Introduce la cantidad de alumnos: '))
list_alumnos = lista_alumnos(num_alumnos)    
print(list_alumnos)

#2
def aprobados(alumnos:list):
   c=0 
   a=0 
   for n in range(len(alumnos)):
         prom=(alumnos[n]["Nota1"]+alumnos[n]["Nota2"]+alumnos[n]["Nota3"])/3
         if prom>=4:
             a+=1
   print(f"El numero de aprobados es {a} \nEl numero de desaprobados es {len(alumnos)-a}")   

aprobados(list_alumnos)   
 #3
def promedio(alumnos:list):

   sum=0
   for n in range(len(alumnos)):
         sum=sum+(alumnos[n]["Nota1"]+alumnos[n]["Nota2"]+alumnos[n]["Nota3"])
   print(f"El promedio del salon es {sum/(len(alumnos)*3)}")

promedio(list_alumnos)          

#4
def aprobados(alumnos:list):
   max=0
   min=0
   for n in range(len(alumnos)):
         prom=(alumnos[n]["Nota1"]+alumnos[n]["Nota2"]+alumnos[n]["Nota3"])/3
         if n==0:
             min=prom
             max=prom
             i=n
             j=n 
         else:

           if prom>=max:
             max=prom
             i=n
           elif prom<=min:
             min=prom
             j=n
   print("El mayor promedio lo tuvo "+alumnos[i]["Nombre"]+f" con {round(max,2)}" )
   print("El menor promedio lo tuvo "+alumnos[j]["Nombre"]+f" con {round(min,2)}" )

aprobados(list_alumnos)

#5
def busca(alumnos:list,cad:str):
  print("Alumnos encontrados \n\n")
  for i in range(len(alumnos)):
     if alumnos[i]["Nombre"][0:len(cad)]==cad:
       print(alumnos[i]["Nombre"]+" Notas "+  str(alumnos[i]["Nota1"])+"," +str(alumnos[i]["Nota2"])+","+str(alumnos[i]["Nota3"]))

busca(list_alumnos,"ma")