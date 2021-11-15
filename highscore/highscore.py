import json


class Highscore():
    def __init__(self):
        self.dictHighscore = {}

    def getHighscore(self):
        getHighscoreList = []
        getHighscoreRenderList = []
        for value in self.dictHighscore.values():
            getHighscoreList.append((value['playername'], value['points']))
        for i in getHighscoreList:
            for x in i:
                getHighscoreRenderList.append(x)
        getHighscoreRenderList.insert(0, "menu")
        return(getHighscoreRenderList)

    def dictionaryToJSON(self):
        # note that highscore.json must already exist at this point
        with open('highscore/highscore.json', 'w+') as f:
            # this would place the entire output on one line
            # use json.dump(lista_items, f, indent=4) to "pretty-print" with four spaces per indent
            json.dump(self.dictHighscore, f, indent=4)

    def addHighscore(self, playername, points):
        y = 1
        for i in self.dictHighscore.values():
            if int(points) > int(i['points']):
                self.dictHighscore['position' + str(y)]['points'] = str(points)
                self.dictHighscore['position' +
                                   str(y)]['playername'] = playername
                print("You scored enough points for position"+str(y))
                break
            else:
                print("You didn't score enough points for position"+str(y))
            print(y)
            y += 1
        self.dictionaryToJSON()

    def jsonToDictionary(self):
        # Opening JSON file
        with open('highscore/highscore.json') as json_file:
            self.dictHighscore = json.load(json_file)
