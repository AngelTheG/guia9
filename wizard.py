from fighter import Fighter


class Wizard(Fighter):
    def __init__(self):
        super().__init__()
        self.__health = 50
        self.__power = 1
        self.__vulnerable = False

    
    def getHealth(self):
        return self.__health

    def toString(self):
        print("\nEs un ser más allá del conocimiento mismo, el destino le es irrelevante")
        print("ya que está por encima del mismísimo tiempo\n")
        print("\nVida 50     Daño Ataque 3")
        print("            Puede preparar su hechizo para aumentar su daño 4 veces por turno")

    def isVulnerable(self):
        return self.__vulnerable

    def prepareSpell(self):
        print("Estas preparando tu hechizo [",4*self.__power,"xDaño")
        self.__vulnerable = True
        self.__power += 1

    def attack(self,target):
        if self.__power > 1:
            finalDamage = self.__power*4*3

        if self.__power == 1:
            finalDamage = 3
        target.takeDamage(finalDamage)
        self.__power = 1
        self.__vulnerable = False

    def takeDamage(self, damage):
        print("Mago recibió ",damage,"puntos de daño")
        self.__health = self.__health - damage