import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_player_stats(player_name, tag):
    url = f'https://tracker.gg/valorant/profile/riot/{player_name}%23{tag}/overview'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Parse the stats you need from the HTML
        stats = {}
        # Example: stats['kda'] = soup.find('div', class_='some_class').text
        return stats
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
