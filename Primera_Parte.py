# Universidad del Valle de Guatemala
# Base de Datos
#   Marcos Gutierrez
#   17909

# Documentacion utilizada para el manejo de la base de datos: http://initd.org/psycopg/docs/module.html#psycopg2.connect

import psycopg2

#Creamos el procedimiento alamcenado
'''
CREATE OR REPLACE PROCEDURE insert(INT, FLOAT, FLOAT, FLOAT, FLOAT)
LANGUAGE plpgsql
AS $$
DECLARE
    F_MODEL BOOL: FALSE;
    N_MODEL INT: $1;
BEGIN
    LOOP
        SELECT INTO F_MODEL EXISTS(
            SELECT MODEL FROM PC
            WHERE MODEL = N_MODEL
        );
        EXIT WHEN F_MODEL = FALSE;
        N_MODEL += 1;
    END LOOP;

    INSERT INTO PC VALUES(N_MODEL, $2, $3, $4, $5);
    INSERT INTO PRODUCT VALUES('UNKNOW', N_MODEL, 'PC');
END;
$$;
'''
# Ejercicio A
# Funcion que recibe como parametro precio, y devuelve las caracteristicas del precio indicado.
def consulta_A(price):
    #Precio debe ser mayor a 0
    if (price >= 0):
        #Realizamos la conexion a la base de Datos
        try:
            conn = psycopg2.connect("dbname=Lab12 user=postgres password=Superturbo2807")
            cursor = conn.cursor()
            # Realizamos el Query
            # execute(query, vars=None)
            cursor.execute(
                '''
                SELECT PC.MODEL, PC.SPEED, PC.RAM, PC.HD, PC.PRICE FROM PC
                ORDER BY (ABS(%s - PC.PRICE))
                ''',
                (price,)
            )
            # Guardamos el resultado
            print('Datos: ')
            #result = cursor.fetchall()
            result = cursor.fetchmany(1)
            # Ciclo para recorrer los resultados
            for i in result:
                print(i)
            conn.commit()
        # Terminamos con la conexion de la base de datos
        finally:
            cursor.close()
            conn.close()
            print('')
            print('CONEXION ACABADA')
    else:
        print('Ingrese un numero que sea mayor a 0')

# Ejercicio B
# Ejercicio que recibe como parametro (speed, ram, hd) y devuelve los datos relacionados con los parametro
def consulta_B(speed, ram, hd):
    # Evitamos los numeros menos a 0 en los parametros
    if (speed>0) and (ram>0) and (hd>0):
        # Realizamos la conexion a la base de Datos
        try:
            conn = psycopg2.connect("dbname=Lab12 user=postgres password=Superturbo2807")
            cursor = conn.cursor()
            # Realizamos el Query
            cursor.execute(
                '''
                SELECT Product.model, ram, speed, hd, Laptop.price, Product.maker FROM Laptop
                JOIN Product ON Product.model = Laptop.model
				WHERE ram >= %s AND speed >= %s AND hd >= %s
                ''',
                (speed, ram, hd,)
            )
            # Guardamos el resultado
            result = cursor.fetchall()
            print('Resultados: ')
            # Recorremos los resultado
            for i in result:
                print(i)
            conn.commit()
        finally:
            cursor.close()
            conn.close()
            print('')
            print('CONEXION ACABADA')
    else:
        print('Ingrese numeros mayor a 0')

#Ejercicio c
def consulta_C(budget, speed):
    #Evitamos los numeros negatios
    if(budget>0) and (speed>0):
        #Realizamos la CONEXION
        try:
            conn = psycopg2.connect("dbname=Lab12 user=postgres password=Superturbo2807")
            cursor = conn.cursor()
            #query
            cursor.execute(
                '''
                SELECT PC.MODEL, PC.SPEED, PRINTER.MODEL, PRINTER.TYPE, PRINTER.COLOR, (PC.PRICE + PRINTER.PRICE) AS TOTAL_PRECI
				FROM PC, PRINTER
				WHERE (PC.PRICE + PRINTER.PRICE) <= %s;
                ''',
                (budget,)
            )
            result = cursor.fetchall()
            for i in result:
                print(i)
            conn.commit()
        finally:
            cursor.close()
            conn.close()
            print('')
            print('CONEXION ACABADA')
    else:
        print('Revise lo ingresado')

#Ejercicio D
def consulta_D(model, speed, ram, hd, price):
    #Evitamos que el usuario ingrese numeros menos a 0
    try:
        conn = psycopg2.connect("dbname=Lab12 user=postgres password=Superturbo2807")
        cursor = conn.cursor()
        #query
        cursor.execute(
            '''
            CALL insert(%s, %s, %s, %s, %s);
            ''',
            (model, speed, ram, hd, price)
        )
        result = cursor.fetchall()
        print('Se ha ingresado una nueva PC')
        for resultados in result:
            print(resultados)
        conn.commit()
    finally:
        cursor.close()
        conn.close()
        print('')
        print('CONEXION ACABADA')
