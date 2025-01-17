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



init()                         
                            #LISTO #Agregar que se pueda guardar la contrasena temporalmente
                            #PENDIENTE Agrega buscador online de archivos 
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

def validate():
    while True:

        

        password = getpass.getpass("Introduce tu contraseña: ")

        if password =="1234":
            break

        elif password =="exit" or password == "salir":
            print("saliendo....")
            estado_salida()
            sys.exit(0)
            #error=="Generado"
            

        elif password !="1234!":
            clearConsole()
            print("┌─┐┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐   ┬┌┐┌┌─┐┌─┐┬─┐┬─┐┌─┐┌─┐┌┬┐")  
            print("├─┘├─┤└─┐└─┐││││ │├┬┘ ││   │││││  │ │├┬┘├┬┘├┤ │   │ ")  
            print("┴  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘   ┴┘└┘└─┘└─┘┴└─┴└─└─┘└─┘ ┴ ")

            

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


#encryptacion automatica al cerrar el programa
def Eliminacion():
    os.remove("Inventario.csv")
    print(Fore.RED+"Archivo eliminado"+Fore.RESET)
    validate()

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
    le = open('estado.txt')
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
                    print("Desea generar una nueva clave de encryptacion")
                    save=input("Y/N :")
                    if save== 'Y' or save== 'y':
                        print("La clave se guardara en el directorio con el nombre: key.key")
                        print(Fore.RED+"La nueva clave de encryptacion es \n"+Fore.RESET)
                        key = Fernet.generate_key()
                        print(key)
                        archivo = open('key.key','wb')
                        archivo.write(key)
                        archivo.close()
                        print(Fore.BLUE+"La clave se a guardado con exito"+Fore.RESET)
                    else:
                        print("SALIENDO...")

        #Elecion si quiero que se desencrypte con llave interna o externa

def encrypted_with_key():
                
                digitos = input('Ingrese 4 digitos que recuerde : ')
                key_agregada = 'a-TE3Yjp6Obuovey30I'+ digitos +'HjiMnQ1BI6UnFh48uYaE='
                print(Fore.RED+ 'Si los olvida no podra recuperar el archivo'+Fore.RESET)
                key = key_agregada
                print("La clave es:")
                time.sleep(2)
                print(key)  

                fernet = Fernet(key) 

                file=open('Inventario.csv', 'rb') 
                original = file.read() 

                encrypted = fernet.encrypt(original) 

                file=open('Inventario.csv', 'rb') 
                original = file.read()

                encrypted_file= open('Inventario.csv', 'wb') 
                encrypted_file.write(encrypted)
                actualizacion_estado()
                print(Fore.RED+"El archivo se encrypto con exito"+Fore.RESET)

          
def encrypted():

        key = 'TnU7BwDz2-U7B1R9slai48vJgnl93GN-5xYpw14ZDyg='
            #key = Fernet.generate_key()
            #archivo = open('key.key', 'rb')
            #key=archivo.read()

                #with open('key.txt', 'wb') as filekey:
                 #  filekey.write(key)

        fernet = Fernet(key)     
        file=open('Inventario.csv', 'rb') 
        original = file.read() 

        encrypted = fernet.encrypt(original) 

        file=open('Inventario.csv', 'rb') 
        original = file.read()


        encrypted_file= open('Inventario.csv', 'wb') 
        encrypted_file.write(encrypted)

        actualizacion_estado()
        print(Fore.RED+"archivo encryptado "+Fore.RESET)


#desencrptacion automatica al introducior la contraseña correcta


    #print(Fore.BLUE + Style.BRIGHT+"Archivo desencryptado con exito!"+Style.RESET_ALL)
    #return
def decrypted():    

        key = 'TnU7BwDz2-U7B1R9slai48vJgnl93GN-5xYpw14ZDyg='
        fernet = Fernet(key) 

        enc_file= open('Inventario.csv', 'rb') 
        encrypted = enc_file.read() 

        decrypted = fernet.decrypt(encrypted)

        dec_file= open('Inventario.csv', 'wb')
        dec_file.write(decrypted)
        actualizacion_estado_dos()
        time.sleep(0.5)
        print(Fore.BLUE + Style.BRIGHT+"El archivo se desencrypto "+Style.RESET_ALL)



def decrypted_key():

  
        pregunta= input(Fore.RED + Style.BRIGHT+"Ingrese sus 4 digitos: "+Style.RESET_ALL)
        print(Fore.RED+ "AVISO" +Fore.RESET)
        time.sleep(1)
        print('Si ingresa los codigos incorrectamente el archivo no se vera desencryptado')
        time.sleep(2)  
        

        key_de_digitos = 'a-TE3Yjp6Obuovey30I' + pregunta + 'HjiMnQ1BI6UnFh48uYaE= '
        key = key_de_digitos
        fernet = Fernet(key) 

        enc_file= open('Inventario.csv', 'rb') 
        encrypted = enc_file.read() 

        decrypted = fernet.decrypt(encrypted)

        dec_file= open('Inventario.csv', 'wb')
        dec_file.write(decrypted)
        actualizacion_estado_dos()
        print(Fore.YELLOW +"Archivo desencryptado"+Fore.RESET)


def menu():

    #print("******MENU INVENTARIO******")
    print("1--- Ver   ","                   2--- Agregar " )
    print("3--- Modificar ","               4--- Buscar")
    print("5--- Encryptar      ","          6--- Desencryptar")
    print("7--- Generar password","         8--- Genera_key_encrypt")
    print("9--- Decryp_con_key","           10---Encryp_externa")
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


        

#Modificacion del inventario
def ProductoNuevo():
    ver= open('estado.txt','r')
    var=ver.read()

    if var == 'encrypted':
        print(Fore.RED+"Primero debe desencriptar el archivo!!"+Fore.RESET)
        
    else:
    
        from random import randint
        lista = []
        for x in range(2):
            lista.append(str(randint(0,99)))
            #lista.append(str(a)) #Estas 2 líneas se pueden juntar en: lista.append(str(randint(0,9)))

        codigo = ''
        for x in range(2):
            codigo = codigo + lista[x]
            codigo_int = int(codigo)

            today = str(date.today())

            
        if ExisteCodigo(codigo)=="No existe":
            ubicacion=input('Servicio: ')
            descripcion=input('Email: ')
            unidad=input('Password: ')
            tipo=input('Usuario: ')
            familia=input('Referencia: ')
            fecha=today


            with open ('Inventario.csv','a')as File:
                File.write('\n'+codigo+','+ubicacion+','+descripcion+','
                +unidad+','+tipo+','+familia+','+fecha)
        else:
            print("****Error el codigo ya existe****")

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
    input('Intro para continuar :')
#soluconar logica para encryptarb sin que se vuelva un bucle

def main():

    validate()
    while True:
        pausa()
        show()
        option=menu()
        if option == '1':
            VerInventario()
        elif option == '2':
            ProductoNuevo()
        elif option == '3':
            ModificarProducto()
        elif option == '4':
            BuscarPorNombre()
        elif option == '5':
            estado()
        elif option == '6':
            estado_dos()
        elif option == '7':
            Generate_pas()
        elif option == '8':
            genera_clave()
        elif option == '9':
            decrypted_key()
        elif option == 'eliminartodo':
            Eliminacion()
        elif option == '10':
            estado_key()
        elif option == 'exit' or 'salir':
            estado_salida()
            clearConsole()
            print("SALIENDO....")
            break
        else:
            print('opcion invalida')
     

main()


