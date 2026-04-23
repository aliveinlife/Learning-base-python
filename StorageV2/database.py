import json


try:
    with open("StorageV2/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
        data = {}



def ldata():
    try:
        with open("StorageV2/data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return data



def sdata(data):
    with open("StorageV2/data.json", "w", encoding="utf-8") as g:
        json.dump(data, g, indent=4, ensure_ascii=False)



