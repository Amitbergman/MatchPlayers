import requests

# Specify the URL
# Specify headers if needed
headers = {
    "Content-Type": "application/json"
}

numberOfPlayers = 100000
for i in range(numberOfPlayers):
    print(i)
    url = f"http://localhost:5007/wannaplay?name={i}"
    response = requests.get(url)

for i in range(numberOfPlayers):
    url = f"http://localhost:5007/getgames?name={i}"
    response = requests.get(url)
    print(response.status_code)
    print(f"Response Content: {response.text}")


