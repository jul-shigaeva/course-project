import json
import requests

URL = "https://www.ncbi.nlm.nih.gov/research/cog/api/taxonomy/"

r = requests.get(URL, params={"format": "json"}, timeout=30)
r.raise_for_status()
data = r.json()

if isinstance(data, dict) and "results" in data:
    items = list(data["results"])
    nxt = data.get("next")
    while nxt:
        r = requests.get(nxt, timeout=30)
        r.raise_for_status()
        data = r.json()
        items.extend(data["results"])
        nxt = data.get("next")
else:
    items = data

print("всего групп:", len(items))
print(json.dumps(items[0], indent=2, ensure_ascii=False))
print([i.get("name") for i in items])

print("--- организмов в каждой группе ---")
for i in items:
    print(i["name"], i["taxid"], len(i["organisms"]))

filled = [i for i in items if i["organisms"]]
if filled:
    print(json.dumps(filled[0]["organisms"][:2], indent=2, ensure_ascii=False))

print("--- группы в таблице COG0001 ---")
from collections import Counter
from table import get_table
table = get_table(["COG0001"])
print(Counter(t["category"] for t in table))