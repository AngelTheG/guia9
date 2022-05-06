from fighter import Fighter

class Warrior(Fighter):
    
    def __init__(self):
        super().__init__()
        self.__vulnerable = False
        self.__health = 90

        #Colores para el estetico de la consola
        self.PRPL = '\033[95m'
        self.BLUE = '\033[94m'
        self.GREN = '\033[92m'
        self.GOLD = '\033[93m'
        self.BRED = '\033[91m'
        self.DFLT = '\033[0m'
    
    def getHealth(self):
        return self.__health

    def toString(self):
        print("\nUn luchador desde que tiene conciencia, su fuerza es capaz de destrozar")
        print("mundos y su voluntad de mover montañas\n")
        print("Vida 150    Daño Ataque 6")
        print("            Si su rival está vulnerable su daño será 10")

    def isVulnerable(self):
        return self.__vulnerable

    def takeDamage(self, damage):
        print("EL GUERRERO recibió ",damage," puntos de DAÑO")
        self.__health = self.__health - damage

    def attack(self, target):
        if target.isVulnerable():
            target.takeDamage(10)
        else:
            target.takeDamage(6)

