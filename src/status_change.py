# Represents a player's change in status

class StatusChange:

	"""
	LIST OF STATUSES:
	- "injured"
	- "ejected"
	"""

	def __init__(self, player, status):
		"""
		Takes a player and a list of approved status changes
		Player, ListOf(Status) -> StatusChange
		"""
		self.player = player
		self.status = status