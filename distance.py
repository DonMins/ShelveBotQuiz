import math
def distance(lat1, lon1, lat2, lon2):
    l = 6371
    lat1 = math.radians(float(lat1))
    lat2 = math.radians(float(lat2))
    lon1  = math.radians(float(lon1))
    lon2 = math.radians(float(lon2))
    dist = l * math.acos(math.sin(lat1) * math.sin(lat2) +
                math.cos(lat1) * math.cos(lat2) * math.cos(-lon1 + lon2))
    return dist


def score(dist):
    atom = 0.00012
    score = int(20 * (math.tan(-dist*atom + 1.5) + math.sqrt(3))/3)
    return score

