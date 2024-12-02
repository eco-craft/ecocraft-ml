import requests

resp = requests.post("https://ecocraft-ml-376132824744.asia-southeast2.run.app/predict", files={'file': open('garpu.jpg', 'rb')})

print(resp.json())