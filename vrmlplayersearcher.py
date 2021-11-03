import requests
import requests.utils, requests.adapters
import json
import time
import sys, os
import certifi.core
import certifi

from PyInstaller.utils.hooks import collect_data_files ## Certificate verification to prevent compiled issues

datas = collect_data_files('certifi')
os.environ["REQUESTS_CA_BUNDLE"] = "certifi/cacert.pem"
requests.utils.DEFAULT_CA_BUNDLE_PATH = "certifi/cacert.pem"
requests.adapters.DEFAULT_CA_BUNDLE_PATH = "certifi/cacert.pem"

class VRMLMain():
    def __init__(self, url, username):
        self.url = url
        self.username = username
        
    
    def createRequest(self):
        # Query all teams, with their rosters
        url_request = requests.get(self.url + "/EchoArena/Players")

        raw_data = url_request.text # All data from query (THIS IS A STRING RN)

        # Convert string into list
        self.data_list = json.loads(raw_data) # This is a list
        try:
            self.progressBar.setProperty("value", 10)
        except:
            pass

    
    def filterRequest(self):
        self.found_team = None

        # Will go through all items in list
        for i in range(0, len(self.data_list)): 
            test_data = self.data_list[i]
            players = test_data['players'] # This is a list
            
            # Go through list of players
            for j in range(0, len(players)):
                individual_player = players[j] # This is a dict
                temp_name = individual_player['name']

                if temp_name == self.username: # If username found
                    self.found_team = True
                    self.found_data = test_data

                    pass
        try:
            self.progressBar.setProperty("value", 70)
        except:
            pass

    
    def outputResults(self):
        # If team is found
        if self.found_team != None:
            team_name = self.found_data['name']
            team_id = self.found_data['id']
            #print("Team: " + team_name) # Display team name

            try:
                self.progressBar.setProperty("value", 80)
            except:
                pass


            url_request = requests.get(self.url + "Teams/" + team_id)

            data = url_request.text
            team_info = json.loads(data)
            ranking = team_info['rankWorldwide']
            tier = team_info['division']

            try:
                self.progressBar.setProperty("value", 90)
            except:
                pass


            #print("Worldwide Rank: " + str(ranking)) # Display ranking
            #print("Tier: " + tier) # Display tier
            #print('')

            try:
                self.progressBar.setProperty("value", 100)
            except:
                pass

            return team_name, ranking, tier

            
        else:

            try:
                self.progressBar.setProperty("value", 100)
            except:
                pass
            return "N/A", "N/A", "N/A"
    
    def completeSearch(self):
        self.createRequest()
        self.filterRequest()
        results = self.outputResults()
        #print("Complete Search Complete")
        return results
    
    def completeSearchWithGUI(self, progressBar):
        self.barHere = True
        self.progressBar = progressBar
        self.progressBar.setProperty("value", 0)
        self.currentProgress = 0
        self.createRequest()
        self.filterRequest()
        results = self.outputResults()
        return results

### Comment out the following if using as a library
#main = Main('https://api.vrmasterleague.com/', "Silveridge")
#main.createRequest()
#main.filterRequest()