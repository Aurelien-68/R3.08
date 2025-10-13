class Personnage:
    def __init__(self, pseudo: str, niveau: int = 1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        if niveau == 1:
            self.__pv = 1
            self.__initiative = 1
        else:
            self.__pv = niveau
            self.__initiative = niveau

    def __str__(self):
        return f"Le personnage {self.__pseudo} de niveau {self.__niveau} a {self.__pv} PVs et {self.__initiative} d'initiative"

    def degats(self) -> int:
        return self.__niveau

    def attaque(self, autre: 'Personnage') -> None:
        print(f"\n{self.__pseudo} attaque {autre.get_pseudo()} !")
        if self.__initiative > autre.get_initiative():
            print(f"{self.__pseudo} attaque en premier")
            autre.set_pv(autre.get_pv() - self.degats())
            if autre.get_pv() > 0:
                self.__pv -= autre.degats()
        elif self.__initiative < autre.get_initiative():
            print(f"{autre.get_pseudo()} attaque en premier")
            self.__pv -= autre.degats()
            if self.__pv > 0:
                autre.set_pv(autre.get_pv() - self.degats())
        else:
            print("Les deux ont la même initiative, ils frappent en même temps")
            self.__pv -= autre.degats()
            autre.set_pv(autre.get_pv() - self.degats())

    def combat(self, autre: 'Personnage') -> None:
        print(f"{self.__pseudo} et {autre.get_pseudo()} se battent jusqu’à la mort !")
        while self.__pv > 0 and autre.get_pv() > 0:
            self.attaque(autre)
            print(f"{self.__pseudo} ==> {self.__pv} PV")
            print(f"{autre.get_pseudo()} ==> {autre.get_pv()} PV")
        if self.__pv > 0:
            print(f"!!! {self.__pseudo} a gagné !!!")
        else:
            print(f"!!! {autre.get_pseudo()} a gagné !!!")

    def soigner(self) -> None:
        self.__pv = self.__niveau
        print(f"{self.__pseudo} s'est soigné et a désormais {self.__pv} PVs")

    # Getters
    def get_pseudo(self) -> str:
        return self.__pseudo

    def get_niveau(self) -> int:
        return self.__niveau

    def get_pv(self) -> int:
        return self.__pv

    def get_initiative(self) -> int:
        return self.__initiative

    # Setters
    def set_pseudo(self, pseudo: str):
        self.__pseudo = pseudo

    def set_niveau(self, niveau: int):
        self.__niveau = niveau

    def set_pv(self, pv: int) :
        self.__pv = max(pv, 0)  # PV ne peut pas être négatif

    def set_initiative(self, initiative: int):
        self.__initiative = initiative


class Guerrier(Personnage):
    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.set_pv(niveau * 8 + 4)
        self.set_initiative(niveau * 4 + 6)

    def degats(self) -> int:
        return self.get_niveau() * 2


class Mage(Personnage):
    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.set_pv(niveau * 5 + 10)
        self.set_initiative(niveau * 6 + 4)
        self.__mana = niveau * 5

    def degats(self) -> int:
        if self.__mana >= 4:
            self.__mana -= 4
            return self.get_niveau() + 3
        else:
            return self.get_niveau()

    # Getter et setter pour mana
    def get_mana(self) -> int:
        return self.__mana

    def set_mana(self, mana: int):
        self.__mana = mana

class Joueur:
    def __init__(self, nom: str, max_perso:int):
        self.__nom=nom
        self.__max_perso=max_perso
        self.__personnages: list(Personnage)=[]

    #getteur
    def get_nom(self):
        return self.__nom
    def get_max_perso(self):
        return self.__max_perso
    def get_personnages(self):
        return self.__personnages

    #setteur
    def set_nom(self, nom:str):
        self.__nom= nom
    def set_max_perso(self, max_perso:int):
        self.__max_perso=max_perso

    def ajout_perso(self, perso:Personnage):
        self.__personnages.append(perso)


    def get_par_num(self, num:int):
        return self.__personnages[num]

    def get_par_pseudo(self,pseudo:str):
        for perso in self.__personnages:
            if perso.get_pseudo() == pseudo:
                return perso
            return None




if __name__ == "__main__":
    g1 = Guerrier("Guerrier", 5)
    m1 = Mage("Mage", 5)

    print(g1)
    print(m1)

    g1.combat(m1)

    g1.soigner()
    m1.soigner()

    print(g1)
    print(m1)
