"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	UNARMED_POWER = 20

	def __init__(self, name: str, power: float, min_level: int) -> None:
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self) -> str:
		return self.__name

	@property
	def power(self) -> float:
		return self.__power

	@power.setter
	def power(self, value: float) -> None:
		self.__power = value

	@property
	def min_level(self) -> int:
		return self.__min_level

	@min_level.setter
	def min_level(self, value: int) -> None:
		self.__min_level = value

	@staticmethod
	def make_unarmed():
		return Weapon("Unarmed", Weapon.UNARMED_POWER, 0)


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name: str, max_hp: float, attack: int, defense: int, level: int) -> None:
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.hp = max_hp

	# --- name
	@property
	def name(self) -> str:
		return self.__name

	# --- max_hp
	@property
	def max_hp(self) -> float:
		return self.__max_hp

	@max_hp.setter
	def max_hp(self, value: float) -> None:
		self.__max_hp = value

	# --- attack
	@property
	def attack(self) -> int:
		return self.__attack

	@attack.setter
	def attack(self, value: int) -> None:
		self.__attack = value

	# -- defense
	@property
	def defense(self) -> int:
		return self.__defense

	@defense.setter
	def defense(self, value: int) -> None:
		self.__defense = value

	# --- level
	@property
	def level(self) -> int:
		return self.__level

	@level.setter
	def level(self, value: int) -> None:
		self.__level = value

	# --- weapon
	@property
	def weapon(self) -> Weapon:
		return self.__weapon

	@weapon.setter
	def weapon(self, value: Weapon) -> None:
		if value is None:
			self.weapon = Weapon.make_unarmed()
		elif value.min_level > self.level:
			raise ValueError
		else:
			self.__weapon = value

	# --- hp
	@property
	def hp(self) -> float:
		return self.__hp

	@hp.setter
	def hp(self, value: float) -> None:
		self.__hp = utils.clamp(value, 0, self.max_hp)

	def compute_damage(self, defender) -> (float, bool):
		PROBABILTY_CRIT_2 = 1/16
		MIN_RANDOM, MAX_RANDOM = 85/100, 100/100

		crit = 2 if random.random() < PROBABILTY_CRIT_2 else 1
		rand = (MAX_RANDOM - MIN_RANDOM) * random.random() + MIN_RANDOM
		return ((2*self.level/5+2) * self.weapon.power * self.attack/defender.defense / 50 + 2) * crit * rand, crit == 2


def deal_damage(attacker: Character, defender: Character) -> None:
	print(f"{attacker.name} used {attacker.weapon.name}")
	damage, crit = attacker.compute_damage(defender)
	damage = int(damage)
	if crit:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")
	defender.hp -= damage


def run_battle(c1: Character, c2: Character) -> int:
	attacker, defender = c1, c2
	turn = 0
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		turn += 1
		deal_damage(attacker, defender)
		if defender.hp == 0:
			print(f"{defender.name } is sleeping with the fishes.")
			break
		attacker, defender = defender, attacker
	return turn
