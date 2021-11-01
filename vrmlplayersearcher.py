import requests
import json


class Main():
    def __init__(self, url, username):
        self.url = url
        self.username = username
    
    def createRequest(self):
        # Query all teams, with their rosters
        url_request = requests.get(self.url + "/EchoArena/Players")

        raw_data = url_request.text # All data from query (THIS IS A STRING RN)

        # Convert string into list
        self.data_list = json.loads(raw_data) # This is a list
    
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
                    break
    
    def outputResults(self):
        # If team is found
        if self.found_team != None:
            team_name = self.found_data['name']
            team_id = self.found_data['id']
            print("Team: " + team_name) # Display team name

            url_request = requests.get(self.url + "Teams/" + team_id)

            data = url_request.text
            team_info = json.loads(data)
            ranking = team_info['rankWorldwide']
            tier = team_info['division']

            print("Worldwide Rank: " + str(ranking)) # Display ranking
            print("Tier: " + tier) # Display tier
            print('')

            
        else:
            print('No team found')

### Comment out the following if using as a library
main = Main('https://api.vrmasterleague.com/', "<Username Here>")
main.createRequest()
main.filterRequest()
main.outputResults()