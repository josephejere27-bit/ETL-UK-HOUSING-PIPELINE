import pandas as pd
import sqlite3

# --- EXTRACT ---
df = pd.read_csv('average-house-prices.csv')
print("Data extracted successfully")
print(df.head())

# --- TRANSFORM ---
df = df.dropna()
df = df[df['Region_Name'] == 'England']
df.columns = ['date', 'region_name', 'average_price']
df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df['average_price'] = df['average_price'].astype(int)
print("Data transformed successfully")
print(df.head())

# --- LOAD ---
conn = sqlite3.connect('housing_data.db')
df.to_sql('house_prices', conn, if_exists='replace', index=False)
conn.close()
print("Data loaded into SQLite database successfully")