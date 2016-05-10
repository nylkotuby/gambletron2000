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

	ejected: plain list of players who are benched from the game; usually badly-injured ones

	TODO: break up w/m/s linebackers
	"""
	roster = {"c": [], "g": [], "t": [], "qb": [], "rb": [], "wr": [], "te": [],
	          "dt": [], "de": [], "lb": [], "cb": [], "s": [], "k": [], "p": []}

	starting_lineup = {"c": [], "g": [], "t": [], "qb": [], "rb": [], "wr": [], "te": [],
	                   "dt": [], "de": [], "lb": [], "cb": [], "s": [], "k": [], "p": []}

	ejected = []

	def remove_ejected_player(self, player):
		"""
		Move an ejected player from the roster to list of injured
		:param player: the Player object who needs to be moved
		Void -> Void
		"""
		self.roster[player.position].remove(player)
		self.ejected.append(player)

	@abstractmethod
	def get_position(self, position):
		"""
		Choose the next player at the given position to send out
		NOTE: using a good position comparator is probably better than a giant if/elif/else for this
		String -> Player
		"""
		return roster[position][0]