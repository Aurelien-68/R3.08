import math

class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"le point a les coodonées x: {self.x} et y: {self.y}"

    def distanceCoord(self,a:float, b:float) -> float:
        dx = self.x - a
        dy = self.y - b
        return (dx ** 2 + dy ** 2) ** 0.5
    def distancePoint(self,camarade: 'Point') -> float:
        return self.distanceCoord(camarade.x, camarade.y)


class Cercle:
    def __init__(self, rayon: float, centre: Point =Point()):
        self.rayon=rayon
        self.centre=centre

    def __str__(self):
        return f" Le cercle a pour rayon: {self.rayon} et pour centre {self.centre}"

    def diametre(self) -> float:
        return 2*self.rayon

    def perimetre(self) ->float:
        return 2*math.pi*self.rayon

    def surface(self) ->float:
        return math.pi * self.rayon ** 2

    def estEnIntersection(self, autrecercle: 'Cercle') -> bool:
        distance = self.centre.distancePoint(autrecercle.centre)
        if distance < self.rayon + autrecercle.rayon or distance == self.rayon + autrecercle.rayon:
            return True
        else:
            return False

    def contient(self, point: 'Point') -> bool:
        distance = self.centre.distancePoint(point)
        if distance < self.rayon or distance == self.rayon:
            return True
        else:
            return False


if __name__ == "__main__":
    p1=Point() #Point sur l'origine
    p2=Point(3,4)

    print(p1)
    print(p2)

    print("Distance avec origine:", p1.distanceCoord(3, 4))  # Résultat : 5.0
    print("Distance avec un Point:", p1.distancePoint(p2))    # Résultat : 5.0

    c1 = Cercle(rayon=5)  # Cercle centré à l'origine
    c2 = Cercle(rayon=2, p2)  # Cercle centré sur p2

    print("Diamètre de c1 :", c1.diametre())
    print("Périmètre de c1 :", c1.perimetre())
    print("Surface de c1 :", c1.surface())

    print("Les cercles se coupent-ils ?", c1.estEnIntersection(c2))
    print("Le point (3,4) est-il dans c1 ?", c1.contient(p2))