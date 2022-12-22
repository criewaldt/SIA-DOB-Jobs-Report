from opendata.opendata import GetJobsBySIA
import sys, os

CURRENT_LOCATION = os.getcwd()
REPORT_PATH = "reports"
# Check whether the specified path exists or not
isExist = os.path.exists(REPORT_PATH)
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(REPORT_PATH)
    print("..The report directory didn't exist, so it was created!")
REPORT_PATH = os.path.join(CURRENT_LOCATION, REPORT_PATH)
print('CSV files will save in the following location: ', REPORT_PATH, '\n')

#Get SIA Jobs
while True:
    sia_number = input('Enter an SIA # to search signed-on DOB Now Build jobs: ')
    if len(sia_number) <= 6 and sia_number.isnumeric() == True:
        break
    print('..unrecognized SIA # try again.')

sia = GetJobsBySIA(sia_number=sia_number)

print(len(sia.now_jobs), 'DOB Now: Build jobs found for the SIA#', sia_number)

while True:
    if len(sia.now_jobs) == 0:
        break
    make_report = input('Would you like to save a CSV file with all found job data? (y/n): ')
    if make_report.lower() == 'n':
        sys.exit()
    if make_report.lower() == 'y':
        sia.make_report(REPORT_PATH)
        print('Report saved for SIA# {}'.format(sia_number))
        input('..press ENTER to exit.')
        sys.exit()

