class Game_stats:

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.level = 1
        self.reset_stats()

    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
