# Spark Session
from pyspark.sql import SparkSession

spark = (
    SparkSession
    .builder
    .appName("Cluster Execution")
    .getOrCreate()
)

df = spark.range(10)

df.write.format("csv").option("header", True).save("/data/output/15/6/range.csv")