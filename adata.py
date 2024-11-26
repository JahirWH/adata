import os
import sys
import csv
import getpass
import random
import polars as pl
from random import choice
from datetime import date, datetime
from cryptography.fernet import Fernet
from colorama import init, Fore, Style
from time import sleep

# Inicializa colorama para usar colores en la consola
init()

# Constantes
ENCRYPTION_KEY = 'TnU7BwDz2-U7B1R9slai48vJgnl93GN-5xYpw14ZDyg='
DATE_FILE = 'date.txt'
STATE_FILE = 'estado.txt'
TEMP_PASSWORD_FILE = 'temp.txt'
INVENTORY_FILE = 'Inventario.csv'


def clear_console():
    """Limpia la consola dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def load_bar(total, prefix='Progreso:', suffix='Completado', length=50, fill='█'):
    """Muestra una barra de carga."""
    for i in range(total + 1):
        percent = f"{100 * (i / float(total)):.1f}"
        filled_length = int(length * i // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
        sleep(0.01)
    print()


def validate_user():
    """Valida la contraseña del usuario para acceder al programa."""
    while True:
        password = getpass.getpass("Introduce tu contraseña: ")
        if password == "2009":
            break
        elif password.lower() in ("exit", "salir"):
            print("Saliendo del programa...")
            sys.exit(0)
        else:
            print(Fore.RED + "Contraseña incorrecta, inténtalo de nuevo." + Style.RESET_ALL)


def read_file(filepath):
    """Lee el contenido de un archivo y lo retorna."""
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return file.read().strip()
    return None


def write_file(filepath, content):
    """Escribe contenido en un archivo, sobrescribiéndolo si ya existe."""
    with open(filepath, 'w') as file:
        file.write(content)


def update_last_modified():
    """Actualiza la última fecha y hora de modificación."""
    now = str(datetime.now())
    write_file(DATE_FILE, now)


def generate_password(length=12):
    """Genera una contraseña aleatoria."""
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
    password = ''.join(choice(characters) for _ in range(length))
    write_file(TEMP_PASSWORD_FILE, password)
    print("Contraseña generada: " + Fore.BLUE + password + Style.RESET_ALL)


def encrypt_file(key, filepath):
    """Encripta un archivo con una clave proporcionada."""
    with open(filepath, 'rb') as file:
        data = file.read()
    encrypted_data = Fernet(key).encrypt(data)
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)
    write_file(STATE_FILE, 'encrypted')
    print(Fore.GREEN + "Archivo encriptado correctamente." + Style.RESET_ALL)


def decrypt_file(key, filepath):
    """Desencripta un archivo con una clave proporcionada."""
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = Fernet(key).decrypt(encrypted_data)
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)
    write_file(STATE_FILE, 'decrypted')
    print(Fore.BLUE + "Archivo desencriptado correctamente." + Style.RESET_ALL)


def verify_encryption_state():
    """Verifica el estado de encriptación del archivo."""
    state = read_file(STATE_FILE)
    return state if state else "unknown"


def menu():
    """Despliega el menú principal."""
    print(Fore.YELLOW + "Menú Principal:" + Style.RESET_ALL)
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Modificar producto")
    print("4. Buscar producto")
    print("5. Encriptar archivo")
    print("6. Desencriptar archivo")
    print("7. Generar contraseña")
    print("8. Salir")
    return input("Selecciona una opción: ")


def main():
    """Función principal del programa."""
    validate_user()
    while True:
        clear_console()
        option = menu()

        if option == '1':
            print("Ver inventario")
        elif option == '2':
            print("Agregar producto")
        elif option == '3':
            print("Modificar producto")
        elif option == '4':
            print("Buscar producto")
        elif option == '5':
            encrypt_file(ENCRYPTION_KEY, INVENTORY_FILE)
        elif option == '6':
            decrypt_file(ENCRYPTION_KEY, INVENTORY_FILE)
        elif option == '7':
            length = input("Longitud de la contraseña (por defecto 12): ")
            length = int(length) if length.isdigit() else 12
            generate_password(length)
        elif option == '8':
            print("Saliendo del programa...")
            break
        else:
            print(Fore.RED + "Opción inválida, intenta de nuevo." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
