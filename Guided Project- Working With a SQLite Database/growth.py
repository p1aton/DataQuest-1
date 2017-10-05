import pandas as pd
import sqlite3
import math

conn = sqlite3.connect('factbook.db')

query = "SELECT * FROM facts"

facts = pd.read_sql_query(sql=query, con=conn)

conn.close()

facts = facts[facts['area_land'] > 0]

def pop_growth(row):
    new_pop = row['population'] * math.e **((row['population_growth']/100) * 35)
    return new_pop
facts['2050'] = facts.apply(pop_growth, axis=1)

print(facts['2050'])