import sqlite3
import pandas as pd

conn = sqlite3.connect('factbook.db')

print(conn.execute('SELECT name, population FROM facts ORDER BY population ASC LIMIT 10').fetchall())

conn.close()