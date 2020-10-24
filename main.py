# -*- coding: utf-8 -*-
import csv
from base_datos import productos

def crear_producto(codigo, descripcion, precio, iva): #Create
    productos[codigo] = [descripcion, precio, iva]


def consultar_producto(codigo): #Read
    pass


def modificar_producto(codigo): #Update
    pass


def borrar_producto(codigo): #Delete
    pass


def guardar_datos(productos):
    with open('base_de_datos.csv', 'w', newline='', encoding='utf-8') as archivo_base_de_datos: #Abro el archivo en modalidad escritura con caracteres UNICODE
        escritor_de_datos = csv.writer(archivo_base_de_datos) #Construyo un objeto para leer datos sobre el arc
        
        for producto in productos.items(): #Recorro mi diccionario para escribir
            escritor_de_datos.writerow((producto[0], producto[1][0],producto[1][1],producto[1][2]))#La primer columna es la llave de mi diccionario y el resto es mi lista [descripción, precio, IVA]


def cargar_datos():
    productos = dict()
    with open('base_de_datos.csv', 'rt', encoding='utf-8') as archivo_base_de_datos: #Abro el archivo en modalidad lectura con caracteres UNICODE
        lector_de_datos = csv.reader(archivo_base_de_datos) #Construyo un objeto para leer datos sobre el archivo
        for idx, row in enumerate(lector_de_datos): #Recorro todos datos
            if idx == 0:
                continue
            if row == []:
                continue
            productos[row[0]] = row[1:4] #La primer columna es la llave de mi diccionario y el resto es mi lista [descripción, precio, IVA]
    return productos
        
def imprimir_datos(diccionario_llave_lista): #Función para imprimir los datos bonitos
    for lista_datos in diccionario_llave_lista.items():
        print('{:^10} {:^30} {:^10} {:^10}'.format(lista_datos[0],lista_datos[1][0],lista_datos[1][1],lista_datos[1][2]))


if __name__ == "__main__":
    guardar_datos(productos)
    productos = cargar_datos()
    imprimir_datos(productos)

