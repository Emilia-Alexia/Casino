#Casino El Minino ------------------------------------------------------------------------------------------------------------------------
#Módulos ---------------------------------------------------------------------------------------------------------------------------------
import os
from colorama import *
import pygame
import time
from rich.console import Console #Para poder usar la consola
from rich.panel import Panel #Para poder usar los paneles que hacen las cajas de diálogo
from rich.box import HEAVY #Para poder usar el estilo de cajas heavy
from rich.prompt import Prompt #Para poder hacer el menú principal (Oficialmente me enamore del módulo rich)
#Módulos creados por mi ---------------------------------------------------------------------------------------------------------------------------------
import betabanquero
import betablackjack
import betagacha
import betaruleta
#Programa --------------------------------------------------------------------------------------------------------------------------------
#Valores de rich
consola = Console()

#Para el menú, la lista de opciones
menu = [
    "1.BLACKJACK",
    "2.TRAGAPERRAS",
    "3.RULETA",
    "4.EDICIÓN COLECCIONISTA (GACHA)",
    "5.BANQUERO",
    "6.SALIR"
]

#Diálogos para usar con los paneles de inicio, la introducción, vamos:
dialogo_intro_1 = 'Bienvenido al Casino El Minino, donde puedes apostar tus Doblones de manera tranquila.'
dialogo_intro_2 = 'Te recomiendo dirigirte al banco para cambiar tus monedas por las fichas de aquí, llamadas "Doblones".'
dialogo_intro_3 = 'Que la suerte te sonría.'

#Imagenes y textos ASCII para simplemente reutilizar código 
anuncio = Fore.RED + '''
                                                       ___                                                   
                          .-.                         (   )                .-.          .-.                  
  .--.     .---.    .--. ( __)___ .-.   .--.     .--.  | |   ___ .-. .-.  ( __)___ .-. ( __)___ .-.   .--.   
 /    \   / .-, \ /  _  \(''"|   )   \ /    \   /    \ | |  (   )   '   \ (''"|   )   \(''"|   )   \ /    \  
|  .-. ; (__) ; |. .' `. ;| | |  .-. .|  .-. ; |  .-. ;| |   |  .-.  .-. ; | | |  .-. . | | |  .-. .|  .-. ; 
|  |(___)  .'`  || '   | || | | |  | || |  | | |  | | || |   | |  | |  | | | | | |  | | | | | |  | || |  | | 
|  |      / .'| |_\_`.(___) | | |  | || |  | | |  |/  || |   | |  | |  | | | | | |  | | | | | |  | || |  | | 
|  | ___ | /  | (   ). '. | | | |  | || |  | | |  ' _.'| |   | |  | |  | | | | | |  | | | | | |  | || |  | | 
|  '(   ); |  ; || |  `\ || | | |  | || '  | | |  .'.-.| |   | |  | |  | | | | | |  | | | | | |  | || '  | | 
'  `-' | ' `-'  |; '._,' '| | | |  | |'  `-' / '  `-' /| |   | |  | |  | | | | | |  | | | | | |  | |'  `-' / 
 `.__,'  `.__.'_. '.___.'(___|___)(___)`.__.'   `.__.'(___) (___)(___)(___|___|___)(___|___|___)(___)`.__.'    
''' + Fore.RESET
tragaperras_titulo = Fore.MAGENTA + '''
,--------.                                                                                  
'--.  .--',--.--. ,--,--. ,---.  ,--,--. ,---. ,--.,--. ,---. ,--.--.,--.--. ,--,--. ,---.  
   |  |   |  .--'' ,-.  || .-. |' ,-.  || .-. ||  ||  || .-. :|  .--'|  .--'' ,-.  |(  .-'  
   |  |   |  |   \ '-'  |' '-' '\ '-'  || '-' ''  ''  '\   --.|  |   |  |   \ '-'  |.-'  `) 
   `--'   `--'    `--`--'.`-  /  `--`--'|  |-'  `----'  `----'`--'   `--'    `--`--'`----'  
                         `---'          `--'                                                
''' + Fore.RESET
gato_traje = '''                                                                                         
                                        ░▒░ ░░░       ░░ ░░░                                        
                                         ░░░░░▒▒▓▒▒▒▒▓▒░▒  ░                                        
                                         ▓▒ ░░░▒░▓▓▓░▒░░░░█▒                                        
                                          ░ ░▒▓▒░░▒▒░▒▓▒  ░░                                        
                                         ░▒░▒███░░░░▒███░░▒                                         
                                        ░▒░░▒▒░░▒░ ░░░░▒▒▒░░                                        
                                        ░░░▒▒▒▒░░█▓█ ░▒▒▒░░░                                        
                                         ▒▓▒░     ▒     ░▒▒                                         
                                           ▒░          ░▒░                                          
                                          ███▓▒░    ░▒▒▒▓██▒                                        
                                     ░██████░   ░▒█░    ▓███████▓                                   
                                ░▓██████████░  ░████▒░  █████████████░                              
                               █████████████░    ██▓    ██████████████░                             
                              ██████████████▓    ▒██    ██████████████▓                             
                             ░███████████████    ███▒  ░███████████████▓                            
                             ▓███████████████▓  ▓███▓  ▒████████████████▓                           
                            ░█████████████████  █████  ██████████████████░                          
                            ██████████████████▒ █████ ▒███████████████████                          
                           ▒███████████████████ █████▒█████████████████████                         
                           █████████████████████████████████████████████████                        
                          ░█████████████████████████████████████████████████░                       
                          ▓██████████████████████████████████████████████████                       
                          ████████████████████████████████████████▒░█████████▒                      
                         ░████████████████████████████████████████░ ██████████                      
                         ██████████░██████████████████████████████   █████████▓                     
                         ██████████ ██████████████████████████████   ██████████░                    
                        ░█████████░ ██████████████████████████████   ▒██████████                    
                        ▓█████████░ ██████████████████████████████▒ ░██████████▓                    
                        ███████████▓██████████████████████████████████████████▓                     '''



#Pantalla de inicio de adorno
os.system('cls')
print (anuncio)
time.sleep(0.2)
os.system('cls')
time.sleep(0.3)
print (anuncio)
time.sleep(0.2)
os.system('cls')
time.sleep(0.3)
print (anuncio)
time.sleep(0.2)
os.system('cls')
time.sleep(0.3)
print (anuncio)
time.sleep(5)
os.system('cls')

#Diálogo de la Introducción
consola.print(gato_traje)
consola.print(Panel(dialogo_intro_1, border_style="white", box=HEAVY))
time.sleep(5)
os.system('cls')
consola.print(gato_traje)
consola.print(Panel(dialogo_intro_2, border_style="white", box=HEAVY))
time.sleep(5)
os.system('cls')
consola.print(gato_traje)
consola.print(Panel(dialogo_intro_3, border_style="white", box=HEAVY))
time.sleep(3)
os.system('cls')

#Menú principal
while True:
    os.system('cls')
    #El menú
    menu_mostrar = '\n'.join(menu) #Se usa el join para hacer sola una cadena de texto
    consola.print(Panel(menu_mostrar, title=anuncio, border_style="white",box=HEAVY))
    #Opciones para que el usuario elija, usando el ask de rich para preguntar
    opcion = Prompt.ask('¿Que desea hacer? (1-6)')
    #Opción 1 - Blackjack
    if opcion == '1':
        os.system('cls')
        betablackjack.Introduccion()
        if betablackjack.Aceptar():
            betablackjack.Jugar()
            print (Fore.LIGHTGREEN_EX + f'Doblones: {betabanquero.doblones}' + Fore.RESET)
            os.system('cls')
        elif betablackjack.Rechazar():
            input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
        os.system('cls')
    #Opción 2 - Tragaperras
    elif opcion == '2':
        os.system('cls')
        print (tragaperras_titulo)
        input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
        os.system('cls')
    #Opción 3 - Ruleta
    elif opcion == '3':
        os.system('cls')
        betaruleta.Introduccion()
        if betaruleta.Aceptar():
            betaruleta.Ruleta()
        elif betaruleta.Rechazar():
            input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
        os.system('cls')
    #Opción 4 - Gacha
    elif opcion == '4':
        os.system('cls')
        betagacha.Introduccion()
        if betagacha.Aceptar():
            betagacha.Gacha()
            os.system('cls')
        else:
            betagacha.Rechazar()
            os.system('cls')
        input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
        os.system('cls')
    #Opción 5 - El banquero
    elif opcion == '5':
        os.system('cls')
        betabanquero.Introduccion_Ban()
        cantidad = input ('Cantidad: ')
        os.system('cls')
        betabanquero.Comprobacion(cantidad)
        os.system('cls')
    #Opción 6 - Fin del programa
    elif opcion == '6':
        os.system('cls')
        print (Fore.GREEN + 'Elegiste salir del programa...')
        time.sleep(3)
        print ('Antes de salir, me gustaría dar unos créditos.')
        time.sleep(3)
        print ('Gracias a mi gato Charlie por prestar sus sonidos de gatos para algunos diálogos.')
        time.sleep(1)
        print ('Gracias también a la inteligencia artificial que me hizo conocer el módulo RICH, ChatGPT, me hizo conocer el mejor módulo que vi de Python.')
        time.sleep(1)
        print ('Y a los desconocidos de GitHub por inspirarme y hacerme aprender cosas nuevas.')
        time.sleep(3)
        os.system('cls')
        print('Gracias por usar el programa')
        print ('Pulse ENTER para salir...' + Fore.RESET)
        break
