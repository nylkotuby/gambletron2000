# Interface for a roster
# TODO: does python have a way to require fields? 
# if not, then this is a guideline, not a rule
from abc import ABCMeta, abstractmethod

class Roster(metaclass=ABCMeta):

	"""
	FIELDS: 

	roster: Map of position (string) -> all players that play that position (list).
	        Lists should be ordered by player stats (probably).

	starting_lineup: Map of position (string) -> starting players (list).

	injured: plain list of injured players who are benched from the game

	TODO: break up w/m/s linebackers
	"""
	roster = {"c": [], "g": [], "t": [], "qb": [], "rb": [], "wr": [], "te": [],
	          "dt": [], "de": [], "lb": [], "cb": [], "s": [], "k": [], "p": []}

	starting_lineup = {"c": [], "g": [], "t": [], "qb": [], "rb": [], "wr": [], "te": [],
	                   "dt": [], "de": [], "lb": [], "cb": [], "s": [], "k": [], "p": []}

	injured = []

	def remove_injured_player(self, player):
		"""
		Move an injured player from the roster to list of injured
		:param player: the Player object who needs to be moved
		Void -> Void
		"""
		self.roster[player.position].remove(player)
		self.injured.append(player)