class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        self.bullet_speed_factor = 1
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = 50, 50, 50
        self.bullets_allowed = 3
        self.alien_speed_factor = 1
        self.alien_points = 50
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.score_scale = 1.5
    
    def increse_speed(self):
        self.aliens_points = int(self.alien_points * self.score_scale)
