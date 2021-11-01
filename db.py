import sqlite3
conn = sqlite3.connect('db.db', check_same_thread=False)
cur = conn.cursor()