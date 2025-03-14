import os
import sys 
import csv
import getpass
import random 
import polars as pl
from random import choice
from datetime import date
from datetime import datetime
from cryptography.fernet import Fernet
from colorama import init,Fore,Back,Style
from time import sleep
import os.path as path
import time
import bcrypt
import base64
import hashlib


init()                         
                            #LISTO #Agregar que se pueda guardar la contrasena temporalmente
                            #PENDIENTE Agrega buscador  de archivos 
                            #ADATA 2.9 correcocion de mejoras pequenas
                            #LISTO Vercion mejorada con polars correccion de errror de encryptacion 
                            #LISTO Agrege colores y auto eliminacion de datos
                            #PENDIENTE Agregacion de syncronizacion de archivos y bases de datos
                            #LISTO Verificacion de archivos desencryptado para modificar o agregar

today = str(date.today())
time_tiempo = 6.2

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

items = list(range(0, 80))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
for i, item in enumerate(items):
        sleep(0.01)
        loadbar(i + 1, l, prefix='Progress:', suffix='Complete', length=l)


def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)


print(' ██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗ ')
print(' ██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗')
print(' ██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║')
print(' ██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║')
print(' ██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝')
print(' ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝ ')




def show():

                clearConsole()
                print("███╗░░░███╗██╗░░░██╗  ██████╗░░█████╗░████████╗░█████╗░██████╗░░█████╗░░██████╗███████╗")
                print("████╗░████║╚██╗░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝")
                print("██╔████╔██║░╚████╔╝░  ██║░░██║███████║░░░██║░░░███████║██████╦╝███████║╚█████╗░█████╗░░")
                print("██║╚██╔╝██║░░╚██╔╝░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║██╔══██╗██╔══██║░╚═══██╗██╔══╝░░")
                print("██║░╚═╝░██║░░░██║░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║██████╦╝██║░░██║██████╔╝███████╗")
                print("╚═╝░░░░░╚═╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝")
                inicio_sesion()
                archivo_estado()


#Problema de logica al hacer un bucle de desincryptacion

password = input("Introduce tu Usuario : ")
secreto = password


def validate():
        
        if not password.isalpha() or len(password) > 6:
            clearConsole()
            time.sleep(1)
            clearConsole()
            print(Fore.RED + "Error: Si introduces un usuario incorrecto no podras desencryptar ." + Fore.RESET)
            time.sleep(3)
            return None
                    
        elif password =="exit" or password == "salir":
            print("saliendo....")
            estado_salida()
            sys.exit(0)
                    #error=="Generado"
            

            

def inicio_sesion():
        let = open('date.txt', 'r')
        ver=let.read()
        print('Ultima modificacion  : '+ Fore.GREEN + ver +Style.RESET_ALL)
        tem = open('temp.txt','r')
        ver=tem.read()
        print('Contrasena temporal  : '+ Fore.BLUE + Style.BRIGHT+ver+Style.RESET_ALL)


def archivo_estado():
        abrir = open('estado.txt', 'r')
        a = abrir.read()
        if a == 'encrypted':
            print("Estado del archivo: "+Fore.GREEN + a + Fore.RESET )
        elif a == 'decrypted':
             print("Estado del archivo: "+Fore.RED + a + Fore.RESET )

def actualizacion_sesion():

    today = str(date.today())
    hora_actual = str(datetime.now())

    archivo_estado = open("date.txt", "w")
    archivo_estado.write(hora_actual)
    archivo_estado.close()


#Generador de passwords 
def Generate_pas():

    longitud = input("De cuantos digitos? :")
    longitud = int(longitud)
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    p = ""
    p = p.join([choice(valores) for i in range(longitud)])
    print("Contrasena generada!:")
    print(Fore.BLUE + Style.BRIGHT+p+Style.RESET_ALL)
    lee = open('temp.txt','w')
    lee.write(p)
    lee.close()


def Eliminacion():
    os.remove("Inventario.csv")
    print(Fore.RED+"Archivo eliminado"+Fore.RESET)
    validate()
#encryptacion automatica al cerrar el programa

def estado_key():
    #Convercion al leer el estado solo validacion, no agrega o modifica el estado
    le = open('estado.txt')
    estado=le.read()
    if estado =="encrypted":
        print("archivo ya esta encryptado!!! ")
        #validate()
    elif estado== "decrypted":
        encrypted_with_key()
        return
    else: 
        print("Error en algo") 

    #generar un archivo extra donde diga si el archivo esta encryptado si lo esta no no encryptara dos veces
def estado():
    #Convercion al leer el estado solo validacion, no agrega o modifica el estado
    le = open('estado.txt',"r",)
    estado=le.read()
    if estado =="encrypted":
        print("archivo ya esta encryptado!!! ")
        #validate()
    elif estado== "decrypted":
        encrypted()
        return
    else: 
        print("Error en algo") 

def estado_salida():
    les = open('estado.txt')
    estado_salir=les.read()
    if estado_salir== "decrypted":
        encrypted()
        return


def estado_dos():
    #Verificacion de desencryptacion
    leer = open('estado.txt','r')
    estado=leer.read()
    if estado =="decrypted":
        print(Fore.RED+"No se puede desencryptar el archivo, el archivo ya se encuentra desencrytado"+Fore.RESET)
        return
    elif estado== "encrypted":
        decrypted()
    else: 
        print("Error en algo") 


def actualizacion_estado():
    archivo_estado = open("estado.txt", "w")
    archivo_estado.write("encrypted")
    archivo_estado.close()

def actualizacion_estado_dos():
    archivo_estado = open("estado.txt", "w")
    archivo_estado.write("decrypted")
    archivo_estado.close()

def genera_clave():
                    print("Desea generar una nueva contraseña y usuario: ")
                    save=input("Y/N :")
                    if save== 'Y' or save== 'y':
                        secreto = input('Tu usuario de maximo 6 letras: ')  # Puede ser cualquier identificador único
                        identificador = input('Clave de maximo 6 numeros: ') 
                         # Usa el nombre de usuario del sistema
# Validar usuario (solo letras y máximo 6 caracteres)
                        if not secreto.isalpha() or len(secreto) > 6:
                            print(Fore.RED + "Error: Debes ingresar un máximo de 6 letras." + Fore.RESET)
                            return
                        if not identificador.isdigit() or len(identificador) > 6:
                            print(Fore.RED + "Error: Debes ingresar un máximo de 6 dígitos." + Fore.RESET)
                            return
                        clave_base = secreto + identificador  
    # Crear un hash SHA256 de la clave base
                        clave_hash = hashlib.sha256(clave_base.encode()).digest()
                        clave_final = base64.urlsafe_b64encode(clave_hash[:32])
                        print(Fore.RED+"La nueva clave de encryptacion es \n"+Fore.RESET)
                        print("Clave generada:", clave_final.decode())
                        time.sleep(4)
                        clearConsole()
                        print("El usuario y clave se guardaran en : clave.txt")
                        time.sleep(2)
                        clearConsole()
                        with open('clave.txt', 'wb') as archivo:
                            archivo.write(f"Usuario: {secreto}:password:{identificador}\n".encode())  # Separar usuario y clave   
                            archivo.close()                    
                        print(Fore.BLUE+"La clave se a guardado con exito"+Fore.RESET)
                        time.sleep(2)
                        print("Desea encryptar el archivo ahora con las nuevas claves:")
                        da = input("Y/N :")
                        if da == "Y" or da == "y":
                            le = open('estado.txt',"r",)
                            estado=le.read()

                            if estado =="encrypted":
                                print("Primero desencrypte el archivo!!! ")
                                return
                            #validate()
                            elif estado== "decrypted":
                                archivo =open('Inventario.csv','rb')
                                datos = archivo.read()
                                f = Fernet(clave_final)
                                datos_cifrados = f.encrypt(datos)
                                encrypted_file= open('Inventario.csv', 'wb') 
                                encrypted_file.write(datos_cifrados)
                                print(Fore.RED+"El archivo se encrypto con exito"+Fore.RESET)
                                actualizacion_estado()
                        else:
                            print("SALIENDO...")
                            time.sleep(1)
                            return

                    else:
                        print("SALIENDO...")

        #Elecion si quiero que se desencrypte con llave interna o externa

# def encrypted_with_key():
#     identificador = input('Usurio maximo 4 letras o num :')  # Usa el nombre de usuario del sistema
#     clave_base = secreto + identificador  
#     # Crear un hash SHA256 de la clave base
#     clave_hash = hashlib.sha256(clave_base.encode()).digest()
#     # Tomar los primeros 32 bytes y codificarlos en base64 para Fernet
#     clave_final = base64.urlsafe_b64encode(clave_hash[:32])
#     # Mostrar la clave generada
#     print("Clave generada:", clave_final.decode())
#     archivo =open('Inventario.csv','rb')
#     datos = archivo.read()
#     f = Fernet(clave_final)
#     datos_cifrados = f.encrypt(datos)
#     encrypted_file= open('Inventario.csv', 'wb') 
#     encrypted_file.write(datos_cifrados)
#     print(Fore.RED+"El archivo se encrypto con exito"+Fore.RESET)
#     actualizacion_estado()


def encrypted():
    
        identificador = input(Fore.BLUE + "Crea clave numérica de máximo 6 dígitos: " + Fore.RESET)

        if not identificador.isdigit() or len(identificador) > 6:
            print(Fore.RED + "Error: La clave debe contener solo números y un máximo de 6 dígitos." + Fore.RESET)
            return

        clave_base = secreto + identificador  

    # Crear un hash SHA256 de la clave base
        clave_hash = hashlib.sha256(clave_base.encode()).digest()

    # Tomar los primeros 32 bytes y codificarlos en base64 para Fernet
        clave_final = base64.urlsafe_b64encode(clave_hash[:32])

    # Mostrar la clave generada
        print("Clave generada:", clave_final.decode())

        archivo =open('Inventario.csv','rb')
        datos = archivo.read()
   
        fernet = Fernet(clave_final)     
        file=open('Inventario.csv', 'rb') 
        original = file.read() 

        encrypted = fernet.encrypt(original) 

        file=open('Inventario.csv', 'rb') 
        original = file.read()


        encrypted_file= open('Inventario.csv', 'wb') 
        encrypted_file.write(encrypted)

        actualizacion_estado()
        # print(Fore.RED+"archivo encryptado "+Fore.RESET)
        print(Fore.BLUE + Style.BRIGHT+"Archivo encryptado con exito!"+Style.RESET_ALL)


        # identificador = input("Ingresa tu consetrasena para desencriptar: ")
        if secreto is None :
            print(Fore.RED + "No se ingresó una clave válida." + Fore.RESET)
            return

        
#desencrptacion automatica al introducior la contraseña correcta


    #return
def decrypted():
        key = secreto
        identificador = input(Fore.GREEN + 'Ingresa los dígitos numéricos para desencriptar: ' + Fore.RESET)

        if not identificador.isdigit() or len(identificador) > 6:
            print(Fore.RED + "Error: Debes ingresar máximo 6 dígitos numéricos." + Fore.RESET)
            return
    
        clave_base = key + identificador  

        clave_hash = hashlib.sha256(clave_base.encode()).digest()
        clave_final = base64.urlsafe_b64encode(clave_hash[:32])
        try:
        # Leer archivo y desencriptar
            with open('Inventario.csv', 'rb') as archivo:
                datos_cifrados = archivo.read()
        
                f = Fernet(clave_final)
                datos_descifrados = f.decrypt(datos_cifrados)

            with open('Inventario.csv', 'wb') as archivo:
                 archivo.write(datos_descifrados)

            actualizacion_estado_dos()
            time.sleep(0.5)
            print(Fore.GREEN + "El archivo se desencriptó con éxito" + Fore.RESET)
            return identificador  # Retorna el identificador si es necesario
    
        except Exception as e:
            print("┌─┐┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐   ┬┌┐┌┌─┐┌─┐┬─┐┬─┐┌─┐┌─┐┌┬┐")  
            print("├─┘├─┤└─┐└─┐││││ │├┬┘ ││   │││││  │ │├┬┘├┬┘├┤ │   │ ")  
            print("┴  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘   ┴┘└┘└─┘└─┘┴└─┴└─└─┘└─┘ ┴ ")
            time.sleep(1)
            print(Fore.RED + "Error: No se pudo desencriptar el archivo. ¿Ingresaste los números correctos?" + Fore.RESET)

  # Obtener el identificador desde decrypted

    # Crear un hash SHA256 y codificarlo para Fernet

 


# def decrypted_key():

  
    
#     identificador = input('Crea Usuario :  ')

#     if not identificador.isdigit() or len(identificador) != 6:
#         print(Fore.RED + "Error: Debes ingresar maximo 6 dígitos." + Fore.RESET)
#         return

#     clave_base = secreto + identificador  

#     # Crear un hash SHA256 y codificarlo para Fernet
#     clave_hash = hashlib.sha256(clave_base.encode()).digest()
#     clave_final = base64.urlsafe_b64encode(clave_hash[:32])

#     try:
#         # Leer archivo y desencriptar
#         with open('Inventario.csv', 'rb') as archivo:
#             datos_cifrados = archivo.read()
        
#         f = Fernet(clave_final)
#         datos_descifrados = f.decrypt(datos_cifrados)

#         with open('Inventario.csv', 'wb') as archivo:
#             archivo.write(datos_descifrados)

#         print(Fore.GREEN + "El archivo se desencriptó con éxito" + Fore.RESET)
    
#     except Exception as e:
#         print(Fore.RED + "Error: No se pudo desencriptar el archivo. ¿Ingresaste los números correctos?" + Fore.RESET)


def menu():

    #print("******MENU INVENTARIO******")
    print("1--- Ver   ","                   2--- Agregar " )
    print("3--- Modificar ","               4--- Buscar")
    print("5--- Encryptar      ","          6--- Desencryptar")
    print("7--- Generar password","         8--- Genera nuevas claves")
    print(Fore.RED+"eliminartodo"+Fore.RESET)



    option=input("Introduzca el número de la opción deseada: ")
    return option


    
def Existename(service):
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            if(service==row['service']):
                return row
        return "No existe name"



def VerInventario():
    df_csv = pl.read_csv("Inventario.csv")
    print(df_csv)

        


def ProductoNuevo():
    try:
        with open('estado.txt', 'r') as ver:
            var = ver.read().strip()  # Eliminar espacios en blanco

        if var == 'encrypted':
            print(Fore.RED + "Primero debe desencriptar el archivo!!" + Fore.RESET)
            return

        from random import randint
        codigo = ''.join(str(randint(0, 9)) for _ in range(4))  # Código de 4 dígitos aleatorios
        
        if ExisteCodigo(codigo) != "No existe":
            print(Fore.RED + "Error: el código ya existe." + Fore.RESET)
            return

        ubicacion = input('Servicio: ').strip()
        descripcion = input('Email: ').strip()
        unidad = input('Password: ').strip()
        tipo = input('Usuario: ').strip()
        familia = input('Referencia: ').strip()
        fecha = str(date.today())

        # Verificar que todos los campos tengan datos
        if not all([ubicacion, descripcion, unidad, tipo, familia]):
            print(Fore.RED + "Error: No puedes dejar campos vacíos." + Fore.RESET)
            return

        with open('Inventario.csv', 'a') as file:
            file.write(f'\n{codigo},{ubicacion},{descripcion},{unidad},{tipo},{familia},{fecha}')
        
        print(Fore.GREEN + "Se agregó correctamente." + Fore.RESET)

    except FileNotFoundError:
        print(Fore.RED + "Error: No se encontró 'estado.txt'." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Error inesperado: {e}" + Fore.RESET)

def ModificarProducto():
    ver= open('estado.txt','r')
    var=ver.read()

    if var == 'encrypted':
        print(Fore.RED+"Primero debe desencriptar el archivo!!"+Fore.RESET)
    else:
        
        service=input('Ingrese servicio a modificar: ')
        #if ExisteCodigo(codigo)=="No existe":
         #   print('----Error el codigo que desea modificar no existe----')
        if  Existename(service)=="No existe name":
             print('----Error el Nombre que desea modificar no existe----')
        else:
            df=pl.read_csv('Inventario.csv')
            palabra=service
            print(Fore.YELLOW+"El Nombre actual contiene:  "+Fore.RESET)
            #print(df.filter(df['codigo'].str.contains(palabra)))
            print(df.filter(df['service'].str.contains(palabra)))
            print('Ingrese el codigo a modificar')
            codigo=input("o intro::")
            ubicacion=input(' service: ')
            descripcion=input('email: ')
            unidad=input('password :')
            tipo=input('username: ')
            familia=input(' Web: ')
            fecha=today
            modificarBDD(codigo,ubicacion,descripcion,unidad,tipo,familia,fecha)




def modificarBDD(codigo,ubicacion,descripcion,unidad,tipo,familia,fecha):
    result=[]
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            #Compara el codigo hasta encontrar lugar vacio
            if row['codigo']==codigo:
                row['codigo']=codigo
                row['service']=ubicacion
                row['email']=descripcion
                row['password']=unidad
                row['username']=tipo
                row['web']=familia
                row['fecha']=fecha
            
            result.append(row)
        
    with open('Inventario.csv','w')as File:
        fieldnames=['codigo','service','email','password','username','web','fecha']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)
        actualizacion_sesion()
        print(f"EL {ubicacion} CON {descripcion} SE AGREGÓ CORRECTAMENTE")


def ExisteCodigo(codigo):
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            if(codigo==row['codigo']):
                return row
        return "No existe"


def BuscarPorNombre():
    ver= open('estado.txt','r')
    var=ver.read()
    

    if var == 'encrypted':
        print(Fore.RED+"Primero debe desencriptar el archivo!!"+Fore.RESET)
    else:

        df=pl.read_csv('Inventario.csv')
        palabra=str(input('Ingrese el nombre a buscar: '))
        print(Fore.YELLOW+"Servicios con la palabra  "+Fore.RESET+ (palabra))
        print(df.filter(df['service'].str.contains(palabra)))
        #print(Fore.YELLOW+"Emails con la palabra  "+Fore.RESET+ (palabra))
        print(df.filter(df['email'].str.contains(palabra)))
        #print(Fore.YELLOW+"Usuarios con la palabra  "+Fore.RESET+ (palabra))
        print(df.filter(df['username'].str.contains(palabra)))
        #print(Fore.YELLOW+"webs con la palabra   "+Fore.RESET+ (palabra))
        print(df.filter(df['web'].str.contains(palabra)))
       

def pausa():
    input("\nPresiona Enter para continuar...")
#soluconar logica para encryptarb sin que se vuelva un bucle

def main():

    validate()
    while True:
        show()
        option=menu()
        if option == '1':
            VerInventario()
            pausa()
        elif option == '2':
            ProductoNuevo()
            pausa()
        elif option == '3':
            ModificarProducto()
            pausa()
        elif option == '4':
            BuscarPorNombre()
            pausa()
        elif option == '5':
            estado()

            pausa()
        elif option == '6':
            estado_dos()
            pausa()
        elif option == '7':
            Generate_pas()
            pausa()
        elif option == '8':
            genera_clave()
            pausa()
        # elif option == '9':
        #     decrypted_key()
        #     pausa()
        elif option == 'eliminartodo':
            Eliminacion()
            pausa()
        # elif option == '10':
        #     estado_key()
        #     pausa()
        elif option == 'exit' or 'salir':
            estado_salida()
            clearConsole()
            print(Fore.GREEN + "Revisando ..."+ Fore.RESET)
            time.sleep(1)
    
            clearConsole()
            print(Fore.GREEN + "SALIENDO....!" + Fore.RESET)
            break
        else:
            print('opcion invalida')
     
main()


