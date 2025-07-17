from config import settings
from pyspark.sql import DataFrame


def write_to_delta(df: DataFrame):
    df.write.format("delta").mode("overwrite").save(settings.DELTA_OUTPUT_PATH)


def write_cleaned_parquet(df: DataFrame):
    df.write.mode("overwrite").parquet(settings.CLEANED_OUTPUT_PATH)