import math

def distance(origin, destination):
    """
    Calculate the Haversine distance in KM.
    Parameters: origin, destination
    Format: float (lat, long)
    Returns: distance_in_km : float
    """

    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 637
    

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) 
         * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    return d