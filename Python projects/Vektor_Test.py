class FlexVektor:

    def __init__(self, coordinates):
        for c in coordinates:
            if not isinstance(c, (int, float)):
                raise ValueError("Koordinaten muessen Zahlen sein")
        self.coordinates = coordinates

    def __add__(self, other):
        """"
        >>> print(FlexVektor([3, 4]) + FlexVektor([1, 2]))
        [4, 6]
        >>> print(FlexVektor([3, 4, 5]) + FlexVektor([1, 2, 3]))
        [4, 6, 8]
        """

        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vektoren haben unterschiedliche Dimensionen")
        result = []
        for i in range(len(self.coordinates)):
            result.append(self.coordinates[i] + other.coordinates[i])
        return FlexVektor(result)

    def __mul__(self, other):
        """
        >>> print(FlexVektor([3, 4]) * FlexVektor([1, 2]))
        11
        :param other: FlexVektor object with x-dimensions
        :return: 0 if vectors have different dimensions or the dot product of the two vectors
        """
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vektoren haben unterschiedliche Dimensionen")
        result = 0
        for i in range(len(self.coordinates)):
            result += self.coordinates[i] * other.coordinates[i]
        return result

    def __str__(self):
        return str(self.coordinates)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)