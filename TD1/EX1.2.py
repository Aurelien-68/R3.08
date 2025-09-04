def plus_grand(a: float, b: float) -> float:
    """
    Retourne le plus grand des deux nombres réels a et b.
    """
    return max(a, b)

def superieur_a_seuil(valeur: float, seuil: float = 10) -> bool:
    """
    Vérifie si la valeur passée est supérieure au seuil donné (par défaut 10).
    """
    return valeur > seuil

def plus_grand_liste(valeurs: list[float]) -> float:
    """
    Retourne la plus grande valeur d'une liste de nombres réels.
    """
    return max(valeurs)

def nombre_inférieur_a_seuil(valeurs: list[float], seuil: float = 3) -> int:
    """
    Retourne le nombre de valeurs dans la liste inférieures au seuil donné (par défaut 3).
    """
    return sum(1 for v in valeurs if v < seuil)

def afficher_dictionnaire(dictionnaire: dict) -> None:
    """
    Affiche l'ensemble des clés et valeurs d'un dictionnaire.
    """
    for cle, valeur in dictionnaire.items():
        print(f"{cle}: {valeur}")