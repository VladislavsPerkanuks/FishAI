import base64
import sqlite3
import os
import PIL


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def img_to_base64(bildite):
    with open(bildite, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return my_string.decode('utf-8')


def add_to_db(liet_id, bilde, zivs_id, datums, zvejas_vieta):
    try:
        connect.open_connection()
        sqlite_insert_blob_query = """ INSERT INTO Loms VALUES (Null, ?, ?, ?,?,?)"""
        data_tuple = (liet_id, bilde, zivs_id, datums, zvejas_vieta)
        connect.cur.execute(sqlite_insert_blob_query, data_tuple)
        connect.conn.commit()
        connect.close_connection()

        print("Image and file inserted successfully as a BLOB into a table")
    except sqlite3.Error as error:
        pass


class Connection:
    def __init__(self):
        self.conn = None
        self.connected = False
        self.cur = None
        self.cursor_opened = False

    def open_connection(self):
        if not self.connected:
            self.conn = sqlite3.connect('db.db', check_same_thread=False)
            self.cur = self.conn.cursor()
            self.connected = True

    def close_connection(self):
        if self.connected:
            self.cur.close()
            self.conn.close()
            self.connected = False

connect = Connection()