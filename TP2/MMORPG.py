class Personnage():
    def __init__(self,pseudo:str,niveau:int=1):
        self.pseudo=pseudo
        self.niveau=niveau
        #constructeur pour le niveau 1: pv=1 initiative=1
        if niveau==1:
            self.pv=1
            self.initiative=1
        else:
            self.pv=niveau
            self.initiative=niveau

    def __str__(self):
        return f"Le personnage {self.pseudo} de niveau {self.niveau} a {self.pv} PVs et {self.initiative} d'initiative"

    def degats(self):
        """Renvoie le nombre de dégâts infligés (règle de base : dégâts = niveau)"""
        return self.niveau

    def attaque(self, autre: 'Personnage') -> None:
        print(f"\n{self.pseudo} attaque {autre.pseudo} !")
        if self.initiative > autre.initiative:
            print(f"{self.pseudo} attaque en premier")
            autre.pv-= self.degats()
            if autre.pv >0:
                self.pv-=autre.degats()
        elif self.initiative < autre.initiative:
            print(f"{autre.pseudo} attaque en premier")
            self.pv-=autre.degats()
            if self.pv>0:
                autre.pv-=self.degats()
        else:
            print("Les deux ont la même initiative, ils frappent en même temps")
            self.pv -= autre.degats()
            autre.pv-= self.degats()

    def combat(self, autre: 'Personnage')->None:
        print(f"{self.pseudo} et {autre.pseudo} se batte jusqu’à ce qu’un des deux soit mort")
        while self.pv >0 and autre.pv>0:
            self.attaque(autre)
            print(f"{self.pseudo} ==> {self.pv} PV")
            print(f"{autre.pseudo} ==> {autre.pv} PV")
        if self.pv>0:
            print(f"!!! {self.pseudo} a gagné !!!")
        else:
            print(f"!!! {autre.pseudo} a gagné !!!")

    def soigner(self) ->None:
        self.pv=self.niveau
        print(f"{self.pseudo} s'est soigner et a desormais {self.pv} PVs")







if __name__ == "__main__":
    p1=Personnage("perso")
    p2=Personnage("persoLVL", 5)
    print(p1)
    print(p2)
    p1.attaque(p2)
    print(p1)
    print(p2)
    p1.soigner()
    print(p1)
    print(p2)
    p1.combat(p2)
    p1.soigner()
    print(p1)
    print(p2)