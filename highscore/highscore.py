class Highscore():
    def __init__(self):
        self.dictHighscore = {
            "position1": {
                "playername": "None",
                "points": 500
            }
        }

    def getHighscore(self):
        return self.dictHighscore

    def addHighscore(self, points):
        new_output = list(self.dictHighscore.values())
        for value in self.dictHighscore.values():
            pass
