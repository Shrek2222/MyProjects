import requests
from bs4 import BeautifulSoup

def get_top_players():
    url = 'https://tracker.gg/valorant/leaderboards/ranked/all/default'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        players = []
        rows = soup.select('div.player-card')
        for row in rows[:10]:  # Get the top 10 players
            player = {
                'rank': row.select_one('.rank').text.strip(),
                'player_name': row.select_one('.player-name').text.strip(),
                'tag': row.select_one('.player-tag').text.strip(),
                'rr': row.select_one('.rating').text.strip(),
                'games_won': row.select_one('.games-won').text.strip()
            }
            players.append(player)
        return players
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    top_players = get_top_players()
    if top_players:
        for player in top_players:
            print(player)
    else:
        print("Error fetching top players")
