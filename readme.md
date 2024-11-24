To run the project:

1. docker-compose build
2. docker-compose up

(you should start seeing the background matcher waiting for players)

Then to add a player named "mock": 

http://localhost:5007/wannaplay?name=mock

To retrieve the game of a player:

http://localhost:5007/getgames?name=mock