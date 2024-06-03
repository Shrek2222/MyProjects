import requests

API_KEY = 'RGAPI-1d32aa88-4a5a-4943-b1e7-95036234fadc'
BASE_URL = 'https://na.api.riotgames.com/val/'

def get_player_stats(player_id):
    url = f'{BASE_URL}/v1/players/by-name/{player_id}'
    headers = {'X-Riot-Token': API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
if __name__ == "__main__":
    player_id = 'Eggsterr#NJLTC'
    player_stats = get_player_stats(player_id)
    if player_stats:
        print(player_stats)
    else:
        print("Error fetching player stats")

