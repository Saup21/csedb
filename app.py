import gspread
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
app.secret_key = 'csedepartmentdb'

#Google sheets database setup
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

gc = gspread.authorize(creds)

sheet = 'https://docs.google.com/spreadsheets/d/1_AKFcMxpkRS28innM0NxENfkihmlRn-nJWxNggCa_II/edit#gid=0'
#csedb
sh = gc.open_by_url(sheet)
sheet = sh.get_worksheet(0)
print(sheet.cell(1, 1))



if __name__ == '__main__':
    app.run(debug=True)
