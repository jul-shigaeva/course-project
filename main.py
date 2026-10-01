from cog_api import get_results
from Bio import SeqIO, Entrez 

cogs = ["COG0105", "COG0085"]

results = []
for cog in cogs: 
    results.append(get_results(cog))

# organisms = []

# for i in range(len(results)):
#     organisms.append(results[i]['organism'])

# print(len(organisms))
# print(organisms[0])


# Достаем ID белков 
prot = {}
for result in results: 
    idx = result[0]['cog']['cogid']
    prot[idx] = []
    for i in range(len(result)):
        prot[idx].append(result[i]['protein']['name'])

# print(prot)


# Достаем белки 
Entrez.email = 'shgvacop@gmail.com'
Entrez.api_key = '3d935824f3086eb5b109f39934a74bbc7308'

prot_seqs = {}

for k, value in prot.items(): 
    handle = Entrez.efetch(
        db = "protein", 
        id = value, # передаю список 
        rettype = "fasta", # формат возвращаемых данных 
        retmode = "text") # тип возвращаемых данных 
    records = list(SeqIO.parse(handle, 'fasta'))
    handle.close()
    prot_seqs[k] = [str(record.seq) for record in records]

print(prot_seqs)