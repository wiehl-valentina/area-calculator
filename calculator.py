
import math

# PANTALLA DE INICIO
print('\n')
print("==================")
print("Area Calculator 📐")
print("==================")
print('\n')

# OPCIONES

print(' 1)Square. \n 2)Rectangle. \n 3)Triangle. \n 4)Circle. \n 5)Quit. \n')

# FUNCIÓN DE IMPRESIÓN
def areaMsg(result):
    print(f'The area is {result}')

# SELECCIÓN DE LA OPCIÓN 

option = int(input('Shape: '))

# ESTRUCTURA DE CONTROL QUE DEFINE COMO PROCEDER

if option == 1:
    side = int(input('Side: '))
    areaMsg(side**2)
elif option == 2:
    base = int(input('Base: '))
    height = int(input('Height: '))
    areaMsg(base*height)
elif option == 3:
    base = int(input('Base: '))
    height = int(input('Height: '))
    areaMsg((height*base)/2)
elif option == 4:
    radius = int(input('Radius: '))
    areaMsg(math.pi*radius**2)
elif option == 5:
    print('Operation canceled.')
else:
    print('Wrong input.')
    
