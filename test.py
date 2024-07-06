import requests

BASE = "http://127.0.0.1:5000/"

# data = [{'likes': 1000, "name": "Amisa", "views": 7234}, 
#         {'likes': 2636, "name": "Flask REST API", "views": 10000},
#         {'likes': 287, "name": "Amisa", "views": 9898}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), json=data[i])
#     print(response.json()) 

response = requests.get(BASE + "video/2")
print(response.json())

data = {"name": "Amisa", "views":99, "likes": 50}

response = requests.patch(BASE + "video/2", json=data)
print(response.json())

print("Test")