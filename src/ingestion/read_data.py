from config import settings
from src.utils.spark_session import get_spark_session
from pyspark.sql import DataFrame

def read_trip_data() -> DataFrame:
    spark  = get_spark_session()
    return spark.read.parquet(settings.RAW_DATA_PATH)


def read_zone_lookup() -> DataFrame:
    spark = get_spark_session()
    return spark.read.option("header", True).csv(settings.ZONE_LOOKUP_PATH)
