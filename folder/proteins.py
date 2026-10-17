from cog_api import get_results
from Bio import SeqIO, Entrez 

Entrez.email = 'shgvacop@gmail.com'
Entrez.api_key = '3d935824f3086eb5b109f39934a74bbc7308'

def fetch_sequences(ids, Batch = 200):
    seqs = {}
    for i in range(len(ids), Batch):
        batch = ids[i:i+Batch]
        handle = Entrez.efetch(
            db = 'protein', 
            id = batch, # достаем по списку айди по 200 айди 
            rettype = 'fasta', # формат выдачи 
            retmode = 'text' # тип выдачи 
        )        
        for record in SeqIO.parse(handle, 'fasta'): 
            seqs[record.id] = str(record.seq)

    return seqs 
     

def get_sequences(table): 

    # Достаем пары ID белков+организм из таблицы 
    unique_ids = list(dict.fromkeys(row["protein_id"] for row in table))
    seqs = fetch_sequences(unique_ids)

    prot_seqs = {}
    for row in table:
        seq = seqs.get(row["protein_id"])
        if seq is None:        # NCBI не вернул этот белок
            continue
        prot_seqs.setdefault(row["cog"], []).append({
            "id": row["protein_id"] + "|" + row["organism"],
            "seq": seq,
        })

    return prot_seqs