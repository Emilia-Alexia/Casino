#Casino El Minino - Gacha ------------------------------------------------------------------------------------------------------------
#Módulos ---------------------------------------------------------------------------------------------------------------------------------
import os
from colorama import *
import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.box import HEAVY
import betabanquero
#Programa - Preparaciones ----------------------------------------------------------------------------------------------------------------
#Consola
consola = Console()

#Diálogos principales
dialogo_1 = 'Un anuncio te llama la atención. Gacha edición coleccionista. Aparentemente es para tirar por personajes.'
dialogo_2 = 'Cuesta 5 fichas, es barato.'
dialogo_3 = 'Metes las cinco para ver que te sale...'
dialogo_4 = 'Vas a por tus doblones solo para darte cuenta de que no tienes suficientes... una pena, será mejor visitar al banquero.'

#Imágenes ascii a usar
gacha_titulo = Fore.MAGENTA + '''
 ,----.                 ,--.              
'  .-./    ,--,--. ,---.|  ,---.  ,--,--. 
|  | .---.' ,-.  || .--'|  .-.  |' ,-.  | 
'  '--'  |\ '-'  |\ `--.|  | |  |\ '-'  | 
 `------'  `--`--' `---'`--' `--' `--`--' 
''' + Fore.RESET
gashapon = '''
                                                                                
          ████████████████████████████████████████████████████████████          
         ████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████         
         ███▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███        
         ███▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███        
         ██████████████████████████████████████████████████████████████         
           ███▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███           
           ███▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███           
            ████████████████████████████████████████████████████████            
              ██░░░░                       ░░░░░░              ░███             
              ██░░░░         ░▓███▓░    ░▓█████████░           ░███             
              ██░░░░      ░███████████░▓███░     ▒███░         ░███             
              ██░░░░     ▓██▓░▒██▒▒▒▓████░        ░███░        ░███             
              ██░░░░    ▓██░░░░██▓▒▒▒▓██░     ░▓███████        ░███             
              ██░░░░   ░██▒░░░░███▒▒▒▓██  ░▓█████▓▒▒███        ░███             
              ██░░░░░  ░██▒░░░░███▒▒▒▓███████▓▒▒▒▒▒▒██▓        ░███             
              ██░░░░░ ░▓██████████▒▓████████▓▓▒▒▓█████████▒░   ░███             
              ██░░░░░███▓░   ░▓██████▓▒░░▒▓███████████░░▓███▒  ░███             
              ██░░░▒██▓         ▓██▓░░░░░░▒██████░░░██░   ░██▓ ░███             
              ██░░░██▓           ▓██░░░░▒███████░░░░██▓    ▒██░░███             
              ██░░░█████████████████░░▓███▓▒▒██▒░░░░▓██     ██▒░███             
              ██░░░██▒░░░░░░░░░░░▒██████▒▒▒▒▒██▓░░░░░██░   ░██▒░███             
              ██░░░▓██▒░░░░░░░░░▒████▓▒▒▒▒▒▒▒███▓░░░░██▓   ███░░███             
              ██░░░░▒███░░░░░░░█████▓▒▒▒▒▒▒▓██████▒░░▒██░▓███░░░███             
            ████████████████████████████████████████████████████████            
           ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████           
           ███▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███████████████▓▒▒▒▒▒███           
           ███▓▓▓▓▒▓▓██████████▓▒▒▒▒▒▒▒▒▒▒▒▒█████████████████▓▒▒▒▒███           
           ███▓▓▓▓▓██████▓▒▒▓████▓▒▒▒▒▒▒▒▒▒▒█████████████████▓▒▒▒▒███           
           ███▓▓▓▓███░ ▒███▒▒▒▒███▓▒▒▒▒▒▒▒▒▒▒▓█████████████▓▒▒▒▒▒▒███           
           ███▓▓▓▓████▒  ▓███▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓█████▓▒▒▒▒▒▒▒▒▒███           
           ███▓▓▓███▒███▒  ▓███▒▓██▒▒▒▒▒▒▒▒▒▒▒▓████████████▓▒▒▒▒▒▒███           
           ███▓▓▓▓██▒▒▓███░  ██████▒▒▒▒▒▒▒▒▒▒▓███▓▓▓▓▓▓▓▓████▒▒▒▒▒███           
           ███▓▓▓▓███▒▒▒▓███  ░███▓▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▓▓▓▓████▒▒▒▒███           
           ███▓▓▓▓▒████▒▒▒███▓░███▓▒▒▒▒▒▒▒▒▒███▓▓▓▓▓▓▓▓▓▓▓▓███▓▒▒▒███           
           ███▓▓▓▓▓▒▓████████████▓▒▒▒▒▒▒▒▒▒▓██▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▒▒▒███           
           ███▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▒▒▒███           
           ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓███           
         ██████████████████████████████████████████████████████████████         
        ████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████        
        ███▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███        
       ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███       
       ██████████████████████████████████████████████████████████████████       
                                                                                
'''

#Consola
consola = Console()

#Clases ----------------------------------------------------------------------------------------------------------------------------------
#Clase para introducir al Crupier
#Clase para introducir al Crupier
def Introduccion():
    print (gacha_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (gacha_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (gacha_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (gacha_titulo)
    time.sleep(2)
    os.system('cls')
    consola.print(Panel(dialogo_1, border_style="white", box=HEAVY))
    time.sleep(5)
    os.system('cls')
    consola.print(Panel(dialogo_2, border_style="white", box=HEAVY))
    
#Clase para aceptar
def Aceptar():
    if betabanquero.doblones >= 5 : #Si tiene doblones se le deja jugar
        consola.print(Panel(dialogo_3, border_style="white", box=HEAVY))
        time.sleep(3)
        os.system('cls')
        return True
    else:
        return False

#Clase para rechazar
def Rechazar():
    if betabanquero.doblones <= 5: #Si no tiene doblones no se le deja jugar
        os.system('cls')
        consola.print(Panel(dialogo_4, border_style="white", box=HEAVY))
        input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
        os.system('cls')
        return True
    else:
        return False

#Función del gacha
def Gacha():
    while True:
        #Esto es para modificar la cantidad de los doblones fuera del propio módulo
        global doblones
        #Resto la cantidad del juego
        betabanquero.doblones -= 5
        os.system('cls')
        print (gashapon)
        time.sleep(5)
        os.system('cls')
        #Listas y diccionarios con los datos
        personajes = ['Ariadna','Emilia','Damián','Jorge','Christian','Pablo','Sergio Gil','Ángel','Marco','José','Sergio Lopéz','Dario','Francisco','Julio','Carlos','Raúl','Gisela','Miguel Ángel','Andrea']
        valores = {'Ariadna':'☆☆☆','Emilia':'☆☆☆','Damián':'☆☆☆☆','Jorge':'☆☆☆','Christian':'☆☆☆☆','Pablo':'☆☆☆','Sergio Gil':'☆☆☆','Ángel':'☆☆☆','Marco':'☆☆☆☆','José':'☆☆☆☆','Sergio Lopéz':'☆☆☆','Dario':'☆☆☆☆','Francisco':'☆☆☆☆','Julio':'☆☆☆','Carlos':'☆☆☆','Raúl':'☆☆☆','Gisela':'☆☆☆','Miguel Ángel':'☆☆☆','Andrea':'☆☆☆'}
        #Sacamos un número random para tener bajas probabilidades
        pity = random.randint(0,80)
        #Si es 80, significa que consiguió al personaje más raro
        if pity == 80 or pity == 50:
            print ('¡Conseguiste al personaje cinco estrellas!')
            print('Conseguiste Daniel rareza ☆☆☆☆☆')
            input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
            os.system('cls')
        #Si no es 80, simplemente se le da un personaje cualquiera del diccionario o lista
        else:
            random.shuffle(personajes)
            elegido = personajes[0]  # elige uno aleatorio tras mezclar
            rareza = valores[elegido]
            random.shuffle(personajes)
            print(f'Conseguiste {elegido} rareza {rareza}')
            input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
            os.system('cls')
        continuar = input ('¿Otra tirada más? (S/N): ')
        if continuar.lower() == 'n':
            break