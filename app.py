from opendata.opendata import GetJobsBySIA

sia = GetJobsBySIA(sia_number="6695")
print(len(sia.now_jobs))