import requests, json, csv
from datetime import date
import os

from config.settings import OPENDATA_APP_TOKEN
APP_TOKEN = os.getenv("OPENDATA_APP_TOKEN") or OPENDATA_APP_TOKEN




class GetJobsBySIA():
    def __init__(self, sia_number):
        self.sia_number = sia_number
        self.now_jobs = self.now()
        self.make_report()
    
    def now(self, ):
        url = "https://data.cityofnewyork.us/resource/w9ak-ipjd.json"
        payload = {
            "$$app_token" : APP_TOKEN,
            "$limit": 2000000,
            "$where": "special_inspection_agency_number like '%{}'".format(self.sia_number)
            }
        r = requests.get(url, params=payload)
        return r.json()
    
    def make_report(self,):

        today = date.today()
        today = today.strftime("%Y-%m-%d")

        # now we will open a file for writing
        with open('{}-{}.csv'.format(self.sia_number, today), 'w') as data_file:
        
            # create the csv writer object
            writer = csv.writer(data_file)

            writer.writerow(["DOB Now Jobs With SIA# {}".format(self.sia_number)])
            ###
            try:
                headers = list(self.now_jobs[0].keys())
                writer.writerow(headers)
                for job in self.now_jobs:
                    r = []
                    for h in headers:
                        try:
                            r.append(job[h])
                        except:
                            pass
                    writer.writerow(r)
            except IndexError:
                writer.writerow(["Index Error: issue finding jobs... maybe none exist? If they do, contact Chris."])
            ###
    

if __name__ == "__main__":
    pass