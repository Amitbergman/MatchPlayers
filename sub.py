import redis

def retrieveFromQueue():
    redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)
    while True:
        player_1 = redis_client.blpop("games", timeout=0)
        if (player_1):
            player_1_name = player_1[1]
            while True:
                # wait for player 2
                player_2 = redis_client.blpop("games", timeout=0)
                if (player_2):
                    player_2_name = player_2[1]
                    print(f"created a game: {player_1_name}:{player_2_name}")
                    redis_client.set(player_1_name, player_2_name)
                    redis_client.set(player_2_name, player_1_name)
                    break

if __name__ == "__main__":
    retrieveFromQueue()