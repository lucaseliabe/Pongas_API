from flask import Blueprint, request, jsonify

player_controller = Blueprint('player_constroller', __name__)

@player_controller.route('/player', methods=['POST'])
def create_player():
    body = request.get_json()
    