def affiche(text:str):
    print(f"texte afficher: {text}")
    return



class velo:
    def __init__(self,marque, taille_pneu,couleur,nb_vitesses ):
        self.marque=marque
        self.taille_pneu=taille_pneu
        self.couleur=couleur
        self.nb_vitesses=nb_vitesses
        self.vitesse_courante=1

    def gear_up(self):
        if self.vitesse_courante <self.nb_vitesses:
            self.vitesse_courante +=1
        print(f"vitesse courante: {self.vitesse_courante}")
        return self.vitesse_courante

    def gear_down(self):
        if self.vitesse_courante > 1:
            self.vitesse_courante -= 1
        print(f"vitesse courante: {self.vitesse_courante}")
        return self.vitesse_courante

str1="azertyuiop"
affiche(str1)

v1= velo("decatlon", 28,"noir", 5)
v1.gear_up()
v1.gear_down()