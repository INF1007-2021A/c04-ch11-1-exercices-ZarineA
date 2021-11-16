"""
Chapitre 11.1
"""


import math
from inspect import *

from game import *


class Point2D_NoGoodPython:
	"""
	Exemple de point (x, y) avec encapsulation à la Java/C++ (méthodes de getter/setter)
	"""

	def __init__(self, x, y, name = "henlo"):
		self.__x = x
		self.__y = y
		self.__name = name

	def get_x(self):
		return self.__x
	
	def set_x(self, val):
		self.__x = val

	def get_y(self):
		return self.__y
	
	def set_y(self, val):
		self.__y = val

	def get_name(self):
		return self.__name

	def __str__(self):
		return f"({self.get_x()}, {self.get_y()})"


class Point2D:
	"""
	Exemple de point (x, y) avec encapsulation à l'aide de propriétés pythoniques
	"""

	def __init__(self, x, y, name = "henlo"):
		self.__x = x
		self.__y = y
		self.__name = name

	@property
	def x(self):
		return self.__x
	
	@x.setter
	def x(self, val):
		self.__x = val

	@property
	def y(self):
		return self.__y
	
	@y.setter
	def y(self, val):
		self.__y = val

	@property
	def name(self):
		return self.__name

	def __str__(self):
		return f"{self.name}: ({self.x}, {self.y})"

	@classmethod
	def from_list(cls, l):
		return cls(l[0], l[1])

	@staticmethod
	def add(p1, p2):
		return Point2D(p1.x + p2.x, p1.y + p2.y)


def main():
	c1 = Character("Äpik", 200, 150, 70, 70)
	c2 = Character("Gämmör", 250, 100, 120, 60)

	c1.weapon = Weapon("BFG", 100, 69)
	c2.weapon = Weapon("Deku Stick", 120, 1)

	turns = run_battle(c1, c2)
	print(f"The battle ended in {turns} turns.")

if __name__ == "__main__":
	main()

