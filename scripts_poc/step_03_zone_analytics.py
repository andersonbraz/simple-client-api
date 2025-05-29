from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T

import pandas as pd
import sqlite3

spark = SparkSession.builder \
    .appName("ZoneAnalytics") \
    .master("local[*]") \
    .getOrCreate()

df_curated = spark.read.parquet("data/curated/repos.parquet")

df_analytics = df_curated.select(
    "*"
)

df_analytics.show()
df_analytics.printSchema()

total_rows = df_analytics.count()
print("Total of", f"{format(total_rows, ',').replace(',', '.')} rows.")

df_analytics.write.mode("append").parquet("data/analytics/repos.parquet")

df_final = pd.read_parquet("data/analytics/repos.parquet")
conn = sqlite3.connect("github.db")
df_final.to_sql("repos", conn, if_exists="replace", index=False)

conn.commit()
conn.close()
# Close the Spark session
spark.stop()
