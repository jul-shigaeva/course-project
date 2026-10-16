from cog_api import get_results

def get_table(cogs): 
    results = {cog: get_results(cog) for cog in cogs}
    table = []
    for cog in results.values(): 
        for r in cog: 
            cog_id = r["cog"]["cogid"]
            protein_id = r["protein"]["name"]
            org = r["organism"]

            seen = set()
            key = (cog_id, protein_id, org["assembly_id"])
            if key in seen:
                continue
            seen.add(key)

            table.append({
                "cog": cog_id,
                "protein_id": protein_id,
                "locus_tag": r.get("gene_tag"),
                "assembly_id": org["assembly_id"],
                "organism": org["genome_name"],
                "taxid": org["taxid"],
                "category": (org.get("category") or {}).get("name"),
            })
            
    return table