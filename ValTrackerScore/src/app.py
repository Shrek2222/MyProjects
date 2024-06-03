from flask import Flask, jsonify, request
import json
import os
from scrape_top_players.py import get_top_players
from calculations import calculate_enhanced_score

app = Flask(__name__)

@app.route('/player/<player_name>/<tag>', methods=['GET'])
def player_stats(player_name, tag):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(base_dir, '..', 'data', 'player_stats.json')
    
    with open(data_file, 'r') as f:
        player_stats = json.load(f)
        for stats in player_stats:
            if stats['player_name'] == player_name and stats['tag'] == tag:
                enhanced_score = calculate_enhanced_score(stats)
                return jsonify({'player_name': player_name, 'tag': tag, 'enhanced_score': enhanced_score, 'stats': stats})
    return jsonify({'error': 'Player not found'}), 404

@app.route('/top-players', methods=['GET'])
def top_players():
    players = get_top_players()
    if players:
        return jsonify(players)
    else:
        return jsonify({'error': 'Error fetching top players'}), 500

if __name__ == '__main__':
    app.run(debug=True)
