import os
from pathlib import Path

from pyspark.sql import SparkSession

POCKET_GITHUB_PATH   = os.getenv("POCKET_GITHUB_PATH", None) # @todo redo with our own project env var for path
POCKET_GITHUB_PARENT = Path(POCKET_GITHUB_PATH).parent if POCKET_GITHUB_PATH else None
RAW_CSV_FILE_PATH    = str(Path(POCKET_GITHUB_PARENT) / "pocket-analytics" / "infra" / "local_env" / "local_data" / "raw" / "AppleWatch - HeartRate StepCount etc 92406 rows - export20200620105726.csv")

spark = SparkSession.builder \
    .appName("raw-2-raw_DL") \
    .enableHiveSupport() \
    .getOrCreate()
    # .config("spark.sql.catalogImplementation", "hive") - @tbc already set by enableHiveSupport()

apple_watch_raw_df = spark.read.csv(RAW_CSV_FILE_PATH, header=True, inferSchema=True)

apple_watch_raw_df.summary()
apple_watch_raw_df.show()
