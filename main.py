
import pandas as pd
import sqlite3

df = pd.read_parquet("data/analytics/repos.parquet")
conn = sqlite3.connect("github.db")
df.to_sql("repos", conn, if_exists="replace", index=False)
