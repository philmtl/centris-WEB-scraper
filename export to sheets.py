import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('centris.json', scope)
client = gspread.authorize(creds)
