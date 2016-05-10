# Interface for a team
from abc import ABCMeta, abstractmethod

class Team(metaclass=ABCMeta):

	def __init__(self, roster=None):
		"""
		Create a team with a roster
		TODO: should roster be passed in?
		Roster -> Team
		"""
		self.roster = roster

	@abstractmethod
	def call_coin_toss(self):
		"""
		Teams must choose a strategy for calling a coin toss
		:return "heads" or "tails"
		Void -> String
		"""
		raise NotImplementedError()

	@abstractmethod
	def get_starting_lineup(self):
		"""
		Pass up the starting lineup for game manager to track
		:returns the roster's starting lineup
		Void -> Map(String -> ListOf(Player))
		"""
		return self.roster.starting_lineup

	@abstractmethod
	def update_players(self, status_changes):
		"""
		Given a list of players and their changes in status (ex. injury),
		update their status in the roster and pass back their replacements.
		:return a list of StatusChange that is strictly the length of the list given
		ListOf(StatusChange) -> ListOf(StatusChange)
		"""
		raise NotImplementedError()
		