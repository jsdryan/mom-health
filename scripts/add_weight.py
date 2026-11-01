"""把一筆體重寫進 data.json（同一天重複送會覆蓋）。

用法：KG=62.3 DATE=2026-11-05 python scripts/add_weight.py
DATE 留空時用台灣時間的今天。
"""
import datetime as dt
import json
import os
import re
import sys

kg_raw = os.environ.get("KG", "").strip().replace(",", ".")
date = os.environ.get("DATE", "").strip()

try:
    kg = round(float(re.sub(r"[^\d.]", "", kg_raw)), 2)
except ValueError:
    sys.exit(f"體重格式錯誤：{kg_raw!r}")
if not 25 <= kg <= 200:
    sys.exit(f"體重超出合理範圍：{kg}")

if not date:
    date = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
    sys.exit(f"日期格式錯誤，需要 yyyy-MM-dd：{date!r}")
try:
    dt.date.fromisoformat(date)
except ValueError:
    sys.exit(f"日期不存在：{date!r}")

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

weights = data.get("weights", [])
same = next((w for w in weights if w["date"] == date), None)
if same:
    same["kg"] = kg
else:
    weights.append({"date": date, "kg": kg})
weights.sort(key=lambda w: w["date"])
data["weights"] = weights

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"{date} {kg} 公斤")
