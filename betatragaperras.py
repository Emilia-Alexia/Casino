#Casino El Minino - Tragaperras ------------------------------------------------------------------------------------------------------------
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
dialogo_1 = 'Te pones enfrente de la máquina de tragaperras, fichas en mano.'
dialogo_2 = '¿Cuánto deseas apostar?'
dialogo_3 = 'Metes la cantidad deseada para apostar, esperas de corazón que te sonría la suerte...'
dialogo_4 = 'Vas a por tus doblones solo para darte cuenta de que no tienes suficientes... una pena, será mejor visitar al banquero.'
dialogo_ganar = 'Parece que la suerte te sonríe y conseguiste una recompensa.'
dialogo_perder = 'Bof, que mal, nada. ¿Intentamos de nuevo?'

#Imágenes ascii a usar
tragaperras_titulo = Fore.MAGENTA + '''
,--------.                                                                                  
'--.  .--',--.--. ,--,--. ,---.  ,--,--. ,---. ,--.,--. ,---. ,--.--.,--.--. ,--,--. ,---.  
   |  |   |  .--'' ,-.  || .-. |' ,-.  || .-. ||  ||  || .-. :|  .--'|  .--'' ,-.  |(  .-'  
   |  |   |  |   \ '-'  |' '-' '\ '-'  || '-' ''  ''  '\   --.|  |   |  |   \ '-'  |.-'  `) 
   `--'   `--'    `--`--'.`-  /  `--`--'|  |-'  `----'  `----'`--'   `--'    `--`--'`----'  
                         `---'          `--'                                                
''' + Fore.RESET

#Consola
consola = Console()

#Clases ----------------------------------------------------------------------------------------------------------------------------------
#Clase para introducir al Crupier
#Clase para introducir al Crupier
def Introduccion():
    print (tragaperras_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (tragaperras_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (tragaperras_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (tragaperras_titulo)
    time.sleep(2)
    os.system('cls')
    consola.print(Panel(dialogo_1, border_style="white", box=HEAVY))
    time.sleep(5)
    os.system('cls')
    consola.print(Panel(dialogo_2, border_style="white", box=HEAVY))
    
#Clase para aceptar
def Aceptar():
    if betabanquero.doblones >50 : #Si tiene doblones se le deja jugar
        consola.print(Panel(dialogo_3, border_style="white", box=HEAVY))
        time.sleep(3)
        os.system('cls')
        return True 
    else:
        return False

#Clase para rechazar
def Rechazar():
    if betabanquero.doblones < 50: #Si no tiene doblones no se le deja jugar
        os.system('cls')
        consola.print(Panel(dialogo_4, border_style="white", box=HEAVY))
        input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
        os.system('cls')
        return True 
    else:
        return False