from cog_api import get_results
from Bio import SeqIO, Entrez 

cgs = ['COG0001', 'COG0012']

def get_sequences(cogs): 
    results = []
    for cog in cogs: 
        results.append(get_results(cog))

    # Достаем ID белков 
    prot = {}
    for result in results: 
        idx = result[0]['cog']['cogid']
        prot[idx] = []
        for i in range(len(result)):
            prot[idx].append(result[i]['protein']['name'])


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
        prot_seqs[k] = [{"id": record.id, "seq": str(record.seq)} for record in records]

    return prot_seqs