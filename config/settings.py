import os
BASE_DIR = r"C:\Users\ShreyaSwain\OneDrive - Atyeti Inc\Desktop\etl_proj\etl_proj_nyc_taxi_trip"


DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_PATH = os.path.join(DATA_DIR, "raw", "yellow_tripdata_2025-01.parquet")
ZONE_LOOKUP_PATH = os.path.join(DATA_DIR, "zone_lookup", "taxi+_zone_lookup.csv") 

OUTPUT_DIR = os.path.join(BASE_DIR, "output")
CLEANED_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "cleaned")
DELTA_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "delta")
LOG_DIR = os.path.join(OUTPUT_DIR, "logs")
