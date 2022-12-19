from opendata.opendata import GetJobsBySIA

sia = GetJobsBySIA(sia_number="544")
print(len(sia.now_jobs))