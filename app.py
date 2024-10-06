import requests

# Make a GET request to a public GitHub API
response = requests.get("https:/api.github.com/users/github")

# Check if the response is successful
if response.status_code == 200:
  data = response.json()
  print(data)
