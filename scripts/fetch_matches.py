import os
import json
import requests
from datetime import datetime
import schedule
import time

# إعدادات تلجرام
TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    try:
        requests.post(url, data=payload)
    except:
        pass

def fetch_and_save_matches():
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
            error_msg = f"API error: status code {response.status_code}"
            print(error_msg)
            send_telegram_message(f"خطأ في جلب البيانات: {error_msg}")
    except requests.exceptions.RequestException as e:
        error_msg = f"Exception: {e}"
        print(error_msg)
        send_telegram_message(f"حدث استثناء: {error_msg}")

def job():
    fetch_and_save_matches()

# جدولة المهمة كل يوم على سبيل المثال
schedule.every().day.at("09:00").do(job)

if __name__ == "__main__":
    print("Starting schedule...")
    while True:
        schedule.run_pending()
        time.sleep(60)
