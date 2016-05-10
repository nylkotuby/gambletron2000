# Represents a player and their essential stats
from abc import ABCMeta, abstractmethod

# TODO: subclasses for each position (ugh)
class Player(metaclass=ABCMeta):

	injury = False

	def __init__(self, last_name, first_name, team_name, number, age, height, 
		               weight, position):
		"""
		:param last_name: String 
		:param first_name: String
		:param team_name: String
		:param number: int
		:param age: int (years)
		:param height: int (inches)
		:param weight: int (pounds)
		:param position: String maybe
		"""
		self.last_name = last_name
		self.first_name = first_name
		self.team_name = team_name
		self.number = number
		self.age = age
		self.height = height
		self.weight = weight
		self.position = position # TODO: unneccessary?