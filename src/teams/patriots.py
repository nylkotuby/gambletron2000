# Patriots team strategy
from ..team import Team
from patriots_roster import PatriotsRoster

class Patriots(Team):

	def __init__(self, roster=None):
		self.roster = PatriotsRoster()

	def call_coin_toss(self):
		"""
		Heads is best, so always call heads
		Void -> String
		"""
		return "heads"