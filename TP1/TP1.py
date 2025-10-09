import math

class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"le point a les coodonées x: {self.__x} et y: {self.__y}"

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def distanceCoord(self, a: float, b: float) -> float:
        """
        Fonction de distance part rapport à un autre point
        :param a: x du point avec qui il faut calculer la distance
        :type a:float
        :param b: y du point avec qui il faut calculer la distance
        :type b: float
        :return: distance separant ce point avec le point donner avec a et b
        :rtype: float
        """
        dx = self.__x - a
        dy = self.__y - b
        return (dx ** 2 + dy ** 2) ** 0.5

    def distancePoint(self, camarade: 'Point') -> float:
        """
        Fonction de distance part rapport à un autre point
        :param camarade: Point avec qui il faut calculer la distance
        :type camarade: Point
        :return: distance separant ce point avec le point donner avec a et b
        :rtype: float
        """
        return self.distanceCoord(camarade.get_x(), camarade.get_y())


class Cercle:
    def __init__(self, rayon: float, centre: Point = Point()):
        self.__rayon = rayon
        self.__centre = centre

    def __str__(self):
        return f"Le cercle a pour rayon: {self.__rayon} et pour centre {self.__centre}"

    def get_rayon(self):
        return self.__rayon

    def get_centre(self):
        return self.__centre

    def diametre(self) -> float:
        """
        Fonction qui calcul le diametre du cercle
        :return: diametre du cercle
        :rtype: float
        """
        return 2 * self.__rayon

    def perimetre(self) -> float:
        """
        Fonction qui calcul le perimetre du cercle
        :return: perimetre du cercle
        :rtype:float
        """
        return 2 * math.pi * self.__rayon

    def surface(self) -> float:
        """
        Fonction qui renvoie la surface du cercle selectionner
        :return: surface du cercle
        :rtype: float
        """
        return math.pi * self.__rayon ** 2

    def estEnIntersection(self, autrecercle: 'Cercle') -> bool:
        """
        Fonction qui calcul si le cercle est en intersection avec un autre cercle
        :param autrecercle: un autre cercle qui a deja été defini avant
        :type autrecercle: Cercle
        :return: Vrai ou Faux si les deux cercle sont en intersection ou pas
        :rtype: bool
        """
        distance = self.__centre.distancePoint(autrecercle.get_centre())
        return distance <= self.__rayon + autrecercle.get_rayon()

    def contient(self, point: 'Point') -> bool:
        """
        Fonction qui cacul si un point est compris dans le cercle
        :param point: un Point qui a deja été defini avant
        :type point: Point
        :return: Vrai ou Faux si le point est compris dans le cercle ou non
        :rtype: bool
        """
        distance = self.__centre.distancePoint(point)
        return distance <= self.__rayon


class Rectangle:
    def __init__(self, *args):
        if len(args) == 0:
            self.__bas_gauche = Point(0, 0)
            self.__longueur = 1
            self.__hauteur = 1
        elif len(args) == 3:
            self.__bas_gauche = args[0]
            self.__longueur = args[1]
            self.__hauteur = args[2]
        elif len(args) == 2:
            p1 = args[0]
            p2 = args[1]
            x1 = min(p1.get_x(), p2.get_x())
            y1 = min(p1.get_y(), p2.get_y())
            x2 = max(p1.get_x(), p2.get_x())
            y2 = max(p1.get_y(), p2.get_y())
            self.__bas_gauche = Point(x1, y1)
            self.__longueur = x2 - x1
            self.__hauteur = y2 - y1
        else:
            print("Erreur : paramètres invalides")

    def get_longueur(self):
        return self.__longueur

    def get_hauteur(self):
        return self.__hauteur

    def get_bas_gauche(self):
        return self.__bas_gauche

    def surface(self):
        """
        Fonction qui renvoie la surface du Rectangle
        :return: surface du Rectangle
        :rtype: float
        """

        return self.__longueur * self.__hauteur

    def perimetre(self):
        """
        Fonction qui renvoie le perimetre du Rectangle
        :return: preimetre du Rectangle
        :rtype: float
        """
        return 2 * (self.__longueur + self.__hauteur)

    def coin_bas_gauche(self):
        """
        Fonction qui renvoie le coin bas gauche du Rectangle
        :return: le coin bas gauche du Rectangle
        :rtype: Point
        """
        return self.__bas_gauche

    def coin_bas_droit(self):
        """
        Fonction qui renvoie le coin bas droit du Rectangle
        :return: le coin bas droit du Rectangle
        :rtype: Point
        """
        return Point(self.__bas_gauche.get_x() + self.__longueur, self.__bas_gauche.get_y())

    def coin_haut_gauche(self):
        """
        Fonction qui renvoie le coin haut gauche du Rectangle
        :return: le coin haut gauche du Rectangle
        :rtype: Point
        """
        return Point(self.__bas_gauche.get_x(), self.__bas_gauche.get_y() + self.__hauteur)

    def coin_haut_droit(self):
        """
        Fonction qui renvoie le coin haut droit du Rectangle
        :return: le coin haut droit du Rectangle
        :rtype: Point
        """
        return Point(self.__bas_gauche.get_x() + self.__longueur, self.__bas_gauche.get_y() + self.__hauteur)

    def contient(self, point:Point):
        """
        Fonction qui renvoie si le Rectangle contient un point donner en argument
        :param point: un point qui a ete defini avant
        :type point: Point
        :return: Vrai ou Faux en fonction si le Rectangle contient un point donner en argument ou non
        :rtype: bool
        """
        x = point.get_x()
        y = point.get_y()
        return (self.__bas_gauche.get_x() <= x <= self.__bas_gauche.get_x() + self.__longueur and
                self.__bas_gauche.get_y() <= y <= self.__bas_gauche.get_y() + self.__hauteur)

    def __str__(self):
        return f"Rectangle (x: {self.__bas_gauche.get_x()}, y: {self.__bas_gauche.get_y()}, L: {self.__longueur}, H: {self.__hauteur})"


class TriangleRectangle:
    def __init__(self, *args):
        if len(args) == 2:
            self.__cote1 = args[0]
            self.__cote2 = args[1]
            self.__angle_droit = Point(0, 0)
        elif len(args) == 3:
            self.__cote1 = args[0]
            self.__cote2 = args[1]
            self.__angle_droit = args[2]
        else:
            raise ValueError("Paramètres invalides")

    def get_cote1(self):
        return self.__cote1

    def get_cote2(self):
        return self.__cote2

    def get_angle_droit(self):
        return self.__angle_droit

    def hypothenuse(self) -> float:
        return math.sqrt(self.__cote1 ** 2 + self.__cote2 ** 2)

    def perimetre(self) -> float:
        return self.__cote1 + self.__cote2 + self.hypothenuse()

    def surface(self) -> float:
        return (self.__cote1 * self.__cote2) / 2

    def estIsocèle(self) -> bool:
        return self.__cote1 == self.__cote2

    def __str__(self):
        return (f"Triangle rectangle en {self.__angle_droit}, "
                f"cathetes {self.__cote1} et {self.__cote2}, "
                f"hypoténuse ≈ {self.hypothenuse():.2f}")


class TriangleRectangle:
    def __init__(self, *args):
        if len(args) == 2:
            # Mode 1 : deux longueurs, angle droit au point (0, 0)
            self.__cote1 = args[0]
            self.__cote2 = args[1]
            self.__point_angle_droit = Point()  # point (0, 0) par défaut
        elif len(args) == 3:
            # Mode 2 : deux longueurs + point d'angle droit
            self.__cote1 = args[0]
            self.__cote2 = args[1]
            self.__point_angle_droit = args[2]
        else:
            raise ValueError("Donne 2 ou 3 arguments : cote1, cote2 [, point]")

    # === Méthodes pour lire les valeurs (getters) ===
    def get_cote1(self):
        return self.__cote1

    def get_cote2(self):
        return self.__cote2

    def get_point_angle_droit(self):
        return self.__point_angle_droit

    # === Calcul de l'hypoténuse ===
    def hypothenuse(self):
        """
        Fonction qui renvoi l'hypothenuse du triangle rectangle
        :return: l'hypothenuse
        :rtype: float
        """
        return math.sqrt(self.__cote1 ** 2 + self.__cote2 ** 2)

    # === Périmètre du triangle ===
    def perimetre(self):
        """
        Fonction qui renvoi le perimetre du triangle rectangle
        :return: le perimetre
        :rtype: float
        """
        return self.__cote1 + self.__cote2 + self.hypothenuse()

    # === Aire (surface) du triangle ===
    def surface(self):
        """
        Fonction qui renvoi la surface du triangle rectangle
        :return: la surface
        :rtype: float
        """
        return (self.__cote1 * self.__cote2) / 2

    # === Le triangle est-il isocèle ? ===
    def est_isocèle(self):
        """
        Fonction qui renvoi si le triangle est isocele
        :return: renvoi si OUI ou NON le triangle est isocele
        :rtype: bool
        """
        return self.__cote1 == self.__cote2

    # === Affichage du triangle ===
    def __str__(self):
        return (f"Triangle rectangle avec angle droit en {self.__point_angle_droit}, "
                f"côtés {self.__cote1} et {self.__cote2}, "
                f"hypoténuse ≈ {self.hypothenuse():.2f}")

if __name__ == "__main__":
    print("\n--- TEST POINT ---")

    p1=Point() #Point sur l'origine
    p2=Point(3,4)

    print(p1)
    print(p2)

    print("Distance avec origine:", p1.distanceCoord(3, 4))  # Résultat : 5.0
    print("Distance avec un Point:", p1.distancePoint(p2))    # Résultat : 5.0

    print("\n--- TEST CERCLE ---")

    c1 = Cercle(5)  # Cercle centré à l'origine
    c2 = Cercle(2, p2)  # Cercle centré sur p2

    print("Diamètre de c1 :", c1.diametre())
    print("Périmètre de c1 :", c1.perimetre())
    print("Surface de c1 :", c1.surface())

    print("Les cercles se coupent-ils ?", c1.estEnIntersection(c2))
    print("Le point c2 est-il dans c1 ?", c1.contient(p2))

    print("\n--- TEST RECTANGLE ---")

    # Rectangle par défaut
    r1 = Rectangle()
    print(r1)
    print("Surface:", r1.surface())
    print("Périmètre:", r1.perimetre())

    # Rectangle avec point, longueur, hauteur
    p3 = Point(2, 3)
    r2 = Rectangle(p3, 4, 5)
    print("\n", r2)
    print("Coins:")
    print("Bas gauche:", r2.coin_bas_gauche())
    print("Bas droit:", r2.coin_bas_droit())
    print("Haut gauche:", r2.coin_haut_gauche())
    print("Haut droit:", r2.coin_haut_droit())

    # Rectangle avec deux points
    p4 = Point(1, 1)
    p5 = Point(5, 4)
    r3 = Rectangle(p4, p5)
    print("\n", r3)
    print("Surface:", r3.surface())
    print("Périmètre:", r3.perimetre())

    # Vérifie si un point est dans le rectangle
    p_test = Point(3, 2)
    print(f"Le point {p_test} est dans r3 ? {r3.contient(p_test)}")

    print("\n--- Triangle Rectangle ---")

    t1 = TriangleRectangle(3, 4)
    print(t1)
    print("Hypoténuse :", t1.hypothenuse())
    print("Périmètre :", t1.perimetre())
    print("Surface :", t1.surface())
    print("Isocèle ?", t1.est_isocèle())

    # Avec un point donné
    p = Point(1, 2)
    t2 = TriangleRectangle(5, 5, p)
    print("\n", t2)
    print("Hypoténuse :", t2.hypothenuse())
    print("Périmètre :", t2.perimetre())
    print("Surface :", t2.surface())
    print("Isocèle ?", t2.est_isocèle())
