# скрипт принимает на вход название КОГа в формате "COG0001"
# на выходе: список словарей для каждого белка в КОГе 
# пример структуры словаря: 

# {
#   "gene_tag": "A11Q_RS08405",
#   "footprint": "1-427",
#   "footprint_length": 427,
#   "bitscore": 455.0,
#   "evalue": 1.2e-158,
#   "profile_length": "432.0",
#   "prot_coord": "1-429",

#   "organism": {
#     "assembly_id": "GCF_000348725.1",
#     "genome_name": "Pseudobdellovibrio_exovorus_JSS",
#     "taxid": 1184267,

#     "category": {
#       "name": "BDELLOVIBRIONOTA",
#       "taxid": 3018035}
#     },

#   "protein": {
#     "name": "WP_200860209.1",
#     "len": 427
#   },

#   "membership": {
#     "membership_class": 0,
#     "description": "footprint covers most of the protein and most of the COG profile"
#   },

#   "cog": {
#     "name": "Glutamate-1-semialdehyde aminotransferase",
#     "cogid": "COG0001",
#     "organism": 1715,
#     "proteins": 2497,
#     "genes": [
#       "HemL"
#     ],
#     "pdbs": [
#       "2CFB"
#     ],
#     "pathways": [
#       "Heme biosynthesis"
#     ],
#     "pubmeds": [
#       2045363
#     ],
#     "funcats": [
#       {
#         "name": "H",
#         "color": "DCDCFC",
#         "description": "Coenzyme transport and metabolism",
#         "order": 0
#       }
#     ]
#   }
# }



import requests
import argparse
import json

def get_results(cog):
    url = "https://www.ncbi.nlm.nih.gov/research/cog/api/cog/"

    params = {
        "cog": cog,
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    nxt = data["next"]
    results = data["results"]

    while nxt:
        response = requests.get(nxt)
        data_temp = response.json()

        results.extend(data_temp["results"])
        nxt = data_temp["next"]

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cog")
    args = parser.parse_args()

    results = get_results(args.cog)