#Casino El Minino - Blackjack ------------------------------------------------------------------------------------------------------------
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
dialogo_1 = 'Bienvenido al BlackJack, un juego de cartas. En este juego, tu objetivo es conseguir llegar a la cantidad de 21 o superar la cantidad de cartas que tenga el Crupier.'
dialogo_2 = 'Yo seré el Crupier en esta velada, ¿cuánto desea apostar? (Tiene que ser más de 50 doblones)'
dialogo_3 = 'Ya veo... perfecto entonces, empecemos el juego.'
dialogo_4 = '¡Vaya! Mucho me temo que no tienes la cantidad que deseas apostar en Doblones... ¿Porqué no vas al banquero a conseguir más y luego vuelves?'
dialogo_ganar = 'Felicidades, parece que ganaste. Aquí tienes tu recompensa.'
dialogo_perder = 'Parece que perdiste... bueno, si sigues teniendo Doblones, no importa tanto, ¿no?'

#Imágenes ascii a usar y título
blackjack_titulo = Fore.MAGENTA + '''
,-----.  ,--.              ,--.      ,--.              ,--.     
|  |) /_ |  | ,--,--. ,---.|  |,-.   `--' ,--,--. ,---.|  |,-.  
|  .-.  \|  |' ,-.  || .--'|     /   ,--.' ,-.  || .--'|     /  
|  '--' /|  |\ '-'  |\ `--.|  \  \   |  |\ '-'  |\ `--.|  \  \  
`------' `--' `--`--' `---'`--'`--'.-'  / `--`--' `---'`--'`--' 
                                   '---'                        
''' + Fore.RESET
gato_trajeado = '''                                                        
                                ░▓▓▒                                                    
                               ▒█▓▓▒▓▓                                                  
                              ▒█▓▓▓▓▓▓█░                                                
                              ███▓▓▓▓███▓                                               
                              ████▓▓▓█████                                              
                              ▓██▓▓▓▓▓████▓▒                       ▒▓▓▓▓▓               
                             ▒▓▓▓▓▓▒▓▓███████▓░                ░███▓▓▓▓█▓               
                             ░▒███▓▒▒▒▓████▓██▓▓░░           ▒█████▓█▓▓█                
                              ▒▓█▒▓███▓▓█▓▓▓▓▓▓▒░░       ░░▒▒▓▓█████▓▓█                 
                             ▒▓██▓▓▓██▓▓▓▓▓█▓█▓▓▒▒        ░▒▓▓█▓▓▓█▓▓▓                  
                            ░▒██▓▓▓▓▓▓▒▒▓▓▓▒▒▒▓▓█▒░▒░░▒░  ░░▓▓▓▓▓▓▓▓▓                   
                             ░▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▒▒▒▒▒▒▒░░▒▓▒▒▒▓▒▒▒░                    
                            ░▒▒▒▒▓▓▓█▓▓▓▓█████▓▒▓▒▒▓▓██▒░ ▒░▒░░▒▒▒░                     
                            ░░░░░▒▒▓▓▓▓▓█▓ ███████████▓▒░░▒░░▒▒▒▒▒                      
                           ░░░ ░▒▒▓▓▒▓▓▒▓░░▓▒▒█▓▓█████▓█▓█▓▓▓▓▒░░▒░                     
                          ░░▒░░░▒▒▒▒▓▓▓▓▒▒░░▒██▒▓▓██▓██▓▓██████▓▒▒░                     
                          ░▒▒▓░░▒▒▒▒▓████▓░░░░░▒░ ░░ ░▒░█░▒▒░░█▒▓▒░                     
                          ░▒▓▒▒▓▒▓▓▓▓▓▓███▓░░▒▒▓▒▒▒░░░ ░░▒▒▒▒▓▒▒▒░░                     
                         ░░▒▓▒▓▓█▓▓▓▓▒▓▓▓█▓▒░▒▓▓▓▒░ ░ ░  ░░▒▒▓▓▓▒░░                     
                          ░▒▓▓█▓████▓▒▒▓██▓▒░░░▒▓█████   ▒▓▓█▓▓▒░                       
                         ░░▒▒▓▓█▓▓██▒▒▓▓█▓▒▓▒▒░▒░ ███░    ▒▒▓▒░                         
                          ░░░▒▒▒▓██▓▓░▓▓▓▓▓▓▓▓░  ░▒█      ▒▓▒ ░▒░                       
                         ░▒▒▒▒▒▒▒▓█▓▓▓▒▒▓▓▓▓▓▓▒▒▒▓██░░  ░  ░ ▒▓░                        
                 ▒███████████▓▓▒▒▒▓▓▓█████▓▓▓▓██████▓▒░▒░  ░▒░░                         
             █████████████████████▓▓▓████████████████▓▒▒░░▓▓▓▒░                         
             ████████████████████████░▒▓▓████▓▓▓▓▒▓▓▓▓▓▓█▓▓▒▒▓███▓░                     
             ████████████████████████▒   ██  ░▓█▓▓▓▒▓▓▒▒▓▒▒▓▓███████                    
            ░█████████████████████████░ ██████▓▓██ ▒▓███████████████▓                   
             ████████████████████████████████░  █████████████████████                   
             ████████████████████████████████   █████████████████████                   
             █████████████████████████████████  █████████████████████                   
             █████████████████████████████████▒░█████████████████████                   
            ██████████████████████████████████▓██████████████████████                   
            ██████████████████████████████████████████████████████████                  
             █████████████████████████████████████████████████████████░                 
             ██████████████████████████████████████████████████████████                 
             ███████████████████████████████████████████████████████████                
             ███████████████████████████████████████████████████████████▒               
             ████████████████████████████████████████████████████████████               
             ▓██████████████████████████████████████▓▒▒▒▒▒▒▓▓▒▒▒▓▓▓▓▓████▓              
              ███████████████████████████████████████   ░░▒▓████▓▒▒▒▓▓████              
              ███████████████████████████████████████░  ░▒▓▓▓██▓█▓▓▒▒▒▓███▓             
               ██████████████████████████████████████▓   ▒▒▒▒▒▓▓▓▓▒▓▒░▓████             
               ███████████████████████████████████████   ░▒░░▒▒▒▓▓██▓██████▓            
               ▒██████████████████████████████████████ ░▒██████████████████▓            
                ███████████████████████████████████████████████████████████░            
                ░██████████████████████████████████████████████████████████             
                 ▓█████████████████████████████████████████████████████████             
                 ░███████████████████████████████████████████████████████▓              
                 ████████████████████████████████████████████████████                   
                ███████████████████████████████████████████████▓░                       
               ░██████████████████████████████████████████████▓                         
               ▓███████████████████████████████████████████████                         
               ████████████████████████████████████████████████▒                        
               █████████████████████████████████████████████████                                                 
'''

#Consola
consola = Console()

#Clases ----------------------------------------------------------------------------------------------------------------------------------
#Clase para introducir al Crupier
def Introduccion():
    print (blackjack_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (blackjack_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (blackjack_titulo)
    time.sleep(0.2)
    os.system('cls')
    time.sleep(0.3)
    print (blackjack_titulo)
    time.sleep(2)
    os.system('cls')
    consola.print(gato_trajeado)
    consola.print(Panel(dialogo_1, border_style="white", box=HEAVY))
    time.sleep(5)
    os.system('cls')
    consola.print(gato_trajeado)
    consola.print(Panel(dialogo_2, border_style="white", box=HEAVY))
    
#Clase para aceptar
def Aceptar():
    if betabanquero.doblones >= 50 : #Si tiene doblones se le deja jugar
        consola.print(gato_trajeado)
        consola.print(Panel(dialogo_3, border_style="white", box=HEAVY))
        time.sleep(3)
        os.system('cls')
        return True 
    else:
        return False

#Clase para rechazar
def Rechazar():
    if betabanquero.doblones <= 50: #Si no tiene doblones no se le deja jugar
        os.system('cls')
        consola.print(gato_trajeado)
        consola.print(Panel(dialogo_4, border_style="white", box=HEAVY))
        input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
        os.system('cls')
        return True 
    else:
        return False

#Clase para valores de las cartas
def Valores_Cartas(mano):
    #Valores
    valores = {
 '''
 -------
|2      |
|       |
|       |
|       |
|      2|
 ------- ''': 2,
'''
 -------
|3      |
|       |
|       |
|       |
|      3|
 ------- ''': 3, 
'''
 -------
|4      |
|       |
|       |
|       |
|      4|
 ------- ''': 4,
'''
 -------
|5      |
|       |
|       |
|       |
|      5|
 ------- ''': 5,
'''
 -------
|6      |
|       |
|       |
|       |
|      6|
 ------- ''': 6,
'''
 -------
|7      |
|       |
|       |
|       |
|      7|
 ------- ''': 7,
'''
 -------
|8      |
|       |
|       |
|       |
|      8|
 ------- ''': 8, 
'''
 -------
|9      |
|       |
|       |
|       |
|      9|
 ------- ''': 9,
'''
 -------
|10     |
|       |
|       |
|       |
|     10|
 ------- ''': 10,
''' 
 -------
|J      |
|       |
|       |
|       |
|      J|
 ------- ''': 10, 
'''
 -------
|Q      |
|       |
|       |
|       |
|      Q|
 ------- ''': 10, 
'''
 -------
|K      |
|       |
|       |
|       |
|      K|
 ------- ''': 10
    }
    total = 0 #Valor para devolver
    #Hago un bucle for
    for carta in mano:
        total += valores[carta] #Se le suma una carta de valores al total
        #Abro bucle por si sale el As
        if carta == ''' 
                        -------
                        |A      |
                        |       |
                        |       |
                        |       |
                        |      A|
                        ------- ''':
            opcion = input ('¿Qué valor tiene el As de 1 o 11?: ')
            #Si el usuario dice 1, se le da uno
            if opcion == '1':
                print ('Se le dió el valor de uno')
                total +=1
            #Si el usuario dice 11, se le da 11
            elif opcion == '11':
                print ('Se le dió el valor de once')
                total +=11
            else: #Foolproof
                print ('Solo se puede elegir números como el uno o el once.')
    return total #Devuelve el total

#Clase para jugar
def Jugar():
    doblones_apuesta = int(input('Apuesta: '))
    betabanquero.Apostar(doblones_apuesta)
    #Listas
    mazo = ['''
                 -------
                |K      |
                |       |
                |       |
                |       |
                |      K|
                 ------- ''', '''
                 -------
                |Q      |
                |       |
                |       |
                |       |
                |      Q|
                 ------- ''', ''' 
                 -------
                |J      |
                |       |
                |       |
                |       |
                |      J|
                 ------- ''', '''
                 -------
                |10     |
                |       |
                |       |
                |       |
                |     10|
                 ------- ''', '''
                 -------
                |9      |
                |       |
                |       |
                |       |
                |      9|
                 ------- ''', '''
                 -------
                |8      |
                |       |
                |       |
                |       |
                |      8|
                 ------- ''', '''
                 -------
                |7      |
                |       |
                |       |
                |       |
                |      7|
                 ------- ''', '''
                 -------
                |6      |
                |       |
                |       |
                |       |
                |      6|
                 ------- ''', '''
                 -------
                |5      |
                |       |
                |       |
                |       |
                |      5|
                 ------- ''', '''
                 -------
                |6      |
                |       |
                |       |
                |       |
                |      6|
                 ------- ''', '''
                 -------
                |5      |
                |       |
                |       |
                |       |
                |      5|
                 ------- ''', '''
                 -------
                |4      |
                |       |
                |       |
                |       |
                |      4|
                 ------- ''', '''
                 -------
                |3      |
                |       |
                |       |
                |       |
                |      3|
                 ------- ''', '''
                 -------
                |2      |
                |       |
                |       |
                |       |
                |      2|
                 ------- ''', ''' 
                 -------
                |A      |
                |       |
                |       |
                |       |
                |      A|
                 ------- '''
                ]
    #Hago un shuffle del mazo y así genero distintos valores tanto para el crupier como para el jugador
    random.shuffle(mazo)

    #Hago un pop para sacar los valores
    jugador = [mazo.pop(), mazo.pop()]
    crupier = [mazo.pop(), mazo.pop()]

    #Muestro la mano de cada e indico los valores
    print (f'Tu mano tiene {jugador}')
    print (f'El valor de tu mano es {Valores_Cartas(jugador)}')
    print (f'El crupier tiene {crupier[0]}')
    print (f'El valor de la mano del crupier es desconocido de momento')

    #Bucle para el juego
    while True:
        #Para que el jugador coja otra carta
        print ('¿Quieres cojer otra carta o pasar? (C/P)')
        ent = input ()
        #Se abre condicional
        #Si coje otra carta
        if ent.lower() == 'c':
            print (f'Cojiste otra carta')
            carta_ran = random.shuffle(mazo) #Se vuelve a barajar el mazo
            jugador.append(mazo.pop()) #Se añade la carta
            print (f'Tus cartas ahora son {jugador}')
            print (f'El valor de tu mano es {Valores_Cartas(jugador)}') #Se vuelve a calcular el valor
            print (f'El crupier tiene {crupier[0]}')
        #Si no, acaba el juego
        elif ent.lower() == 'p':
            print ('El juego acabo...')
            if Valores_Cartas(jugador) > 21: #Ha perdido si tiene menos de lo apostado
                os.system('cls')
                consola.print(gato_trajeado)
                consola.print(Panel(dialogo_perder, border_style="white", box=HEAVY))
                print (Fore.LIGHTGREEN_EX + f'Resultado del jugador: {Valores_Cartas(jugador)}' + Fore.RESET)
                print (Fore.LIGHTGREEN_EX + f'Resultado del jugador: {Valores_Cartas(crupier)}' + Fore.RESET)
                betabanquero.Perder()
                input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
                os.system('cls')
                break
            elif Valores_Cartas(jugador) == 21: #Y también para si el jugador tiene el valor 21, ganando
                os.system('cls')
                consola.print(gato_trajeado)
                consola.print(Panel(dialogo_ganar, border_style="white", box=HEAVY))
                print (Fore.LIGHTGREEN_EX + f'Resultado del jugador: {Valores_Cartas(jugador)}' + Fore.RESET)
                print (Fore.LIGHTGREEN_EX + f'Resultado del jugador: {Valores_Cartas(crupier)}' + Fore.RESET)
                input (Fore.LIGHTGREEN_EX + 'Presione ENTER para volver al menú una vez haya acabado...' + Fore.RESET)
                betabanquero.Ganar()
                os.system('cls')
                break