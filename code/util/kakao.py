# kakao.py

import os
import requests
from dotenv import load_dotenv
from pprint import pprint

# .env에서 환경 변수 로드
load_dotenv()
KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")

if KAKAO_API_KEY is None:
    raise ValueError("⚠ KAKAO_API_KEY를 .env에서 불러오지 못했습니다.")


def get_coord_from_kakao(place_name: str):
    # 카카오맵 키워드 검색 API로 건물명 → (위도, 경도) 좌표 반환
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {"query": place_name}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if "documents" not in data or len(data["documents"]) == 0:
        print("검색 결과 없음:", place_name)
        return None

    doc = data["documents"][0]

    # Kakao API 좌표는 (x=경도, y=위도)
    lon = float(doc["x"])
    lat = float(doc["y"])

    return lat, lon


def get_all_coord(building_list):
    results = []

    for name in building_list:
        coord = get_coord_from_kakao(name)
        results.append({"name": name, "coord": coord})

    return results


if __name__ == "__main__":
    data = get_all_coord(
        [
            "충무로역 4호선",
            "동국대학교 서울 캠퍼스 후문",
        ]
    )
    pprint(data)
