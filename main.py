# -*- coding: utf-8 -*-
import csv
from getpass import getpass

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
            codigo = producto[0]
            descripcion = producto[1][0]
            precio = producto[1][1]
            iva = producto[1][2]
            escritor_de_datos.writerow((codigo, descripcion,precio,iva))#La primer columna es la llave de mi diccionario y el resto es mi lista [descripción, precio, IVA]


def cargar_datos():
    productos = dict()
    with open('base_de_datos.csv', 'rt', encoding='utf-8') as archivo_base_de_datos: #Abro el archivo en modalidad lectura con caracteres UNICODE
        lector_de_datos = csv.reader(archivo_base_de_datos) #Construyo un objeto para leer datos sobre el archivo
        for idx, row in enumerate(lector_de_datos): #Recorro todos datos
            #if idx == 0:
            #    continue
            if row == []:
                continue
            
            codigo = row[0]
            descripcion = row[1]
            precio = int(row[2])
            iva = float(row[3])
            productos[codigo] = [descripcion, precio, iva] #La primer columna es la llave de mi diccionario y el resto es mi lista [descripción, precio, IVA]
    return productos

#endregion

#region Impresiones de datos
def imprimir_todo(lista_productos): #Función para imprimir los datos bonitos
    print('{:^10} {:^30} {:^10} {:^5}'.format('Código', 'Descrición', 'Precio', 'IVA'))
    for producto in lista_productos.items():
        codigo = producto[0]
        descripcion = producto[1][0]
        precio = producto[1][1]
        iva = int(100*float(producto[1][2]))
        print('{:^10} {:^30} {:^10} {:^5}%'.format(codigo, descripcion, precio, iva))


def imprimir_producto(codigo):
    descripcion = productos[codigo][0]
    precio = productos[codigo][1]
    iva = int(100*float(productos[codigo][2])) #el número lo convertimos 
    print('{:^10} {:^30} {:^10} {:^5}'.format('Código', 'Descrición', 'Precio', 'IVA'))
    print('{:^10} {:^30} {:^10} {:^5}%'.format(codigo, descripcion, precio, iva))
    
#endregion

def pedir_numero(mensaje):
    mensaje += '\n'
    while True:
        try:
            print(mensaje)
            numero = int(input())
            return numero
        except ValueError:
            print('Debe ingresar un número entero')


def pedir_porcentaje(mensaje):
        mensaje += '\n'
        while True:
            try:
                print(mensaje)
                numero = float(input())
                if numero > 1:
                    return round(numero/100,2)
                if numero < 1:
                    return round(numero,2)

            except ValueError:
                print('Debe ingresar un número entero')

def validar_ingreso(usuario, contraseña):
    cuentas = [{
        'usuario': 'user1',
        'contraseña': 'password1',
        'permiso': 'administrar'
    }, {
        'usuario': 'user2',
        'contraseña': 'password2',
        'permiso': 'facturar'
    }]
    for cuenta in cuentas:
        if cuenta['usuario'] == usuario and cuenta['contraseña'] == contraseña:
            return cuenta['permiso']
    return 'ingreso no valido'

if __name__ == "__main__":
    productos = cargar_datos()
    opcion_menu = 'no assigned'

    opcion_menu = 'menu'
    while opcion_menu != 'exit':
        
        if opcion_menu == 'menu':
            usuario = input("Puede ingresar 'salir' para terminar la sesión\nIngrese el nombre de usuario\n")
            contraseña = getpass()
            opcion_menu = validar_ingreso(usuario, contraseña)

        elif opcion_menu == 'administrar':
            print('Menu administracion')

        elif opcion_menu == 'facturar':
            print('Menu facturacion')
        
        elif opcion_menu == 'ingreso no valido':
            print('Usuario y/o contraseña incorrectos')
            opcion_menu = 'menu'

        else:
            opcion_menu = 'exit'

    guardar_datos(productos)



