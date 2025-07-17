from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def clean_trip_data(df: DataFrame) -> DataFrame:
    return df.filter((col("passenger_count")>0) & (col("trip_distance") >0))