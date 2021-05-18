import gspread
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, url_for, redirect
import time

app = Flask(__name__)
app.secret_key = 'csedepartmentdb'

#Google sheets database setup
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

gc = gspread.authorize(creds)

sheet_url = 'https://docs.google.com/spreadsheets/d/1_AKFcMxpkRS28innM0NxENfkihmlRn-nJWxNggCa_II/edit#gid=0'
#csedb
sh = gc.open_by_url(sheet_url)

#sheets header items
def cse_row():
    sheet = sh.sheet1
    row1 = sheet.row_values(1)
    return row1

#sheets data script not working so called directly from render_template function, need to fix it
# def cse_data():
#     sheet = sh.sheet1
#     data = sheet.get_all_records()
#     return data


@app.route('/')
def cse_data():
    return render_template('data.html', row=cse_row(), db=sh.sheet1.get_all_records())



if __name__ == '__main__':
    app.run(debug=False)
