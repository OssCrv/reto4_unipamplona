# -*- coding: utf-8 -*-
import csv
from getpass import getpass


def validar_ingreso(usuario, contraseña):
    cuentas = [{
        'usuario': 'user1',
        'contraseña': 'password1',
        'permiso': 'administrar'
    }, 
    {
        'usuario': 'user2',
        'contraseña': 'password2',
        'permiso': 'facturar'
    }]

    for cuenta in cuentas:
        if cuenta['usuario'] == usuario and cuenta['contraseña'] == contraseña:
            return cuenta['permiso']
    return 'ingreso no valido'


#region CRUD functions
def crear_producto(codigo): #Create
    if codigo in productos:
        print('El código {} proporcionado ya fue usado\n'.format(codigo))
    else:
        descripcion = input('Ingrese la descripción del producto: ')
        precio = pedir_numero('Ingrese el precio del producto: ')
        iva = pedir_porcentaje('Ingrese el IVA: ')
        productos[codigo] = [descripcion, precio, iva]
        imprimir_producto(codigo)
        print('El producto se ha creado satisfactoriamente\n')


def consultar_producto(codigo): #Read
    if codigo in productos:
        imprimir_producto(codigo)
    else:
        print('El producto con codigo {} no se encuentra registrado en la base de datos\n'.format(codigo))


def modificar_producto(codigo): #Update
    if codigo in productos:
        descripcion = input('Ingrese la nueva descripción del producto: ')
        if descripcion == '':
            descripcion = productos[codigo][1]
        precio = pedir_numero('Ingrese el nuevo precio del producto: ')
        if precio == '':
            precio = productos[codigo][2]
        iva = pedir_porcentaje('Ingrese el nuevo IVA: ')    
        if iva == '':
            iva = productos[codigo][3]
        productos[codigo] = [descripcion, precio, iva]
        imprimir_producto(codigo)
        print('El producto se ha modificado satisfactoriamente\n')
    else:
        print('El código {} no existe en nuestra base de datos'.format(codigo))


def borrar_producto(codigo): #Delete
    if codigo in productos:    
        del productos[codigo]
        print('El elemento con codigo {} ha sido eliminado\n'.format(codigo))
    else:
        print('Ese producto no se encuentra en la base de datos\n')


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
    

def imprimir_factura(lista_productos, usuario):
    subtotal = 0
    iva_19 = 0
    iva_10 = 0
    valor_total = 0
    raya = '---------------------------------------------------------------------------------------'
    if lista_productos == []:
        print('\nUsted no ha ingresado productos a la lista\n')
    else:
        print('\n\n'+raya)
        print('|{:<10}|{:<47}|{:<15}|{:<10}|'.format('Cliente', usuario[0], 'No Factura', '001'))
        print(raya)
        print('|{:<10}|{:<25}|{:<10}|{:<5}|{:<15}|{:<15}|'.format('Código', 'Descripción', 'Cantidad', 'IVA', 'Valor unitario', 'Valor total'))
        print('|{:<10}|{:<25}|{:<10}|{:<5}|{:<15}|{:<15}|'.format('', '', '', '(%)', '(pesos)', '(pesos)'))
        print(raya)
        for producto in lista_productos:
            codigo = producto[0]
            descripcion = producto[1]
            precio = producto[2]
            iva_porc = int(100*float(producto[3]))
            cantidad = producto[4]
            print('|{:<10}|{:<25}|{:<10}|{:<5}|{:<15}|{:<15}|'.format(codigo, descripcion, cantidad, iva_porc, precio, precio*cantidad))
            
            iva = producto[3]
            subtotal += precio_sin_iva(precio, iva)*cantidad
            if iva == 0.19:
                iva_19 += calculo_iva(precio, iva)*cantidad
            elif iva == 0.10:
                iva_10 += calculo_iva(precio, iva)*cantidad
            valor_total += precio*cantidad
        print(raya)
        print('|{:53}|{:<15}|{:<15}|'.format('','SUBTOTAL', round(subtotal)))
        print('|{:53}|{:<15}|{:<15}|'.format('','IVA 9%', round(iva_19)))
        print('|{:53}|{:<15}|{:<15}|'.format('','IVA 10%', round(iva_10)))
        print('|{:53}|{:<15}|{:<15}|'.format('','TOTAL', round(valor_total)))
        print(raya+'\n\n')
#endregion

#region calculosIVA
def precio_sin_iva(precio, IVA):
    base = precio/(1+IVA)
    return base

def valor_iva(base, IVA):
    valor_iva = base*IVA
    return valor_iva

def calculo_iva(precio, IVA):
    return valor_iva(precio_sin_iva(precio, IVA), IVA)
#endregion


#region Petición de datos númericos
def pedir_numero(mensaje):
    mensaje += ': '
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print('Debe ingresar un número entero\n')


def pedir_porcentaje(mensaje):
        mensaje += ': '
        while True:
            try:
                numero = float(input(mensaje))
                if numero > 1:
                    return round(numero/100,2)
                if numero < 1:
                    return round(numero,2)

            except ValueError:
                print('Debe ingresar un número entero\n')
#endregion


def menu_admin(opcion_ingresada):
    if opcion_ingresada == '1': #Opción de creación de producto
        codigo = input('Ingrese el código del producto a crear: ')
        crear_producto(codigo)

    elif opcion_ingresada == '2': #Opción de modificación de productos
        imprimir_todo(productos)
        codigo = input('Ingrese el código del producto a modificar: ')
        imprimir_producto(codigo)
        modificar_producto(codigo)
        
    elif opcion_ingresada == '3': #Opción de eliminación de productos
        imprimir_todo(productos)
        codigo = input('Ingrese el código del producto a eliminar: ')

    else: 
        print('Opcion invalida\n Intentalo de nuevo\n')


def menu_factura(opcion_ingresada):
    if opcion_ingresada == '1': #Opción para listar productos
        imprimir_todo(productos)

    elif opcion_ingresada == '2': #Opción de consulta de productos
        codigo = input('Ingrese el código del producto que desea consultar: ')
        imprimir_producto(codigo)
        
    elif opcion_ingresada == '3': #Opción para emitir factura
        menu_emision_factura()

    else:
        print('Opcion invalida\n Intentalo de nuevo\n')


def anniadir_cliente():
    ingreso_consola = '2'
    while ingreso_consola == '2':
        usuario = list()
        nombre = input('Ingrese el nombre del usuario\n')
        cedula = input('Ingrese la cédula del usuario\n')
        usuario.append(nombre)
        usuario.append(cedula)

        print('Usuario: ', nombre, 'con cédula', cedula)
        print(usuario)

        ingreso_consola = input('''¿La información del cliente es correcta?
        [1] - Sí
        [2] - No\n''')
    return usuario


def listar_productos():
    imprimir_todo(productos)
    lista_productos = list()
    ingreso_consola = '1'
    while ingreso_consola != '2':
        if ingreso_consola == '1':
            codigo = input('Ingrese el código del producto: ')
            try:
                lista_transitoria = [codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2]]
                cantidad = int(input('Ingrese la cantidad de productos: '))
                lista_transitoria.append(cantidad)
                lista_productos.append(lista_transitoria)
            except KeyError:
                print('El producto no existe\n')

        else:
            print('Opción no válida\n')

        ingreso_consola = input('''¿Desea añadir un nuevo producto? 
        [1] - Sí
        [2] - No\n''')

            
    return lista_productos


def menu_emision_factura():
    opcion_accion = '1'
    usuario = ['---', '---']

    lista_productos_factura = list()
    while opcion_accion != '5':

        if opcion_accion == '1': #Opción de registro de productos
            lista_transitoria = listar_productos()
            for producto in lista_transitoria:
                lista_productos_factura.append(producto)

        elif opcion_accion == '2': #Opción para previsualizar la factura
            imprimir_factura(lista_productos_factura, usuario)

        elif opcion_accion == '3': #Opción para añadir el cliente a la factura
            usuario= anniadir_cliente()

        elif opcion_accion == '4':#Opción para emitir factura
            pass

        else:
            print('No ha ingresado una accion válida')

        opcion_accion = input('''Se esta generando una nueva factura
        [1] - Registrar productos
        [2] - Previsualizar productos
        [3] - Ingresar Usuario
        [4] - Emitir facturar
        [5] - Cancelar y salir\n''')


if __name__ == "__main__":
    productos = cargar_datos()

    opcion_menu = 'login'
    while opcion_menu != 'exit':
        
        if opcion_menu == 'login':
            usuario = input("\nPuede ingresar 'salir' para terminar la sesión\n\nIngrese el nombre de usuario: ")
            if usuario == 'salir':
                break
            contraseña = getpass()
            opcion_menu = validar_ingreso(usuario, contraseña)

        elif opcion_menu == 'administrar':
            opcion = input('''Usted ha ingresado con permisos de administración
            [1] - Crear producto
            [2] - Modificar producto
            [3] - Eliminar producto
            [4] - Salir\n''')
            if opcion != '4':
                menu_admin(opcion)
            else:
                opcion_menu = 'exit'

        elif opcion_menu == 'facturar':
            opcion = input('''Usted ha ingresado con permisos de facturación
            [1] - Listar productos
            [2] - Consultar producto por código
            [3] - Nueva factura
            [4] - Salir\n''')
            if opcion != '4':
                menu_factura(opcion)
            else:
                opcion_menu = 'exit'
        
        elif opcion_menu == 'ingreso no valido':
            print('Usuario y/o contraseña incorrectos')
            opcion_menu = 'login'

    guardar_datos(productos)
