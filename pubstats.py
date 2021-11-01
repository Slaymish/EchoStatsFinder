import requests
import json

with open('ip.txt') as f:
    ip = f.readline()



player_names = []

def find_names():

    url_request = requests.get('http://' + ip + ':6721/session')

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
                player_names.append(temp_player['name']) # Add name to list
        
    else:
        print("Error connecting to echo api (" + url_request.status_code + "). Ensure the ip is correct")


def main(user):
    url = 'https://api.vrmasterleague.com/'
    
    username = user

    # Query all teams, with their rosters
    url_request = requests.get(url + "/EchoArena/Players")

    raw_data = url_request.text # All data from query (THIS IS A STRING RN)

    # Convert string into list
    data_list = json.loads(raw_data) # This is a list
    found_team = None

    # Will go through all items in list
    for i in range(0, len(data_list)): 
        test_data = data_list[i]
        players = test_data['players'] # This is a list
        
        # Go through list of players
        for j in range(0, len(players)):
            individual_player = players[j] # This is a dict
            temp_name = individual_player['name']

            if temp_name == username: # If username found
                found_team = True
                found_data = test_data
                break


    # If team is found
    if found_team != None:
        team_name = found_data['name']
        team_id = found_data['id']
        print("Team: " + team_name) # Display team name

        url_request = requests.get(url + "Teams/" + team_id)

        data = url_request.text
        team_info = json.loads(data)
        ranking = team_info['rankWorldwide']
        tier = team_info['division']

        print("Worldwide Rank: " + str(ranking)) # Display ranking
        print("Tier: " + tier) # Display tier
        print('')


        
    else:
        print('No team found')
        print('')

def run():
    find_names()
    for i in range(0, len(player_names)):
        print("Username: " + player_names[i])
        main(player_names[i])



run()


# Slaymish was here xoxox

