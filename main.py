from cog_api import get_results()

organisms = []
for elem in results: 
    print(elem["organism"])

for i in range(len(results)):
    organisms.append(results[i]['organism'])

for elem in organisms: 
    print(elem['taxid'])