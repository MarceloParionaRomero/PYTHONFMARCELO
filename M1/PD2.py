from math import sqrt

a= int(input('Ingrese un valor <> de 0: '))
b= int(input('Ingrese el valor de b: '))
c= int(input('Ingrese el valor de c: '))
if a != 0:
    d= (b**2 - 4*a*c)
    
    if d<0: 
        print('Ecuación no presenta solución real')
    else: 
        x1= (-b+ sqrt(d))/(2*a)
        x2= (-b- sqrt(d))/(2*a)
        print(f'Las raíces son {x1} y {x2}')
    
else:     
    print('El valor de a debe ser distinto a cero')
    