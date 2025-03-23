from pyspark.sql.types import StructType, StructField, StringType, DoubleType

raw_schema = StructType([
    StructField("event_id",     StringType()),
    StructField("user_id",      StringType()),
    StructField("usage_type",   StringType()),
    StructField("amount",       DoubleType()),
    StructField("unit",         StringType()),
    StructField("timestamp",    StringType())
])
