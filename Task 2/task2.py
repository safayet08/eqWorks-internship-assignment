import math

def distance(origin, destination):
    """
    Calculate the Haversine distance.
    Parameters
    ----------
    origin : tuple of float (lat, long)
    destination : tuple of float (lat, long)

    Returns
    -------
    distance_in_km : float
    """
    
    print(origin)
    print(destination)

    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) 
         * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d



from pyspark.sql import SparkSession, types
from pyspark.sql.functions import *

spark = SparkSession.builder.appName('2. Label') .getOrCreate()

requestLogs = spark.read.csv('data/DataSample.csv', header = True)
poiList = spark.read.csv('data/POIList.csv', header = True)

poi_latitude = []
poi_longitude = []

for row in poiList.rdd.collect():
    poi_latitude.append(float(row.Latitude))
    poi_longitude.append(float(row.Longitude))
    
# Distance function works perfect
print(distance((poi_latitude[0], poi_longitude[0]), 
               (poi_latitude[3], poi_longitude[3])))

