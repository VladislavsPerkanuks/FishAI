import base64
import os
from datetime import datetime


def img_to_base64(bildite):
    with open(bildite, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return my_string.decode('utf-8')

def get_file_path(file):
    file_path = os.path.join('S:\\Zivju_projeketelis\\', file.filename)
    file.save(file_path)
    return file_path

def get_today_date():
    #return datetime.now().strftime("%d.%m.%Y")
    return datetime.now().strftime("%Y-%m-%d")

def date_string_from_normal_to_db_format(date_string):
    return datetime.strptime(date_string, '%d.%m.%Y').strftime('%Y-%m-%d')

