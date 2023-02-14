import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("telenews_key.json",scope)
client = gspread.authorize(creds)

ndate=datetime.datetime.now()
today="{}/{}/{}".format(ndate.year,ndate.month,ndate.day)

def checkNews(sheetName,news):
    theSheet = client.open(sheetName).sheet1

    # Initialize a list to store the values
    values = theSheet.col_values(1)
    values=[str(val).replace("\xa0","").replace("\t","") for val in values]
    newValues=values[0:14]
    if not news in newValues:
        theSheet.insert_row([news,today])
        return True
    else:
        return False



