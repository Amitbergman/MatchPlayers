import time
import redis
from flask import Flask, request
import logging

redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)


app = Flask(__name__)

# Configure logging to flush immediately
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', force=True)

@app.route('/wannaplay')
def home():
    user_to_play = request.args.get('name')
    redis_client.rpush("games", user_to_play)
    return f"added user {user_to_play} to the waiting list"

@app.route('/getgames')
def getGames():
    user_to_play = request.args.get('name')
    game = redis_client.get(user_to_play)
    if game:
        return f"found a game: {user_to_play}:{game}"
    return f"no games"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)