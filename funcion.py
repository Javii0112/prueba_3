import time
import os
import msvcrt

def menu():
    print("""Menú
    1. Grabar
    2. Buscar
    3. Retirarse
    4. Salir """)

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4):
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

import numpy

lista_rut = []
lista_nombre = []
lista_nom_masc = []
lista_cantidad = []
lista_habitacion = []


guarderia = numpy.zeros((2,5), int)


def validar_rut_dueño():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if len(str(rut)) >=7 and len(str(rut)) <= 8:
                return rut
            else:
                print("ERROR! RUT INCORRECTO! DEBE TENER ENTRE 7 Y 8 DIGITOS!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre_dueño():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")
    
def validar_nombre_mascota():
    while True:
        nombre = input("Ingrese nombre de su mascota: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de días: "))
            if cantidad >= 1:
                return cantidad
            else:
                print("ERROR! LA CANTIDAD DE DIAS DEBE SER AL MENOS 1!")
        except:
            print("ERROR! DEBE INGREAR UN NÚMERO ENTERO")

def validar_habitacion():
    while True:
        try:
            habitacion = int(input("Ingrese habitacion (del 1 al 10): "))
            if habitacion >= 1 and habitacion <= 10:
                return habitacion
            else:
                print("ERROR HABITACION INCORRECTA")
        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO!")

def ingresar_mascota():
    os.system('cls')
    while True:
        rut = validar_rut_dueño()
        nombre = validar_nombre_dueño()
        nombre_mascota = validar_nombre_mascota()
        cantidad = validar_cantidad()
        os.system('cls')
        contador = 1
        print("Habitaciones disponibles: \n")
        for x in range(2):
            print(f"Fila {x+1}:", end=' ')
            for y in range(5):
                print(f"Habitacion {contador}", guarderia[x][y], end=' ')
        print( )
        contador += 1 
           
        if guarderia[x][y] == 0:
            habitacion = validar_habitacion()
            lista_habitacion.append(habitacion)
            guarderia[x][y] == 1
        print("presione tecla para continuar....")
        msvcrt.getch()
        continue

def buscar_mascota():
    print("Buscar mascota")
    os.system('cls')
    rut = validar_nombre_dueño()
    lista_rut.append(rut)
    lista_habitacion.append(lista_habitacion)
    if rut in lista_rut:
        print(lista_rut, lista_habitacion )
def retirarse():
    rut = validar_rut_dueño()
    lista_rut.append(rut)
    lista_cantidad.append(validar_cantidad)
    if rut in lista_rut:
        total = lista_cantidad*15000
    print("Su total a pagar es: ",total)
    for x in range(2):
        for y in range(5):
            if guarderia[x][y] == 1:
                guarderia[x][y] == 0
