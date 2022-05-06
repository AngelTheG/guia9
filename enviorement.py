import os
from runner import Runner

class Enviorement():
    def __init__(self):
        self.__defaultRunner = Runner()

        #Colores para el estetico de la consola
        self.PRPL = '\033[95m'
        self.BLUE = '\033[94m'
        self.GREN = '\033[92m'
        self.GOLD = '\033[93m'
        self.BRED = '\033[91m'
        self.DFLT = '\033[0m'


    def menu(self):
        #DEBUG - Limpiar la terminal por cada vez que se muestre el menú en pantalla
        os.system ("clear")

        while True:

            #WARRIORS
            print(self.BRED)
            print("   █     █░ ▄▄▄       ██▀███   ██▀███   ██▓ ▒█████   ██▀███    ██████ ")
            print("  ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓██ ▒ ██▒▓██▒▒██▒  ██▒▓██ ▒ ██▒▒██    ▒ ")
            print("  ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██▒▒██░  ██▒▓██ ░▄█ ▒░ ▓██▄   ")
            print("  ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒██▀▀█▄  ░██░▒██   ██░▒██▀▀█▄    ▒   ██▒")
            print("  ░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░██▓ ▒██▒░██░░ ████▓▒░░██▓ ▒██▒▒██████▒▒")
            print("  ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░▓  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░")
            print("    ▒ ░ ░    ▒   ▒▒ ",self.DFLT," _______  _        ______",self.BRED,"  ▒ ▒░   ░▒ ░ ▒░░ ░▒  ░ ░")
            print("    ░   ░    ░   ▒  ",self.DFLT,"(  ___  )( (    /|(  __  \ ",self.BRED,"░ ▒    ░░   ░ ░  ░  ░  ")
            print("      ░          ░  ",self.DFLT,"| (   ) ||  \  ( || (  \  ) ",self.BRED," ░     ░           ░  ")#
            print("                    ",self.DFLT,"|  ___  || (\ \) || |   | |")
            print("                      | (   ) || | \   || |   ) |")
            print("                      | )   ( || )  \  || (__/  )")
            print("                      |/     \||/    )_)(______/ ")
            print(self.BLUE,"          ██     ██ ██ ███████  █████  ██████  ██████  ███████ ")#
            print("          ██     ██ ██    ███  ██   ██ ██   ██ ██   ██ ██      ")
            print("          ██  █  ██ ██   ███   ███████ ██████  ██   ██ ███████ ")
            print("          ██ ███ ██ ██  ███    ██   ██ ██   ██ ██   ██      ██ ")
            print("           ███ ███  ██ ███████ ██   ██ ██   ██ ██████  ███████ ")


            #Opciones
            print(self.DFLT,"")
            print("                             [ 1 ] Jugar")
            print("                             [ 0 ] Salir",self.GOLD)

            mainMenuChoice = int(input("                           Elija su destino\n                                 >"))
            
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
                print(self.BRED,"\nBusca tu camino a casa...\n\n")
                break