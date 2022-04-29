import os
from runner import Runner

class Enviorement():
    def __init__(self):
        self.__defaultRunner = Runner()


    def menu(self):
        #DEBUG - Limpiar la terminal por cada vez que se muestre el menú en pantalla
        os.system ("clear")

        while True:
            print("Warrior & Wizards")
            print("[ 1 ] Jugar")
            print("[ 0 ] Salir")

            mainMenuChoice = int(input("Elija su destino\n> "))
            
            if mainMenuChoice == 1:
                os.system ("clear")
                print("Elije un modo")
                print("[ 1 ] Jugador vs Jugador")
                #NO DISPONIBLE POR FALTA DE TIEMPO
                #print("[ 2 ] Jugador vs CPU")
                #print("[ 3 ] CPU vs CPU")
                print("[ 0 ] Huir de la lucha")
                modeChoice = int(input("Elije el modo de lucha\n>"))


                self.__defaultRunner.start(modeChoice)


                if modeChoice == 0:
                    os.system ("clear")
                    print("\nVolviendo al menu principal totalmente deshonrado...\n\n")


                if modeChoice != 0:
                    print("Después de inicar no podras detenerte hasta que el combate finalice con la muerte")
                    print("de alguno de los luchadores.")
                    confirmation = input("¿Estás seguro de querer jugar?   (Y/N)\n> ")
                    if confirmation.capitalize() == "Y":
                        #Inicia el combate por turnos
                        self.__defaultRunner.run(modeChoice)


                    if confirmation.capitalize() == "N":
                        os.system ("clear")
                        print("\nLos dioses te observan con desprecio\n\n")
                        break
                                 

            if mainMenuChoice == 0:
                os.system ("clear")
                print("\nBusca tu camino a casa...\n\n")
                break