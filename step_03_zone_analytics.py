from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T

spark = SparkSession.builder \
    .appName("ZoneAnalytics") \
    .master("local[*]") \
    .getOrCreate()

df_curated = spark.read \
    .parquet("data/curated/microsoft_repos")

df_analytics = df_curated.select(
    "*",
    F.current_date().alias("processed_at")
)

df_analytics.show()
df_analytics.printSchema()

df_analytics.write.mode("overwrite").parquet("data/analytics/microsoft_repos")

spark.stop()
