import requests

BASE = "http://127.0.0.1:5000/" 




response = requests.patch(BASE + "video/2", json={"views": 3000, "likes": 1000})
print(response.json())