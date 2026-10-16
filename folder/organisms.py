from cog_api import get_results

cogs = ["COG0105", "COG0085"]

results = []
for cog in cogs: 
    results.append(get_results(cog))

print(results)