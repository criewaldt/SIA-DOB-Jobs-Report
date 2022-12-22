import requests, json, csv, sys
from datetime import date
import os

from config.settings import OPENDATA_APP_TOKEN

APP_TOKEN = os.getenv("OPENDATA_APP_TOKEN") or OPENDATA_APP_TOKEN

class GetJobsBySIA():
    def __init__(self, sia_number):
        self.sia_number = sia_number
        self.now_jobs = self.now()
        self.clean_jobs()

    def clean_jobs(self,):
        jobs = []
        for job in self.now_jobs:
            sia_numbers = job['special_inspection_agency_number'].split(',')
            if self.sia_number.zfill(6) in sia_numbers or self.sia_number in sia_numbers:
                jobs.append(job)
                #print(job['special_inspection_agency_number'], 'added.')
        self.now_jobs = jobs
    
    def now(self, ):
        url = "https://data.cityofnewyork.us/resource/w9ak-ipjd.json"
        payload = {
            "$$app_token" : APP_TOKEN,
            "$limit": 2000000,
            "$where": "special_inspection_agency_number like '%{}'".format(self.sia_number)
            }
        r = requests.get(url, params=payload)
        return r.json()
    
    def make_report(self, REPORT_PATH):

        today = date.today()
        today = today.strftime("%Y-%m-%d")

        # now we will open a file for writing

        csv_path = os.path.join(REPORT_PATH, '{}-{}.csv'.format(self.sia_number, today))
        csv_path = os.path.abspath(csv_path)
        with open(csv_path, 'w', newline='') as data_file:
        
            # create the csv writer object
            writer = csv.writer(data_file)

            writer.writerow(["DOB Now Jobs With SIA# {} - Jobs Count: {}".format(self.sia_number, len(self.now_jobs))])
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