import requests, json
import config

"""
f = open("api.txt", "r")
text_api_key = f.read() #needs to be hidden
"""

class SearchIgnite():
    def __init__(self,username):
        self.username = username
        self.api_key = config.api_key
        self.createRequest()
        self.findResults()

    def createRequest(self):
        url_request = requests.get("https://api.ignitevr.workers.dev/player_stats/" + self.username + "?x-api-key=" + self.api_key)

        self.data_list = json.loads(url_request.text) #this is a list

        
        if url_request.status_code == 200:
            self.has_stats = True
        if url_request.status_code == 404:
            self.has_stats = False


    def findResults(self):
        #print(self.data_list)
        if self.has_stats:
            try:
                self.game_count = int(self.data_list['player'][0]['game_count'])
                self.wins = int(self.data_list['player'][0]['total_wins'])
                self.level = int(self.data_list['player'][0]['level'])
                self.winrate = round(((self.wins / self.game_count) * 100),2)

                self.has_vrml = True

                if len(self.data_list['vrml_player']) == 0: #not triggering
                    self.has_vrml = False

                if self.has_vrml:
                    self.country = self.data_list['vrml_player']['country']
                    self.team_name = self.data_list['vrml_player']['team_name']
                    self.team_logo = self.data_list['vrml_player']['team_logo']
                    self.team_page = self.data_list['vrml_player']['team_page']

                self.has_stats = True
            except:
                print("Player has no ignite stats (except occured)")
                print(self.has_vrml)
                self.has_stats = False

    def printResults(self): 
        if self.has_stats:
            print(self.winrate)
            print(self.level)

            if self.has_vrml:
                print(self.country)
                print(self.team_page)
                print(self.team_logo)
                print(self.team_name)
    
    def outputResults(self):
        self.ignite_stats = []
        self.ignite_stats.append(self.has_stats)
        if self.has_stats:
            self.ignite_stats.append(self.has_vrml)
            self.ignite_stats.append(self.winrate)
            self.ignite_stats.append(self.level)

            if self.has_vrml:
                self.ignite_stats.append(self.country)
                self.ignite_stats.append(self.team_page)
                self.ignite_stats.append(self.team_logo)
                self.ignite_stats.append(self.team_name)
            
            
        return self.ignite_stats



#player = SearchIgnite('TheRealZeroz')
#player.printResults()