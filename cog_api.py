import requests

url = "https://www.ncbi.nlm.nih.gov/research/cog/api/cog/"

params = {
    "cog": "COG0003",
    "format": "json"
}

response = requests.get(url, params=params)

data = response.json() # перевод из json в python-объект (словарь)

# print(data)
# for elem in data["results"]:
#     print(elem)

for key, value in data["results"][0].items(): 
    print(key, ":", value)


