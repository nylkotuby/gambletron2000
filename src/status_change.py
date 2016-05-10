# Represents a player's change in status

class StatusChange:

	"""
	LIST OF STATUSES:
	- "injured"
	"""

	def __init__(self, player, status):
		"""
		"""
		self.player = player
		self.status = status