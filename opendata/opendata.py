import requests, json, csv
import os

from config.settings import OPENDATA_APP_TOKEN
APP_TOKEN = os.getenv("OPENDATA_APP_TOKEN") or OPENDATA_APP_TOKEN

def pprint(json_item):
    print(json.dumps(json_item, indent=4))

OPENDATA_URLS = {
    "complaints" : "https://data.cityofnewyork.us/resource/eabe-havv.json",
    "ecb" : "https://data.cityofnewyork.us/resource/6bgk-3dad.json",
    "violations" : "https://data.cityofnewyork.us/resource/3h2n-5cm9.json",
    "now" : "https://data.cityofnewyork.us/resource/w9ak-ipjd.json",
    "bis" : "https://data.cityofnewyork.us/resource/ic3t-wcy2.json",
    "sign": "https://data.cityofnewyork.us/resource/nyis-y4yr.json",
    "cofo": "https://data.cityofnewyork.us/resource/bs8b-p36w.json",
}

class GetJobsBySIA():
    def __init__(self, sia_number):
        self.sia_number = sia_number
        self.now_jobs = self.now()
    
    def now(self, ):
        url = "https://data.cityofnewyork.us/resource/w9ak-ipjd.json"
        payload = {
            "$$app_token" : APP_TOKEN,
            "$limit": 2000000,
            "$where": "special_inspection_agency_number like '%{}'".format(self.sia_number)
            }
        r = requests.get(url, params=payload)
        return r.json()
    

if __name__ == "__main__":
    #binData = GetBin("1084455")
    #d = GetBlockLot(520, 56)
    pass