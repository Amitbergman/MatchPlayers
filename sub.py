import time
import redis

def retrieveFromQueue():
    redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)
    while True:
        player_1 = redis_client.lpop("games")
        if (player_1):
            print(f"player 1: {player_1}")
            while True:
                # wait for player 2
                player_2 = redis_client.rpop("games")
                if (player_2):
                    redis_client.set(player_1, player_2)
                    redis_client.set(player_2, player_1)
                    break
                else:
                    print("keep waiting for player 2")
                    time.sleep(1)
        else:
            print("keep waiting for player 1")
            time.sleep(5)

if __name__ == "__main__":
    retrieveFromQueue()