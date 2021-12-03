import requests
import json
#import certifi
from searchignite import *

"""
## Fix Certificate Issues
from PyInstaller.utils.hooks import collect_data_files ## Certificate verification to prevent compiled issues

datas = collect_data_files('certifi')
os.environ["REQUESTS_CA_BUNDLE"] = "certifi/cacert.pem"
requests.utils.DEFAULT_CA_BUNDLE_PATH = "certifi/cacert.pem"
requests.adapters.DEFAULT_CA_BUNDLE_PATH = "certifi/cacert.pem"

"""


class PubMain():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.player_names = []
        self.completeSearch()
    
    def resetVar(self):
        self.player_names = []
    
    def findNames(self):
        #print("findNames called")
        try:
            url_request = requests.get('http://' + self.ip + ':' + self.port + '/session')

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
        except Exception as e:
            print(e)

    def getInfo(self):
        try:
            self.totalStats = []
            for name in self.player_names:
                main = SearchIgnite(name)
                res = main.outputResults()
                self.totalStats.append(res)
            return self.totalStats
            
        except Exception as e:
            print("Something went wrong. Likely no player names detected.")

    def cliResults(self):
        for i in range(0, len(self.player_names)):
            print("-------------------------------------")
            print(self.player_names[i])
            has_stats = self.totalStats[i][0]

            if has_stats:
                has_vrml = self.totalStats[i][1]
                print("Winrate:" + str(self.totalStats[i][2]))
                print("Level:" + str(self.totalStats[i][3]))

                if has_vrml:
                    print("Country:" + str(self.totalStats[i][4]))
                    print("Team Name:" + str(self.totalStats[i][7]))


    def completeSearch(self):
        self.resetVar()
        self.findNames()
        self.getInfo()

#main = PubMain("127.0.0.1","6721")
#main.completeSearch()

