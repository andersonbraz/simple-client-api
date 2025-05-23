from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.sql.functions import format_number

spark = SparkSession.builder \
    .appName("ZoneCurated") \
    .master("local[*]") \
    .getOrCreate()

df_raw = spark.read\
        .option("sep", ",")\
        .option("decimal", ".")\
        .option("header", "true")\
        .option("encoding", "UTF-8")\
        .csv("data/raw/repos.csv")

# Montando Zona CURATED

df_curated = df_raw.select(
    F.col("id").cast(T.IntegerType()),
    F.upper(F.split(F.col("full_name"), "/")[0]).alias("organization"),
    F.col("name").cast(T.StringType()),
    F.col("language").cast(T.StringType()),
    F.col("created_at").cast(T.TimestampType()),
    F.col("updated_at").cast(T.TimestampType()),
    F.col("size").cast(T.IntegerType()),
    F.col("stargazers_count").cast(T.IntegerType()),
    F.col("watchers_count").cast(T.IntegerType()),
    F.col("forks_count").cast(T.IntegerType()),
    F.col("open_issues_count").cast(T.IntegerType()),
    F.col("archived").cast(T.BooleanType()),
    F.col("disabled").cast(T.BooleanType()),
    F.col("visibility").cast(T.StringType()),
    F.current_date().alias("processed_at"),
)

df_curated.show(truncate=False)
df_curated.printSchema()

total_rows = df_curated.count()
print("Total of", f"{format(total_rows, ',').replace(',', '.')} rows.")

df_curated.write.mode("append").parquet("data/curated/repos.parquet")

spark.stop()