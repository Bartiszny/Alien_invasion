class GameStats():
    """Monitoring statistic data in ALien "Invasion" """

    def __init__(self, ai_settings):
        """ Initialzing statistic data"""
        self.ai_settings = ai_settings
        self.reset_status()
        # Running the game
        self.game_active = True

    def reset_status(self):
        """Initializing statistic data wich could change during the game"""
        self.ships_left = self.ai_settings.ship_limit
