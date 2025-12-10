# cache.py

import json
import os


class Cache:
    def __init__(self, filename):
        ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        DATA_DIR = os.path.join(ROOT_DIR, "data")

        os.makedirs(DATA_DIR, exist_ok=True)

        self.path = os.path.join(DATA_DIR, filename)

    def load(self):
        if not os.path.exists(self.path):
            return {}
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, cache):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=4)

    @staticmethod
    def make_key(src_name, dst_name):
        return f"{src_name}|{dst_name}"
