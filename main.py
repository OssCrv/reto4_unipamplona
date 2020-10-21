# -*- coding: utf-8 -*-
import csv
from base_datos import productos

def crear_producto(codigo): #Create
    pass


def consultar_producto(codigo): #Read
    pass


def modificar_producto(codigo): #Update
    pass


def borrar_producto(codigo): #Delete
    pass


import csv
from base_datos import productos

def guardar_datos(productos):
    with open('base_de_datos.csv', 'w', newline='', encoding='utf-8') as archivo_base_de_datos:
        escritor_de_datos = csv.writer(archivo_base_de_datos)
        
        for producto in productos.items():
            escritor_de_datos.writerow((producto [0], producto[1][0],producto[1][1],producto[1][2]))

def cargar_datos():
    productos = dict()
    with open('base_de_datos.csv', 'rt', encoding='utf-8') as archivo_base_de_datos:
        lector_de_datos = csv.reader(archivo_base_de_datos)
        for idx, row in enumerate(lector_de_datos):
            if idx == 0:
                continue
            if row == []:
                continue
            productos[row[0]] = row[1:4]
    return productos
        

if __name__ == "__main__":
    guardar_datos(productos)
    productos = cargar_datos()

