import requests

response = requests.get("https://i.imgur.com/ExdKOOz.png")
file = open("input-images/inpImage.png", "wb")
file.write(response.content)
file.close()