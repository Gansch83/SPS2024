class FlexVektor:
    """ 2D Vektor Klasse """
    def __init__(self, coordinates):
        #check if coordinates are numbers
        for i in coordinates:
            if not isinstance(i, (int, float)):
                raise TypeError("Vektoren müssen Zahlen enthalten")
        self.coordinates = coordinates

    def __add__(self, other):
        #addiere 2 Vektoren mit x dimensionen
        try:
            if len(self.coordinates) == len(other.coordinates):
                return FlexVektor([self.coordinates[i] + other.coordinates[i] for i in range(len(self.coordinates))])
            else:
                raise ValueError("Vektoren haben unterschiedliche Dimensionen")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
            return False

#    def __mul__(self, other):
#        # multipliziere 2 Vektoren mit x dimensionen
#        if len(self.coordinates) == len(other.coordinates):
#            return FlexVektor([self.coordinates[i] * other.coordinates[i] for i in range(len(self.coordinates))])
#        else:
#            print("Vektoren haben unterschiedliche Dimensionen")

    def __mul__(self, other):
        # multipliziere 2 Vektoren mit x dimensionen
        temp = FlexVektor([])

        if len(self.coordinates) == len(other.coordinates):
            for i in range(len(self.coordinates)):
              temp.coordinates.append(self.coordinates[i] * other.coordinates[i])
        else:
            raise  ValueError("Vektoren haben unterschiedliche Dimensionen")
            #print("Vektoren haben unterschiedliche Dimensionen")
        return temp

    def __str__(self):
        #print the coordinates of the vector
        return str(self.coordinates)


if __name__ == '__main__':
    print("\nBeispiel Polymorphismus")
    v1 = FlexVektor([3, 4, 5, 6, 7])
    v2 = FlexVektor([1, 2, 3, 4, 5])

    print ("v1 =", v1)
    print ("v2 =", v2)

    vs = v1 + v2
    print("Addition:", vs)

    vp = v1 * v2
    print("Multiplikation:", vp)

    v3 = FlexVektor([1, 2])
    print("v3 =", v3)


    ve = v1 + v3
    print("Fehler:", ve)

    try:
        Vektor1= FlexVektor([1,2])
        Vektor2= FlexVektor([1,"Orange"])
        v4 = Vektor1+Vektor2
        print("try except:", v4)
    except TypeError as e:
        print(e)


