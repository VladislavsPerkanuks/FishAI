import base64
import os
from datetime import datetime
from PIL import Image, ImageOps


def img_to_base64(bildite):
    with open(bildite, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return my_string.decode('utf-8')


def get_file_path(file):
    file_path = os.path.join('/home/vladislavs/Desktop/zivis', file.filename)
    with  Image.open(file) as im:
        image = ImageOps.exif_transpose(im)
        image.thumbnail((512,512), Image.ANTIALIAS)
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
