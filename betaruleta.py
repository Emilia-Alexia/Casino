#Casino El Minino - Ruleta------------------------------------------------------------------------------------------------------------
#Módulos ---------------------------------------------------------------------------------------------------------------------------------
import os
from colorama import *
init ()
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
dialogo_1 = '¡Bienvenido a la Ruleta! Yo seré el que de la vuelta a la ruleta.'
dialogo_2 = 'De momento, solo puedes apostar por color o por número.'
dialogo_3 = '¿Cuánto deseas apostar?'
dialogo_4 = 'De acuerdo, ¡pongamos la ruleta en marcha!'
dialogo_5 = 'Uy, parece que no tienes doblones suficientes... Si quieres seguir divirtiendote, sugiero que visites al banquero.'
dialogo_ganar = 'Parece que la suerte te sonríe y conseguiste una recompensa.'
dialogo_perder = 'Bof, que mal, nada. ¿Intentamos de nuevo?'

#Imágenes ascii a usar
ruleta_titulo = Fore.MAGENTA + '''
,------.         ,--.         ,--.                  
|  .--. ',--.,--.|  | ,---. ,-'  '-. ,--,--. ,---.  
|  '--'.'|  ||  ||  || .-. :'-.  .-'' ,-.  |(  .-'  
|  |\  \ '  ''  '|  |\   --.  |  |  \ '-'  |.-'  `) 
`--' '--' `----' `--' `----'  `--'   `--`--'`----'  
''' + Fore.RESET
gato_traje_rul = '''                                                                         
                               ▒░                         ░▒▒                               
                              ░▓▓▓▓░░  ░░░░░░░░░░░░░  ░▓▓▓▒▒▓                               
                               ▓▓▒▓▓▓▒▒▒▒▒▓▒▒▒▒▒▒▒▒▓▓▓▓▓▒▓▒▒▒                               
                               ▒▓▓▓▓▓█▓▒▓▒▓▒▒▒░▓▒▒▓▒▒▓▓▒▒▒▓▓                                
                                ▓▓▓▓███▓▓▓▓▓▓▒▒▒▓▒▒▒▒▓▓▓▓▓▓▒                                
                                ░▓█▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▒▓▓▒▓▒▓▓                                 
                                 ▓▓▓█▓▓▓▓▓▓▒▓▓▓▒▓▒▓▓▓▓▒▓▓▓░                                 
                                 ▓▒▓▓█▓▒▒█▓▓▒▒▓▓▒▓▒▒▒▒▓▒▒▒                                  
                                 ▓▒▓▓▒▒▒▒▓▓▓▓▒▓▓▒▓▒▒▒▒▒▒▒░                                  
                                 ▒▓▓▒▓▒▒▒▓▒▓▒▓▓▒▓▒▒▒▒▒▓▒▒░                                  
                                  ▓▒▒▒▒▓▓█▒▒▓▒░▒▒█▓█▒░▒▒▒                                   
                                   ▓▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒                                    
                                    ▒▓▒▒░▒▓▓▒▒▒▒░▒▒▒▒▒▒                                     
                                     ░▒▓▒▒▒▓▓▓▒░▒▒▒▒▒░                                      
                                     █▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓                                       
                                   ███▓▓▓▓▓▓▒▒▒▓▓▓░▒████▓                                   
                               ███████▓▓▓▒▒▒▓▓▓▒░░░▒█████████▓                              
                          ░████████████▓▒▒▒██▓▒▒░░░▒███████████████                         
                     ▓█████████████████▓▒▒███▓▓▓█░░▒█████████████████▓                      
                   ███████████████████▓▒▒▒▒▓██▓░░▒▒▒██████████████▓▓██▒                     
                   ████████████████████▒▒▒▒▒██▒▓░░░▒██▓███████████▓█▓██                     
                   ████████████████████▓▒▒▒▒█▓▒▒▓░░▒██▓██████▓▓▓███████░                    
                  ▒█████████████████████▒▒▒▓█▓▓▒▒░░▒█▓███████▓██████████                    
                  ██████████████████████▒▒░▓▓▓▓▒▒░░▒████████████████████                    
                  ██████████████████████▓░▒▓▓▓▓▒▒▒░▓██▓██████████████████                   
                  ███████████████████████▒░▓▒▓▓▒▒▒▒██▓██▓████████████████                   
                 ████████████████████████▓▒█▓▓▒▒▒▒▒█▓█████████████████████                  
                 █████████████████████████▒█▒▓▓▓▒▒▓███████████████████████                  
                 ███████████████████████████▓▒▒▒▓▓▓████████████████████████                 
                ░███████████████████████████▓▓▓▒▒▓█████████████████████████                 
                ████████████████████████████▓▓▓▓▒▓█████████████████████████░                
                █████████████████████████████▓▓▓▓███████████████ ███████████                
                █████████████████████████████▓▓▓▓███████████████ ███████████                
                █████████████████████████████▓▓▓████████████████ ███████████                
               ▒██████████████████████████████▓▓███████████████▓ ████████████               
               ███████████░░██████████████████▓████████████████▒ ████████████░              
               ███████████  ███████████████████████████████████░ █████████████              
               ███████████  ███████████████████████████████████░  ████████████              
              ░███████████  ███████████████████████████████████░  ███████████               
              ████████████  ███████████████████████████████████░░██████████▓                
              ███████████▓  █████████████████████████████████████████▓█████░                
              ███████████  █████████████████████████████████████████████▓█░                 
              ███████████  ████████████████████████████████▒▓▓▓░█████████░                  
             ▓███████████  ██████████████████████████████▓▓▓▒▓▓▓▒██████░                    
             ████████████ ██████████████████████████████▒▒▒▓▒▒▒▓▒█████                      
             ████████████ ██████████████████████████████▒▒▒▒▒▒▓▒▓███                        
             ████████████░███████████████████████████████▓▒▒▒▓███▓█                         
             ████████████▓████████████████████████████████████████                          
             ███████████▒████████████████████████████████████████                           
             ███████████ ████████████████████████████████████████░                          
             ███████████ █████████████████████████████████████████                          
             ███████████░█████████████████████████████████████████                          
             █████████████████████████████████████████████████████                          
             █████████████████████████████████████████████████████▓                         
             ██████████████████████████████████████████████████████                         
             ██████████████████████████████████████████████████████                         
             ██████████████████████████████████████████████████████░                        
             ██▓▓▒▒▒▒▓█▓████████████████████████████████████████████                        
              ▒▒▓▓▓▓▒▒░█████████████████████████████████████████████                        
              ▒▒▓▓▓▓▒░░█████████████████████████████████████████████                        
               ▒▒▓▓▓▒░░█████████████████████████████████████████████                        
               ▒▒▒▒▒░░   ███████████████████████████████████████████                        
                ▒░▒▒▒░   ███████████████████████████████████████████                        
                  ░░     ███████████████████████████████████████████▒                       
                         ▓████████████████████▓ █████████████████████                       
'''
ruleta_diseño = '''
                           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                           
                     ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒                     
                  ▒▒▒▒▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▒▒▒▒                  
               ▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒               
             ▒▒▓▓▓▓█▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▒▓▓▓▓█▓▓▓▓▒▒             
           ▒▒▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▒░░  ░░░░  ░░▒▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▒▒           
         ▒▒▓▓▓▓▓▓▓▓▓▓▓▒▓░░▒███▓ ▓▓░ ░▒▓░░░███▒░░▓▓▓▓▓▓▓▓▓█▓▓▓▒▒         
       ▒▒▒▓▓█▓▓▓▓▓▓▒▓░░▓▓░▓ █ ░▓░▓▒▒▒▒░  ▒████▒▒▓░░▓▓▓▓▓▓▓▓█▓▓▓▒▒       
      ▒▒▓█▓▓▓▓▓▓▓▒▓░███▓  ▓█▓░▒██▓░▓▓░▓██▒░▓█░▓▒ ▒██░▓▒▓▓▓▓▓▓▓▓▓▒▒      
     ▒▒▓▓█▓▓▓▓▓▓▓░▓█░▓ ▓▓░█▓███░▓▓░  ░▓▓░███▒█░▓█▓███▓░▓▒▓▓▓▓▓█▓█▒▒     
    ▒▒▓▓▓▓▓▓▓▓▓░▓▒ ▓▓█░██▒▓▓░████░    ░█▓██░▓▓▓██░█░▓▓▓▓░▓▓▓▓▓▓▓▓▓▒▒    
   ▒▒▓▓▓▓▓▓▓▓▓░██▓▓▓░█░███░█░░░░        ░░░░█░███░█░▓▓▓██░▓▓▓▓▓▓▓▓▓▒▒   
  ▒▒▓▓▓▓▓▓▓▓▓░███ █░▓▓▓▓▓░░░░█▒▒▒▒▒▒▒▒▒▒▒▒█░░░░█▓▓▓▓░██  █░▓▓▓▓▓▓█▓█▒▒  
 ▒▒▓▓█▓▓░▓▓▓░▓▓░█▒███░▓░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░▓░███▒█▒▒▓░▓▓░░▓▓██▓▒▒ 
 ▒▒▓▓▓▓▓▓▓▓░▓░░▓░█░▒██░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███░█░▓ ▒▓░▓▒▓▓▓▓▓█▒▒ 
▒▒▓▓█▓▓▓▓▓░█▒█░▓█▓▓▓▓░░█▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒█░░▓▓▓▓█▓░███░▓▓▓▓▓███▒▒
▒▒▓▓▓▓▓▓▓▓░█ █▓░███░░░█▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒█░░░███░██░█░▓▓▓▓▓▓██▒▒
▒▒▓▓▓▓▓▓▓▓▓▓▓░▒▓████░░▒▓▓▒▒▒▒▒▒▒▓▒░▒▒░▓▓▒▒▒▓▒▒▒▒▒▒░░████▓▒░▓▓▓▓▓▓▓▓▓▓█▒▒
▒▓▓▓▓▓▓▓▓░▓ ░░░█▓▓▓░░▓▓▓▓▓▒▓▓▓▒▓▒░▒▒▒▒░▒▒▓▓▒▓▒▒▓▒▒▓░░▓▓▓█░▒▓░▓░▓▓▓▓▓▓█▓▒
▒▓▓▓██▓▓▓░▒░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░▒░▓▓▓██▓█▓▒
▒▓▓▓▓▓▓▓▓░█░██▒████░░▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓░░████▒▒  █░▓▓▓▓▓▓█▓▒
▒▒█▓▓▓▓▓▓▓▓██░▒▒▓▓▓█░░▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░█▓▓▓▒▒░██▓▓▓▓▓▓▓▓█▒▒
▒▒▓▓▓▓▓▓▓▓░▓ ▓▓░▓▓▓░░░▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓░░░▓▓▓░▓▓░▓░▓▓▓▓▓▓█▓▒▒
▒▒▓▓█▓▓▓▓▓░▓▓▓░██████░░▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓░░██████░▓▓█░▓▓▓▓▓███▒▒
 ▒▒█▓▓▓▓▓▓▓░█   ▒█░▓▓▓░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░▓▓░▒█▒░▒░█░▓▓▓▓▓▓▓█▒▒ 
 ▒▒▓▓█▓▓░░▓▓░██░▓▒█▓▓░█░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░█░▓▓█▒▓░██░▓▓▓░▓▓██▓▒▒ 
  ▒▒▓▓▓▓▓▓▓▓▓░▓ ▒▓▓░█████░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▒████░▓  ▓▓░▓▓▓▓▓▓▓██▒▒  
   ▒▒▓▓▓▓▓▓▓▓▓░▓▓█ █░█░▓▓▓░█░░░░░░░░░░░░░░░░█░▓▓▓░█░███▓▓░▓▓▓▓▓▓█▓█▒▒   
    ▒▒█▓▓▓▓▓▓▓▓░██▒█░▓░█████░▓▓▒█▓░░░░▓█▓▓▓░██▓▓█░▓██ ██░▓▓▓▓▓▓█▓▓▒▒    
     ▒▒███▓▓▓▓▓▓▓░█▓▓▒▓▓█░█▒▓▓▓░██░▒▒░██░▓▓▓██░█▓▒▓░▓█░▓▓▓▓▓▓▓██▓▒▒     
      ▒▒█▓▓▓▓▓▓▓▓▓▓░█▓░░ █░▓▒░░███░▓▓░███▒░▓▓█  █▓▓█░▓▓▓▓▓▓▓▓▓▓▓▒▒      
       ▒▒▓█▓█▓▓▓▓▓▓▓▓░▒█▓▓▓▓ ▓▒▒ ░▒▒▒▒█ █▒ ░ ▒▒▓█▒░▓▓▓▓▓▓▓▓██▓▓▒▒       
         ▒▒▓▓▓█▓▓▓▓▓▓▓▓▓▒░▒█▓▓█ ░█▒  ▒█  █▓▓█▒░▒▓▓▓▓▓▓▓▓▓█▓██▒▒         
           ▒▒▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░▒▒▒▒░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▒▒           
             ▒▒▓▓▓▓█▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓█▓█▓▓▒▒             
               ▒▒▒█▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒               
                  ▒▒▒▓▓██▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓█▓▒▒▒                  
                     ▒▒▒▒▒▓▓██▓▓▓██▓▓▓▓█▓▓█▓▓▓▒▒▒▒▒                     
                           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                           
'''
#Defino los colores de la ruleta
rojo = Fore.RED
negro = Fore.BLACK
verde = Fore.GREEN
blanco = Fore.WHITE
#Números de la ruleta con sus colores
ruleta = [
    (0, verde), (32, rojo), (15, negro), (19, rojo), (4, negro), (21, rojo),
    (2, negro), (25, rojo), (17, negro), (34, rojo), (6, negro), (27, rojo),
    (13, negro), (36, rojo), (11, negro), (30, rojo), (8, negro), (23, rojo),
    (10, negro), (5, rojo), (24, negro), (16, rojo), (33, negro), (1, rojo),
    (20, negro), (14, rojo), (31, negro), (9, rojo), (22, negro), (18, rojo),
    (29, negro), (7, rojo), (28, negro), (12, rojo), (35, negro), (3, rojo),
    (26, negro), (0, verde)
]

#Consola
consola = Console()

#Clases ----------------------------------------------------------------------------------------------------------------------------------
#Introducción
def Introduccion():
    print (ruleta_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (ruleta_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (ruleta_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (ruleta_titulo)
    time.sleep(2)
    os.system('cls')
    consola.print(gato_traje_rul)
    consola.print(Panel(dialogo_1, border_style="white", box=HEAVY))
    time.sleep(5)
    os.system('cls')
    consola.print(gato_traje_rul)
    consola.print(Panel(dialogo_2, border_style="white", box=HEAVY))
    time.sleep(5)
    os.system('cls')
    consola.print(gato_traje_rul)
    consola.print(Panel(dialogo_3, border_style="white", box=HEAVY))
    time.sleep(3)
    os.system('cls')
    
#Clase para aceptar
def Aceptar():
    consola.print(gato_traje_rul)
    if betabanquero.doblones >50 : #Si tiene doblones se le deja jugar
        consola.print(Panel(dialogo_4, border_style="white", box=HEAVY))
        time.sleep(3)
        os.system('cls')
        return True 
    else:
        return False

#Clase para rechazar
def Rechazar():
    if betabanquero.doblones < 50: #Si no tiene doblones no se le deja jugar
        os.system('cls')
        consola.print(gato_traje_rul)
        consola.print(Panel(dialogo_5, border_style="white", box=HEAVY))
        input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
        os.system('cls')
        return True 
    else:
        return False

#Clase ruleta (Use el chatgpt para esta, que si no me generaba un dolor de cabeza)
def Mostrar_Ruleta():
    print(f"{blanco}  ┌────────────────────────────────────────┐")
    print(f"{blanco}  | {rojo}  32  {negro}  15  {rojo}  19  {negro}  4  {rojo}  21  {negro}  2  {rojo}  25  {negro}  17  {rojo}  34  {negro}  6  {rojo}  27  {negro}  13  {rojo}  36  {negro}  11  {rojo}  30  {negro}  8  {rojo}  23 {blanco} |")
    print(f"{blanco}  | {rojo}  10  {negro}  5  {rojo}  24  {negro}  16  {rojo}  33  {negro}  1  {rojo}  20  {negro}  14  {rojo}  31  {negro}  9  {rojo}  22  {negro}  18  {rojo}  29  {negro}  7  {rojo}  28  {negro}  12  {rojo}  35 {blanco} |")
    print(f"{blanco}  |                {verde}   0   {blanco}                |")
    print(f"{blanco}  └────────────────────────────────────────┘")


#Clase de ruleta para jugar
def Ruleta(opcion):
    #Muestra una ruleta como efecto visual
    print(ruleta_diseño)
    time.sleep (3)
    os.system('cls')
    #Muestro la ruleta y su diseño mientras apuestan
    print (Mostrar_Ruleta())
    #Las listas con los valores
    colores = ['negro','rojo']
    numeros = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13, 1, 00, 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]
    #Abro condicional
    #Si el usuario escoje color
    if opcion.lower() == 'color':
        color = input ('¿Qué color?:')
        #Abro condicional para cada color
        if color.lower() == 'negro':
            #Otro condicional
            #Si acierta el color del random shuffle
            if color.lower() == random.shuffle(colores):
                print ('Ganaste')
                print ('Cayó en negro')
            #Si no lo acierta
            else:
                print ('Perdiste')
                print ('Cayo en rojo')
        elif color.lower() == 'rojo':
            #Si acierta el color del random shuffle
            if color.lower() == random.shuffle(colores):
                print ('Ganaste')
                print ('Cayo en rojo')
            else:
                print ('Perdiste')
                print ('Cayó en negro')
        else:
            print ('No es ninguna de las opciones dadas.')
    #Si el usuario escoje el número
    elif opcion.lower() == 'num':
        #Random shuffle en números
        random.shuffle(numeros)
        #Abro bucle
        for i in numeros:
            numero = input ('¿Qué número?:')
            #Si acierta el numero del random shuffle
            if i == numero:
                print ('Ganaste')
                print (f'Cayo en {i}')
                break
            #Si no lo acierta
            elif i != numero:
                print ('Perdiste')
                print (f'Cayo en {i}')
                break
    else: #Foolproof
        print ('No es ninguna de las opciones dadas.')