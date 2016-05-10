# Eagles team strategy
from ..team import Team
from eagles_roster import EaglesRoster

class Eagles(Team):

	def __init__(self, roster=None):
		self.roster = EaglesRoster()

	def call_coin_toss(self):
		"""
		Tails has an eagle usually, so always call tails
		Void -> String
		"""
		return "tails"