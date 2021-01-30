from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('1. Cleanup') .getOrCreate()

requestLog_raw = spark.read.csv('../data/DataSample.csv', header = True)
requestLog_clean = requestLog_raw.dropDuplicates(['TimeSt', 'Latitude', 'Longitude'])

print("Total entries in request log: " + str(requestLog_raw.count()))
print("After cleaning, total entries in request log: " + str(requestLog_clean.count()))

requestLog_clean.repartition(1).write.csv("../Results/Cleanup")