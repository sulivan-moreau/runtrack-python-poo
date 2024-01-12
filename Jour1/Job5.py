class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("Coordonnées du point :",self.x,", ",self.y)

    def afficheX(self):
        print ("x = ",self.x)

    def afficheY(self):
        print ("y = ",self.y)

    def changerX(self):
        self.x= input("Donnez une valeur pour x : ")

    def changerY(self):
        self.y= input("Donnez une valeur pour y : ")

point = Point(2, 3)

point.afficherLesPoints()
point.afficheX()
point.afficheY()

point.changerX()
point.changerY()

point.afficherLesPoints()