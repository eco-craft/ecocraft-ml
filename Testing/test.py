import requests

resp = requests.post("http://127.0.0.1:5000", files={'file': open('bright-messy-clothing-background-17160491.jpg', 'rb')})

print(resp.json())