import requests
import argparse

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