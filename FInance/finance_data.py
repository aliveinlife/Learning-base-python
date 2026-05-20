import json, os
scriptdir = os.path.dirname(__file__)
pathtofile = os.path.join(scriptdir, "data.json")

def ldata():
    try:
        with open(f"{pathtofile}", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def sdata(data):
    with open(f"{pathtofile}", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

