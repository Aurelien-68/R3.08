class Tasse:
    matière: str = "céramique"

    def __init__(self, couleur: str, contenance: int, marque: str, contenu: str=None):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque
        self.contenu = contenu

    def __str__(self) -> str:
        if self.contenu:
            return f"La tasse de matière {self.matière}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml et contient {self.contenu}."
        else:
            return f"La tasse de matière {self.matière}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml et est vide."

    def definir_contenu(self, contenu: str):
        self.contenu = contenu

    def boire(self):
        if self.contenu:
            self.contenu=None
        else:
            print("La tasse est déjà vide.")

if __name__ =='__main__':

    # Création de plusieurs objets de la classe Tasse
    tasse1 = Tasse("bleue", 250, "Duralex", "coca")
    tasse2 = Tasse("rouge", 350, "IKEA", "eau")

    # Affichage des espace de nommages
    print(vars(tasse1))
    print(vars(Tasse))


    # Affichage des objets avant d'ajouter du contenu
    print(tasse1)
    print(tasse2)

    # Définir le contenu des tasses
    tasse1.definir_contenu("café")
    tasse2.definir_contenu("thé")

    # Affichage après avoir ajouté du contenu
    print(tasse1)
    print(tasse2)

    # Boire le contenu de la tasse
    tasse1.boire()
    print(tasse1)

    # Essayer de boire à nouveau alors que la tasse est déjà vide
    tasse1.boire()
