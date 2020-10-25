# -*- coding: utf-8 -*-
import csv

#productos = {
#    '001': ['descripción', 'precio', 'IVA']
#}

#region CRUD functions
def crear_producto(codigo, descripcion, precio, iva): #Create
    if codigo in productos:
        print('El código {} proporcionado ya fue usado'.format(codigo))
    else:
        productos[codigo] = [descripcion, precio, iva]


def consultar_producto(codigo): #Read
    if codigo in productos:
        imprimir_producto(codigo)
    else:
        print('El producto con codigo {} no se encuentra registrado en la base de datos'.format(codigo))


def modificar_producto(codigo, descripcion, precio, iva): #Update
    if codigo in productos:
        productos[codigo] = [descripcion, precio, iva]
    else:
        print('El código {} no existe en nuestra base de datos'.format(codigo))


def borrar_producto(codigo): #Delete
    if codigo in productos:    
        del productos[codigo]
        print('El elemento con codigo {} ha sido eliminado'.format(codigo))
    else:
        print('Ese producto no se encuentra en la base de datos')

#endregion

#region gestión de datos
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

#endregion

#region Impresiones de datos
def imprimir_todo(diccionario_llave_lista): #Función para imprimir los datos bonitos
    for lista_datos in diccionario_llave_lista.items():
        print('{:^10} {:^30} {:^10} {:^10}'.format(lista_datos[0],lista_datos[1][0],lista_datos[1][1],lista_datos[1][2]))


def imprimir_producto(codigo):
    print('{:^10} {:^30} {:^10} {:^10}'.format(codigo, productos[codigo][0],productos[codigo][1],productos[codigo][2]))
    
#endregion

if __name__ == "__main__":
    productos = cargar_datos()
    imprimir_todo(productos)



