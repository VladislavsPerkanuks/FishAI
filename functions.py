import base64
import os
from datetime import datetime

import numpy as np
import pandas as pd
from PIL import Image, ImageOps
from sys import platform


def haversine(lat1, lon1, lat2, lon2, to_radians=False, earth_radius=6371):
    """
    slightly modified version: of http://stackoverflow.com/a/29546836/2901002

    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees or in radians)

    All (lat, lon) coordinates must have numeric dtypes and be of equal length.

    """
    # print(type(lat1),type(lon1),type(lat2),type(lon2))
    if to_radians:
        lat1, lon1, lat2, lon2 = np.radians([lat1, lon1, lat2, lon2])

    a = np.sin((lat2 - lat1) / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1) / 2.0) ** 2

    return earth_radius * 2 * np.arcsin(np.sqrt(a))


def get_closest_location(latitude, longitude):
    # ja palaist no lokala datora
    # csv_path = ceļš/līdz/latvian_udenstiplnes.csv

    # ja ir uz servera
    if platform == "linux" or platform == "linux2":
        csv_path = '/home/vladislavs/PycharmProjects/fishai/latvian_udenstiplnes.csv'
    else:
        csv_path = 'latvian_udenstiplnes.csv'
    df = pd.read_csv(csv_path, sep=',', encoding='utf-8', index_col=0)
    df['dist'] = haversine(df['Latitude'], df['Longitude'], latitude, longitude)
    return df.sort_values(by=['dist']).head(1)['Nosaukums'].values[0]


def img_to_base64(bildite):
    with open(bildite, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return my_string.decode('utf-8')


def get_file_path(file):
    # ja palaist no lokala datora
    # file_path = ceļš uz jaunu folderi kur glābāsies visas iesūtītas fotogrāfijas

    # ja ir uz servera
    if platform == "linux" or platform == "linux2":
        file_path = os.path.join('/home/vladislavs/Desktop/zivis', file.filename)
    else:
        file_path = os.path.join('S:/Zivju_projeketelis/', file.filename)
    with Image.open(file) as im:
        image = ImageOps.exif_transpose(im)
        image.thumbnail((512, 512), Image.ANTIALIAS)
        image.save(file_path)

    return file_path


def get_today_date():
    # return datetime.now().strftime("%d.%m.%Y")
    return datetime.now().strftime("%Y-%m-%d")


def date_string_from_normal_to_db_format(date_string):
    return datetime.strptime(date_string, '%d.%m.%Y').strftime('%Y-%m-%d')


def date_string_from_db_to_normal_format(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d').strftime('%d.%m.%Y')


def split_string_to_array(string):
    b = []
    for x in string:
        x = x.replace("[", "")
        x = x.replace("]", "")
        x = x.replace('"', "")
        x = x.replace('"', "")
        x = x.replace("'", "")
        x = x.replace("'", "")
        x = (x.split(','))
        b.append([str(x[0]), float(x[1])])
    return b
