from ast import While
import os

from matplotlib.pyplot import waitforbuttonpress
from warrior import Warrior
from wizard import Wizard

class Runner():
    def __init__(self):
        self.__defaultWizard = Wizard()
        self.__defaultWarrior = Warrior()

    def start(self, mode):
        if mode == 1:
            os.system ("clear")
            print("\nModo seleccionado Jugador vs Jugador\n\n")
            print("Elijan sus luchadores")
            print("[ 0 ] Guerrero")
            print("[ 1 ] Mago")
            
            while True:
                p1Choice = int(input("Jugador 1 > "))
                if p1Choice == 0:
                    self.__defaultWarrior.toString()
                    print("¿Estás seguro que quieres usar al GUERRERO?   (Y/N)")
                    confirmation = input("> ")
                    if confirmation.capitalize() == "Y":
                        os.system ("clear")
                        print("Guerrero (J1) vs Mago (J2)")
                        break

                if p1Choice == 1:
                    self.__defaultWizard.toString()
                    print("¿Estás seguro que quieres usar al MAGO?   (Y/N)")
                    confirmation = input("> ")
                    if confirmation.capitalize() == "Y":
                        os.system ("clear")
                        print("Guerrero (J2) vs Mago (J1)")
                        break

        if mode == 2:
            os.system ("clear")
            print("\nModo seleccionado Jugador vs CPU\n\n")
            print("Elije tu luchador")
            print("[ 0 ] Guerrero")
            print("[ 1 ] Mago")
            
            while True:
                p1Choice = int(input("Jugador > "))
                if p1Choice == 0:
                    self.__defaultWarrior.toString()
                    print("¿Estás seguro que quieres usar al GUERRERO?   (Y/N)")
                    confirmation = input("> ")
                    if confirmation.capitalize() == "Y":
                        os.system ("clear")
                        print("Has elegido la senda del Guerrero")
                        break

                if p1Choice == 1:
                    self.__defaultWizard.toString()
                    print("¿Estás seguro que quieres usar al MAGO?   (Y/N)")
                    confirmation = input("> ")
                    if confirmation.capitalize() == "Y":
                        os.system ("clear")
                        print("Has elegido el conocimiento del Mago")
                        break


        if mode == 3:
            os.system ("clear")
            print("Guerrero (CPU1) vs Mago (CPU2)")

    def run(self,mode):
        os.system ("clear")
        print("EMPIEZA EL JUEGO")


        #Para el modo JcJ
        if mode == 1:
            turnCounter = 0
            while True:
                turnCounter+=1
                print("\n\nTurno ",turnCounter,end="")

                #Turno del mago
                if turnCounter%2 == 0:
                    print(" - Mago")
                    print("Elije tu siguiente jugada")
                    print("Vida del enemigo: ", self.__defaultWarrior.getHealth())
                    print("Tu vida: ",self.__defaultWizard.getHealth())
                    print("[ 1 ] Preparar un Hechizo (x4 Ataque)")
                    print("[ 2 ] Atacar (3 Daño)")
                    turn = int(input(">"))
                    if turn == 1:
                        self.__defaultWizard.prepareSpell()
                    if turn == 2:
                        self.__defaultWizard.attack(self.__defaultWarrior)

                #Turno del guerrero
                else:
                    print(" - Guerrero")
                    print("Elije tu siguiente jugada")
                    print("Vida del enemigo: ", self.__defaultWizard.getHealth())
                    print("Tu vida: ",self.__defaultWarrior.getHealth())
                    print("[ 1 ] Atacar (6 - 10 Daño)")
                    turn = int(input(">"))
                    if turn == 1:
                        self.__defaultWarrior.attack(self.__defaultWizard)

                if self.__defaultWarrior.getHealth() <= 0:
                    print("El GUERRERO ha sido derrotado, el mago se retira en silencio")
                    break

                if self.__defaultWizard.getHealth() <= 0:
                    print("\n\nEl MAGO ha sido derrotado, el guerrero se retira victorioso\n\nFIN DEL JUEGO\n\n")
                    break

                