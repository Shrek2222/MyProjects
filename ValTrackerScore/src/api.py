import requests

API_KEY = 'removed private information'
BASE_URL = 'https://public-api.tracker.gg/v2/valorant/standard/profile/riot/'

def get_player_stats(player_name, tag):
    url = f'{BASE_URL}{player_name}%23{tag}'
    headers = {
        'TRN-Api-Key': API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Example usage
if __name__ == "__main__":
    player_name = 'Eggsterr'
    tag = 'NJLTC'
    player_stats = get_player_stats(player_name, tag)
    if player_stats:
        print(player_stats)
    else:
        print("Error fetching player stats")
