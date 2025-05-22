from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T

import pandas as pd
import sqlite3

spark = SparkSession.builder \
    .appName("ZoneAnalytics") \
    .master("local[*]") \
    .getOrCreate()

df_curated = spark.read \
    .parquet("data/curated/repos.parquet")

df_analytics = df_curated.select(
    "*"
)

df_analytics.show()
df_analytics.printSchema()

df_analytics.write.mode("overwrite").parquet("data/analytics/repos")


df_final = pd.read_parquet("data/analytics/repos")
conn = sqlite3.connect("github.db")
df_final.to_sql("repos", conn, if_exists="replace", index=False)

spark.stop()
