#Módulos ---------------------------------------------------------------------------------------------------------------------------------
import os
from colorama import *
import time
import random
#Clases ----------------------------------------------------------------------------------------------------------------------------------
#Clase de Tragaperras
class Tragaperras():
    #Inicializadores
    def __init__(self):
        #Lista de combinaciones
        self.combinaciones = ['777','111','222','999','771','711','171','117','912']
    #Método de combinaciones
    def Combinaciones(self):
        #Uso del shuffle en random para hacer variar las combinaciones
        for _ in range(5):
            random.shuffle(self.combinaciones)
            print(self.combinaciones)
            time.sleep(1)
            os.system('cls')
        #Se abre el bucle para leer la lista
        for i in self.combinaciones:
            #Condicional
            #Si es una de las siguiebtes opciones se gana
            if i == '777' or i == '111' or i == '222' or i == '999':
                print (i)
                print ('Ganaste')
                break
            #Si no se pierde
            else:
                print (i)
                print('Perdiste')
                break
            
#Clase de Ruleta
class Ruleta():
    #Inicializador
    def __init__(self):
        #Las listas con los valores
        self.colores = ['negro','rojo']
        self.numeros = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13, 1, 00, 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]
    #Método para apuestas
    def Apuesta(self, opcion):
        
        #Abro condicional
        #Si el usuario escoje color
        if opcion.lower() == 'color':
            color = input ('¿Qué color?:')
            #Abro condicional para cada color
            if color.lower() == 'negro':
                #Otro condicional
                #Si acierta el color del random shuffle
                if color.lower() == random.shuffle(self.colores):
                    print ('Ganaste')
                    print ('Cayó en negro')
                #Si no lo acierta
                else:
                    print ('Perdiste')
                    print ('Cayo en rojo')
            elif color.lower() == 'rojo':
                #Si acierta el color del random shuffle
                if color.lower() == random.shuffle(self.colores):
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
            random.shuffle(self.numeros)
            #Abro bucle
            for i in self.numeros:
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

#Clase de Blackjack
class Blackjack():
    #Inicializador
    def __init__(self,total):
        self.mazo = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.valores = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 10, 'Q': 10, 'K': 10
    }
        self.total = total
    #Método para calcular el valor de las cartas
    def Valores_Cartas(self, mano):
        total = 0 #Valor para devolver
        #Hago un bucle for
        for carta in mano:
            total += self.valores[carta] #Se le suma una carta de valores al total
            #Abro bucle por si sale el As
            if carta == 'A':
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
        return total
    #Método para repartir las cartas
    def Repartir(self):
        return random.shuffle(self.mazo)
    #Ahora ya si, método para jugar
    def Jugar(self):
        #Hago un pop para sacar los valores
        jugador = [self.mazo.pop(), self.mazo.pop()]
        crupier = [self.mazo.pop(), self.mazo.pop()]

        #Muestro la mano de cada e indico los valores
        print (f'Tu mano tiene {jugador}')
        print (f'El valor de tu mano es {self.Valores_Cartas(jugador)}')
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
                carta_ran = random.shuffle(self.mazo) #Se vuelve a barajar el mazo
                jugador.append(self.mazo.pop()) #Se añade la carta
                print (f'Tus cartas ahora son {jugador}')
                print (f'El valor de tu mano es {self.Valores_Cartas(jugador)}') #Se vuelve a calcular el valor
                print (f'El crupier tiene {crupier[0]}')
            #Si no, acaba el juego
            elif ent.lower() == 'p':
                print ('El juego acabo...')
                #Se abre otra condicional
                #Si el crupier tiene un valor mayor gana el
                if self.Valores_Cartas(crupier) > self.Valores_Cartas(jugador):
                    print('¡Ganó el Crupier! Tenía más cartas')
                    print (f'El crupier tiene {crupier}')
                    print (f'El valor de la mano del crupier era {self.Valores_Cartas(crupier)}')
                    break
                #Si el jugador tiene un valor mayor que el crupier gana el jugador
                elif self.Valores_Cartas(crupier) < self.Valores_Cartas(jugador):
                    print ('¡Ganaste!')
                    print (f'El crupier tiene {crupier}')
                    print (f'El valor de la mano del crupier era {self.Valores_Cartas(crupier)}')
                    break
            #Si el valor de las cartas del jugador es mayor de 21, el bucle se para y el jugado pierde
            if self.Valores_Cartas(jugador) > 21:
                print ('Superaste 21, perdiste')
                break
            elif self.Valores_Cartas(jugador) == 21: #Y también para si el jugador tiene el valor 21, ganando
                print ('Ganaste')
                break
#Clase de Gacha
class Gacha():
    #Inicializador
    def __init__(self):
        self.personajes = ['Daniel','José','Damián','Pablo','Jorge','Ariadna']
        self.valores = {'Daniel':'5 estrellas','José':'4 estrellas','Damián':'4 estrellas','Pablo':'3 estrellas','Jorge':'3 estrellas','Ariadna':'3 estrellas'}
    #Método para tirar por un personas
    def Tirada(self):
        random.shuffle(self.personajes)
        elegido = self.personajes[0]  # elige uno aleatorio tras mezclar
        rareza = self.valores[elegido]
        print(f'Te tocó {elegido}, que es de {rareza}')
#Programa --------------------------------------------------------------------------------------------------------------------------------
#Valores para cada clase
tragaperras = Tragaperras()
ruleta = Ruleta()
blackjack = Blackjack(0)
gacha = Gacha()
while True:
    print (Fore.RED + 'Menú Casino' + Fore.RESET)
    print ('1.Tragaperras')
    print ('2.Ruleta')
    print ('3.BlackJack')
    print ('4.Gacha')
    print ('5.Salir')
    elegir = input('Opción: ')
    if elegir == '1':
        os.system('cls')
        print ('Tragaperras')
        tragaperras.Combinaciones()
        input()
        os.system('cls')
    elif elegir == '2':
        os.system('cls')
        print ('Ruleta')
        print ('Puedes apostar por color o número (num)')
        opcion = input ('¿Qué tipo de apuestas quieres hacer?:')
        ruleta.Apuesta(opcion)
        input()
        os.system('cls')
    elif elegir == '3':
        os.system('cls')
        print ('BlackJack')
        blackjack.Jugar()
        input()
        os.system('cls')
    elif elegir == '4':
        os.system('cls')
        print ('Gacha')
        gacha.Tirada()
        input()
        os.system('cls')
    elif elegir == '5':
        break
    else:
        os.system('cls')
        print ('La opción escogida no se encuentra disponible o no es correcta')
        input ('Pulse ENTER para volver al menú')
        os.system('cls')

#Fin del programa
input()