"""Batch transformation job for the Analytics Data Platform."""
from __future__ import annotations

import argparse
from pyspark.sql import SparkSession, functions as F, types as T

SCHEMA = T.StructType([
    T.StructField("order_id", T.IntegerType(), False),
    T.StructField("customer_id", T.StringType(), False),
    T.StructField("order_ts", T.TimestampType(), False),
    T.StructField("country", T.StringType(), False),
    T.StructField("amount", T.DoubleType(), False),
    T.StructField("status", T.StringType(), False),
])


def transform(spark: SparkSession, source: str, target: str) -> None:
    df = spark.read.option("header", True).schema(SCHEMA).csv(source)
    clean = (
        df.filter(F.col("amount").isNotNull() & (F.col("amount") >= 0))
          .filter(F.col("status").isin("paid", "refunded"))
          .dropDuplicates(["order_id"])
          .withColumn("order_date", F.to_date("order_ts"))
          .withColumn("net_amount", F.when(F.col("status") == "refunded", -F.col("amount")).otherwise(F.col("amount")))
    )
    clean.write.mode("overwrite").partitionBy("order_date").parquet(target)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="data/raw/orders.csv")
    parser.add_argument("--target", default="data/processed/orders")
    args = parser.parse_args()
    spark = SparkSession.builder.appName("orders-transform").getOrCreate()
    try:
        transform(spark, args.source, args.target)
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
