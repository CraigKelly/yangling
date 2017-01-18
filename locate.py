"""Translate lat and long to a "standard" city name."""

from math import sin, cos, sqrt, atan2, radians

CITIES = {
    ("Edinburgh",        55.9533,   -3.1883),
    ("Karlsruhe",        49.0069,    8.4037),
    ("Montreal",         45.5017,  -73.5673),
    ("Waterloo",         43.4643,  -80.5204),
    ("Pittsburgh",       40.4406,  -79.9959),
    ("Charlotte",        35.2271,  -80.8431),
    ("Urbana-Champaign", 40.1106,  -88.2073),
    ("Phoenix",          33.4484, -112.0740),
    ("Las Vegas",        36.1699, -115.1398),
    ("Madison",          43.0731,  -89.4012),
}


def _dist(lat1, lon1, lat2, lon2):
    """Return distance in km between 2 lat/long pairs."""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return c * 6373.0


def closest(lat1, lon1):
    """Return distance (km) and city closest to given coords."""
    lat1, lon1 = float(lat1), float(lon1)

    min_dist, min_city = None, None
    for city, lat2, lon2 in CITIES:
        dist = _dist(lat1, lon1, lat2, lon2)
        if min_dist is None or dist < min_dist:
            min_dist, min_city = dist, city

    return min_dist, min_city
