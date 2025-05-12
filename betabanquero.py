#Casino El Minino - Banquero------------------------------------------------------------------------------------------------------------------------
#Módulos ---------------------------------------------------------------------------------------------------------------------------------
import os
from colorama import *
import time
from rich.console import Console
from rich.panel import Panel 
from rich.box import HEAVY 
from rich.prompt import Prompt

#Programa --------------------------------------------------------------------------------------------------------------------------------
#Valores de rich
consola = Console()

#Cantidad de doblones iniciales
doblones = 0

#Dialogos del banquero
dialogo_ban_1 = 'Bienvenido, soy el banquero. ¿En qué puedo servirle?'
dialogo_ban_2 = '¿Cambiar monedas a Doblones? Ya veo... ¿cuánta cantidad?'
dialogo_ban_3 = 'Aquí tiene. Que la suerte le acompañe.'
dialogo_ban_4 = 'Parece que ha pasado algo raro... ¿Podría volver más tarde e intentarlo de nuevo?'

#Imagenes y textos ASCII para simplemente reutilizar código 
banquero_titulo = Fore.YELLOW + '''
______                                        
| ___ \                                       
| |_/ / __ _ _ __   __ _ _   _  ___ _ __ ___  
| ___ \/ _` | '_ \ / _` | | | |/ _ \ '__/ _ \ 
| |_/ / (_| | | | | (_| | |_| |  __/ | | (_) |
\____/ \__,_|_| |_|\__, |\__,_|\___|_|  \___/ 
                      | |                     
                      |_|                     
''' + Fore.RESET
gato_banquero = '''                                                      
                      ▓▓▒▒▓░                                        ░▒▓▓▒                    
                      ▓▓▒▒▒▓▓▓░                                  ░▓▓▓▓▒▓▓                    
                      ▒▒▒▒▒▒▒▓▓▓                               ▒▓▓▓▒▒▒▒▓▒                    
                      ▒▒▒▒▒▒▒▒▒▓▓▓          ░▒▒░             ░▓▓▒▒▓▓▓▓▓▓                     
                      ▒▓▒▒▒▒▒▒▒▒▓▓▓▓░▒▓████████████████▓▒▒▒▒▓▓▓▒▒▒▒▒▓▓▓▒                     
                       ▒▒▒▒▒▒▒▒▒▒▓▓██▓███████████████████▓▓▓▓▓▒▒░░░░▒▒▒                      
                       ░▒▒▒▒▒▒▒▒▒░▒▓▓██████████████████████▓▒▒▒▒░░░░░░                       
                        ░░▒▒▓▓█▓▓▒▒▓▓█████████████████████▓▒▒░▒▒▒▒░░░░                       
                         ▒▓▓▓▓▒▒▒▓▓▓▓▓▓██████▓████▓█████▓▓▓█▓▒░▒▒▒▓▓▒                        
                         ░░░░░▒▒▒▓▓▓▓██▓██▓▓█▓████████████▓▓▓▓▒░░░░░                         
                         ▒█▓▓▓▓▓█▓▓▓▓▓▓▓██▓▒▓▓██▓▓██▓▓██▓▓██▓█▓▓▒▓██                         
                          ██▓█▓▓█▓▓▓▓█▓▒██▒▒▒▓▓▒▒▒██▒▒██▓▓██▓▓█▓▓▓▓▓                         
                          ▒▓█▓▓▓▓▒░▒▒▓▓▒▓▒▒▒▓▒░░░▒▓▓▒▒▓█▒▒▓▓▒▒▓█▓▓▓░                         
                          ▒██████▓███████▒░░▒▒░  ░▒▓▒░░▓█████▓▓█▓▓▓▒                         
                           ████▓▒░▒▓███████░░░░   ░░ ▒█████▓█░░▓███░                         
                           ██████▒ ░▓▓█▓▓██▒░░░   ░ ░█▒▓██▓█░ ░▓███                          
                           ████▓▓▓██▓░░░ ░▓█░░░   ░░▓▓  ░░░░▒▓▓▓▒█▒                          
                          ░███▓███▓▓▓▓▓▒░░▓▓▒░     ░▓▓░░▓▓▓▒▓▓▓▒▒█░                          
                          ░███▓██████▓▒▒▒▒▒▒░       ░░▒▒▒▓█▓▓▓▓▓▓▓                           
                           ▓██████▓▓▒▒▒░░   ░          ░░▒▒██████▓                           
                           ▒▓███▓▓▒▒░░▒▒░   ░          ▒▒░░░░░▒▓▒░                           
                            ▒▓▓███▓▒░░░      ▒░   ░      ░░░▒▓▒▒▒                            
                             ░░░░▒▓▒▒░░        ▒▒        ░▒▒░░▒░                             
                                   ░░▒░       ░▓░                                            
                                  ░░░░░▒▒░░░░░   ░░░░░                                       
                           ░      ░░░░▒▒▒▓▒▒░     ░░░         ▒                              
                          █░         ░░░░▒▒▒▒▒▒▒░░░           ██                             
                         ██                 ░░░               ███▒                           
                      ░████                                   █████▒                         
                  ░████████                                  ░█████████▓                     
              ▓████████████░                                 ▒█████████████▓                 
         ▒█████████████████▓                                 ██████████████████▓░            
   ░████████████████████████░                               ▓████████████████████████        
████████████████████████████▓                              ░█████████████████████████████▓   
█████████████████████████████                              ██████████████████████████████████
█████████████████████████████▒                            ░██████████████████████████████████
██████████████████████████████           ░▒▒░▓▒           ▓██████████████████████████████████
██████████████████████████████░        ▒█████████        ░███████████████████████████████████
██████████████████████████████▓       ████████████▒      ▓███████████████████████████████████
███████████████████████████████     ▒██████████████▓     ████████████████████████████████████
███████████████████████████████░     ▒▓██████████░ ░░   ▓████████████████████████████████████
███████████████████████████████▓       ░███████▓        █████████████████████████████████████
'''
#El anuncio del banquero
def Introduccion_Ban():
    print (banquero_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (banquero_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (banquero_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (banquero_titulo)
    time.sleep(2)
    os.system('cls')
    #Uso la consola para los diálogos
    consola.print(gato_banquero)
    consola.print(Panel(dialogo_ban_1, border_style="white", box=HEAVY))
    time.sleep(3)
    os.system('cls')
    consola.print(gato_banquero)
    consola.print(Panel(dialogo_ban_2, border_style="white", box=HEAVY))

#Comprobar el dinero ingresado
def Comprobacion(cantidad):
    #Esto es para modificar la cantidad de los doblones fuera del propio módulo
    global doblones
    #Aquí ya no uso la consola y haré las comprobaciones de paso 
    if cantidad.isdigit():
        doblones += int(cantidad) #Añado los doblones
        consola.print(gato_banquero)
        consola.print(Panel(dialogo_ban_3, border_style="white", box=HEAVY))
        input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
    else:
        consola.print(gato_banquero)
        consola.print(Panel(dialogo_ban_4, border_style="white", box=HEAVY))
        input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)

#Método para apostar
def Apostar(doblones_apuesta):
    #Esto es para modificar la cantidad de los doblones fuera del propio módulo
    global doblones
    #Se comprueba que no haya un error
    if doblones_apuesta < doblones:
        print (Fore.LIGHTGREEN_EX + 'Vaya, parece que hubo un error en la apuesta... ¿tal vez apostastes más de lo que tienes?' + Fore.RESET)

#Cuando ganas la apuesta
def Ganar():
    #Esto es para modificar la cantidad de los doblones fuera del propio módulo
    global doblones
    #Se multiplican los doblones apostados
    doblones += Apostar.doblones_apuesta * 2
    return doblones

#Cuando pierdes la apuesta
def Perder():
    #Esto es para modificar la cantidad de los doblones fuera del propio módulo
    global doblones
    #Se restan los doblones
    doblones -= Apostar.doblones_apuesta
    return doblones