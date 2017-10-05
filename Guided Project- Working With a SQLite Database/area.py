import sqlite3

conn = sqlite3.connect('factbook.db')

land = conn.execute('SELECT SUM(area_land) FROM facts').fetchall()[0]

water = conn.execute('SELECT SUM(area_water) FROM facts').fetchall()[0]

ratio = land[0] / water[0]

print(ratio)

conn.close()