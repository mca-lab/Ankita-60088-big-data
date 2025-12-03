from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

spark = SparkSession.builder \
    .appName("Data Cleaning") \
    .getOrCreate()

RAW_DIR = "/app/data/raw"
PROCESSED_DIR = "/app/data/processed"

# ===========================
# POPULATION CLEANING
# ===========================
population_df = spark.read.option("header", True).csv(
    f"{RAW_DIR}/population.csv"
)

population_cleaned = (
    population_df
    .withColumn(
        "population",
        expr("try_cast(Value as double)")
    )
    .withColumn(
        "population",
        expr("cast(round(population) as bigint)")
    )
    .filter(col("population").isNotNull())
    .select(
        col("Country Name").alias("country"),
        col("Country Code").alias("country_code"),
        col("Year").cast("int").alias("year"),
        col("population")
    )
)

population_cleaned.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(f"{PROCESSED_DIR}/population_cleaned")

print(" Population data cleaned successfully")

# ===========================
# CO2 CLEANING
# ===========================
co2_df = spark.read.option("header", True).csv(
    f"{RAW_DIR}/co2_emissions.csv"
)

co2_cleaned = (
    co2_df
    .withColumn("co2", expr("try_cast(Total as double)"))
    .filter(col("co2").isNotNull())
    .select(
        col("Year").cast("int").alias("year"),
        col("co2")
    )
)

co2_cleaned.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(f"{PROCESSED_DIR}/co2_cleaned")

print(" CO2 data cleaned successfully")

spark.stop()
