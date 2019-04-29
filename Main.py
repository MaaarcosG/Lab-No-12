# Universidad del Valle de Guatemala
# Base de Datos
#   Marcos Gutierrez
#   17909

import Primera_Parte
#Le damos una variable a la Primera_Parte
data = Primera_Parte

def main():
        print(
        '''
        *-----Bienvenido al sistema de control de base de datos-----*
        1. Consultar el una computador por medio del precio
        2. Buscar una Laptop
        3. Consulta de PC + Printer
        4. Insetar una computadora nueva
        5. Cantidad de PC vendidas por un precio
        6. Salir
        ''')

#contador
opcion = 1
while (opcion != 6):
    main()
    opcion = input('¿Que desea hacer? \n')
    #Condicion solo para aceptar numero de opcion
    try:
        opcion = int(opcion)
        #Opcion No. 1
        if(opcion == 1):
            price = input('Ingrese el precio que desea consultar: ')
            try:
                price = int(price)
                data.consulta_A(price)
            #Mensaje de error
            except ValueError:
                print('Ingrese un numero entero')
        #Opcion No. 2
        elif(opcion == 2):
            speed = input('Ingrese la velocidad: ')
            ram = input('Ingrese la RAM: ')
            hd = input('Ingrese HD: ')
            #Verificar que sean numeros
            try:
                speed = int(speed)
                ram = int(ram)
                hd = int(hd)
                data.consulta_B(speed, ram, hd)
            except ValueError:
                print('Ingrese unicamente numeros')
        #Opcion No. 3
        elif(opcion == 3):
            budget = input('Ingrese el presupuesto maximo: ')
            speed = input('Velocidad minima: ')
            try:
                budget = int(budget)
                speed = int(speed)
                data.consulta_C(budget, speed)
            except ValueError:
                print('Cuidado con lo que ingresa')
        elif(opcion == 4):
            model = input('Modelo: ')
            speed = input('Velocidad: ')
            ram = input('RAM: ')
            hd = input('hd: ')
            price = input('Price: ')
            try:
                model = int(model)
                speed = int(speed)
                ram = int(ram)
                hd = int(hd)
                price = int(price)
                data.consulta_D(model, speed, ram, hd, price)
            except ValueError:
                print('Ingrese solo numeros enteros')
    #Mensaje de error
    except ValueError:
        print('Ingrese solo un numero de 1-6')
