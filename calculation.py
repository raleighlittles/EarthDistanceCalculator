import geopy.distance
import math



def euclidean_distance(lat_A, lon_A, lat_B, lon_B):
    return round( math.sqrt( (lat_B - lat_A)**2 + (lon_B - lon_A)**2 ), 3)

def great_circle_distance(lat_A, lon_A, lat_B, lon_B):
    return round( geopy.distance.great_circle((lat_A, lon_A), (lon_B, lon_B)).km, 4)

def vincenty_distance(lat_A, lon_A, lat_B, lon_B):
    return round( geopy.distance.vincenty( (lat_A, lon_A), (lon_B, lon_B )).km, 4)

def compute_percentage_error(euclid, greatcircle, vincenty):
    euclid_vicenty_error = percent_error(euclid, vincenty)
    print (euclid_vicenty_error)
    greatcircle_vincenty_error = percent_error(greatcircle, vincenty)
    print (greatcircle_vincenty_error)
    return [euclid_vicenty_error, greatcircle_vincenty_error]

def percent_error(measured, expected):
    return round((math.fabs((measured - expected) / expected) * 100), 3)

