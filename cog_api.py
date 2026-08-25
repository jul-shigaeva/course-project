import requests

url = "https://www.ncbi.nlm.nih.gov/research/cog/api/cog/"

params = {
    "cog": "COG0085",
    "format": "json"}
response = requests.get(url, params=params)
data = response.json() # перевод из json в python-объект (словарь)

for key, value in data["results"][0].items(): 
    print(key)

nxt = data["next"]
results = data["results"]
while nxt: 
    print(nxt)
    response = requests.get(nxt)
    data_temp = response.json()
    results.extend(data_temp["results"])
    nxt = data_temp["next"]