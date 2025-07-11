from pyspark.sql import DataFrame
from pyspark.sql.functions import when


def enrich_with_zone_names(df: DataFrame, zones: DataFrame) -> DataFrame:
    return df.join(
        zones,
        df["PULocationID"] == zones["LocationID"],
        how="left"
    ).withColumnRenamed("Zone","Pickup_Zone")

def add_distance_bucket(df: DataFrame) -> DataFrame:
    return df.withColumn(
        "distance_bucket",
        when(df.trip_distance < 2, "0-2 km")
        .when((df.trip_distance >=2) & (df.trip_distance <5), "2-5 km")
        .when((df.trip_distance>=5) & (df.trip_distance < 10), "5-10 km")
        .otherwise("10+ km")
    )
