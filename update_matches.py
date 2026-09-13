import os
import json
import requests
from datetime import datetime

today_date = datetime.now().strftime("%Y-%m-%d")
api_url = f"https://api-ar.ysscores.com/api/matches/matches_date_get/{today_date}/%5B%5D/%5B%5D/%5B%5D/D/180"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://ysscores.com/",
    "Accept": "application/json"
}

try:
    response = requests.get(api_url, headers=headers, timeout=15)
    if response.status_code == 200:
        data = response.json()
        with open("matches.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Mondepro Engine: Matches data updated successfully!")
    else:
        print(f"Mondepro Engine Error: API status code {response.status_code}")
except Exception as e:
    print(f"Mondepro Engine Exception: {e}")
