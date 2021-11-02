import requests
import json
from vrmlplayersearcher import *

class PubMain():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.player_names = []
    
    def resetVar(self):
        self.player_names = []
    
    def findNames(self):
        print("findNames called")
        url_request = requests.get('http://' + self.ip + ':6721/session')

        if url_request.status_code:
            data = url_request.text # String
            echo_data = json.loads(data) # Dict

            #teams[].players    # An array of objects containing data used to instantiate the team's players.
                


            teams_data = echo_data['teams']

            for i in range(0,len(teams_data)-1):
                per_team = teams_data[i]
                per_team_players = per_team['players']

                for j in range(0,len(per_team_players)):
                    temp_player = per_team_players[j]
                    self.player_names.append(temp_player['name']) # Add name to list
            return self.player_names
            
        else:
            print("Error connecting to echo api (" + url_request.status_code + "). Ensure the ip is correct")
    
    def getInfo(self):
        try:
            totalStats = []
            for name in self.player_names:
                main = VRMLMain('https://api.vrmasterleague.com/', name)
                res = main.completeSearch()
                totalStats.append(res)
            return totalStats
            
        except Exception as e:
            print("Something went wrong. Likely no player names detected.")
            print

    def completeSearch(self):
        self.resetVar()
        self.findNames()
        res = self.getInfo()
        print(res)

#main = PubMain("127.0.0.1","6721")
#main.completeSearch()

