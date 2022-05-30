from pyspark.sql import SparkSession

def concatenation():
    spark = SparkSession.builder.getOrCreate()

    dataframe = spark.read\
        .option('header',True)\
        .option('escape','"')\
        .csv("./data/A_lvr_land_A.csv")
    
    dataframe.printSchema()
concatenation()
