from pyspark.sql import SparkSession

def get_spark_session(app_name="NYC Taxi ETL"):
    return SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.extensions","io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog","org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .getOrCreate()

        

    

    