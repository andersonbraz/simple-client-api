from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T

spark = SparkSession.builder \
    .appName("ZoneCurated") \
    .master("local[*]") \
    .getOrCreate()

df_raw = spark.read\
        .option("sep", ",")\
        .option("decimal", ".")\
        .option("header", "true")\
        .option("encoding", "UTF-8")\
        .csv("data/raw/microsoft_repos.csv")

# Montando Zona CURATED

df_curated = df_raw.select(
    F.col("id").cast(T.IntegerType()),
    F.upper(F.split(F.col("full_name"), "/")[0]).alias("organization"),
    F.col("name").cast(T.StringType()),
    F.col("language").cast(T.StringType()),
    F.col("created_at").cast(T.TimestampType()),
    F.col("updated_at").cast(T.TimestampType())
)

df_curated.show(truncate=False)
df_curated.printSchema()

df_curated.write.mode("overwrite").parquet("data/curated/microsoft_repos")

spark.stop()