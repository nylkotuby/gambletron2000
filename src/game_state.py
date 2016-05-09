# Store game state data

class GameState:

	def __init__(self, home_team, away_team):
		"""
		Make a pre-coin toss game state
		"""
		self.home_team = home_team
		self.away_team = away_team
		self.possession = False  # who has the ball?
		self.down = 1
		self.home_score = 0
		self.away_score = 0