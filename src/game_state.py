# Store game state data

class GameState:

	def __init__(self, home_team, away_team):
		"""
		Make a pre-coin toss game state
		"""
		self.home_team = home_team
		self.away_team = away_team
		self.home_playing = home_team.get_starting_lineup()
		self.away_playing = away_team.get_starting_lineup()
		self.possession = False  # who has the ball?
		self.down = 1
		self.home_score = 0
		self.away_score = 0

	def change_possession(self, team=False):
		"""
		Set the team that currently has possession
		:param team: the team to take possession; if none given, just switch to other team
		Opt: Team -> Void
		"""
		if team is not False:
			self.possession = team
		elif self.possession == self.home_team:
			self.possession = self.away_team
		else:
			self.possession = self.home_team