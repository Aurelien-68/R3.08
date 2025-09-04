def plus_grand(a: float, b: float) -> float:
    """
    Retourne le plus grand des deux nombres réels a et b.
    """
    print(max(a, b))
    return max(a, b)

def superieur_a_seuil(valeur: float, seuil: float = 10) -> bool:
    """
    Vérifie si la valeur passée est supérieure au seuil donné (par défaut 10).
    """
    print(valeur > seuil)
    return valeur > seuil

def plus_grand_liste(valeurs: list[float]) -> float:
    """
    Retourne la plus grande valeur d'une liste de nombres réels.
    """
    print(max(valeurs))
    return max(valeurs)

def nombre_inférieur_a_seuil(valeurs: list[float], seuil: float = 3) -> int:
    """
    Retourne le nombre de valeurs dans la liste inférieures au seuil donné (par défaut 3).
    """
    print(sum(1 for v in valeurs if v < seuil))
    return sum(1 for v in valeurs if v < seuil)

def afficher_dictionnaire(dictionnaire: dict) -> None:
    """
    Affiche l'ensemble des clés et valeurs d'un dictionnaire.
    """
    for cle, valeur in dictionnaire.items():
        print(f"{cle}: {valeur}")


plus_grand(15,55)
superieur_a_seuil(15)
plus_grand_liste([15,2,44,223,12,56,98])
nombre_inférieur_a_seuil([1,3,45,78,2,1,2,0.12,2.22])
afficher_dictionnaire({"nom": "Alice","âge": 30,"ville": "Paris"})