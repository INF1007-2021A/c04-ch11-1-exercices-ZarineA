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


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""



def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	print(f"{attacker.name} used {attacker.weapon.name}")
	if crit:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		# TODO: Appliquer l'attaque
		# TODO: Si le défendeur est mort
			print(f"{defender.name } is sleeping with the fishes.")
			break
		# Échanger attaquant/défendeur
	# TODO: Retourner nombre de tours effectués
