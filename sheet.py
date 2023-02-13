import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("telenews_key.json",scope)
client = gspread.authorize(creds)
sheetSe = client.open("telebot se news").sheet1

# Initialize a list to store the values
values = sheetSe.col_values(1)
values=[str(val) for val in values]
newValues=values[0:2]
# Loop through the rows and append the value in the first column to the list


print(newValues)