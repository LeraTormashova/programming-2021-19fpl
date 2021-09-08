"""
Programming for linguists

Implementation of the class Square
"""
from shapes.rectangle import Rectangle


class Square(Rectangle):
    """
    A class for squares
    """
    def __init__(self, uid: int, length: int):
        super().__init__(uid, length, length)
        self.uid = uid

    def get_area(self):
        """
        Returns the area of a square
        :return int: the area of a square
        """
        return super().get_area()

    def get_perimeter(self):
        """
        Returns the perimeter of a square
        :return int: the perimeter of a square
        """
        return super().get_perimeter()

    def get_diagonal(self):
        """
        Returns the diagonal length of a square
        :return int: the diagonal length of a square
        """
        return super().get_diagonal()
