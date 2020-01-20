import gspread
from oauth2client.service_account import ServiceAccountCredentials
from os import path


# id 必ずint型 message strでお願いします
def add_into_data(id,message):
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

    # 後でjsonファイル入れます
    fjb = path.join(path.dirname(__file__), 'fjb-g.json')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(str(fjb), scope)
    gc = gspread.authorize(credentials)
    wks = gc.open('fjb-g').sheet1

    # number only のとき死なないようにキャスト変換
    wks.update_acell('A'+str(id), str(message))

# 例
# add_into_data(1,"test read")
