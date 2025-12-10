# osrm.py

import requests
from util.cache import Cache


def get_osrm_route_cached(src, dst):
    osrm_cache = Cache("cache.json")  # 원하는 파일명
    cache_data = osrm_cache.load()
    key = Cache.make_key(src.name, dst.name)

    if key in cache_data:
        return cache_data[key]["duration"]

    duration = get_osrm_route(src.lat, src.lng, dst.lat, dst.lng)
    cache_data[key] = {"duration": duration}
    osrm_cache.save(cache_data)

    return duration


def get_osrm_route(src_lat, src_lng, dst_lat, dst_lng):
    url = (
        f"http://router.project-osrm.org/route/v1/foot/"
        f"{src_lng},{src_lat};{dst_lng},{dst_lat}"
        f"?overview=full&geometries=polyline"
    )

    res = requests.get(url).json()

    if "routes" not in res:
        return None, None

    route = res["routes"][0]

    duration = route["duration"]

    return duration
