import json
import os
import re
import pandas as pd
from datetime import datetime, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

PLAYLIST_JSON = os.path.join(SCRIPT_DIR, "playlist.json")
OUTPUT_XLSX = os.path.join(SCRIPT_DIR, "playlist_export.xlsx")

def extract_handle(entry: dict) -> str:
   
    h = entry.get("channel_handle")
    if h:
        return h if h.startswith("@") else "@" + h

    for key in ("uploader_url", "channel_url", "uploader_url_basename", "channel"):
        val = entry.get(key)
        if isinstance(val, str):
            m = re.search(r"/@([A-Za-z0-9._-]+)", val)
            if m:
                return "@" + m.group(1)

    val = entry.get("webpage_url")
    if isinstance(val, str):
        m = re.search(r"/@([A-Za-z0-9._-]+)", val)
        if m:
            return "@" + m.group(1)

    return ""

with open(PLAYLIST_JSON, "r", encoding="utf-8-sig") as f:
    data = json.load(f)

rows = []
for e in data.get("entries", []):
    if not e:
        continue

    video_id = e.get("id")
    video_url = e.get("webpage_url") or (
        f"https://www.youtube.com/watch?v={video_id}" if video_id else ""
    )

    upload_date = e.get("upload_date")
    if upload_date and len(upload_date) == 8:
        upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"

    upload_time_utc = ""
    ts = e.get("timestamp")
    if ts:
        upload_time_utc = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    channel_handle = extract_handle(e)

    rows.append({
        "Video URL": video_url,
        "Video Title": e.get("title") or "",
        "Video Description": e.get("description") or "",
        "Channel Name": e.get("channel") or e.get("uploader") or "",
        "Channel Handle": channel_handle,
        "Upload Date": upload_date or "",
        "Upload Time (UTC)": upload_time_utc,
    })

df = pd.DataFrame(rows)
df.to_excel(OUTPUT_XLSX, index=False)

print("SUCCESS ✅")
print(f"Videos exported: {len(df)}")
print(f"Excel created: {OUTPUT_XLSX}")
