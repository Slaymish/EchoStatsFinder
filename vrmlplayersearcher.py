import requests
import json

def main():
    url = 'https://api.vrmasterleague.com/'


    username = input('Username: ')

    """
    # Test Connection to API
    url_request = requests.get(url)

    if url_request:
        # Display Connection
        print("Sucesfully Connected (" + str(url_request.status_code) + ")")
    else:
        # Display Error message
        print("Error: " + str(url_request.status_code))

    """

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
        # Loop
        main()

        
    else:
        print('No team found')
        main()

main()