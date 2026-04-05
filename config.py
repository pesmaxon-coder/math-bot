import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8703148768:AAHPkZrlJsg-2Rr0iMJPldFlTi2ffGv7jtk")

ADMIN_IDS = [5420944421, 582974676]  # O'z Telegram ID ingiz

# Majburiy a'zo bo'lish kanallari - o'zingiznikini yozing
REQUIRED_CHANNELS = [
    {
        "name": "English Team LC",
        "username": "@vestelop",
        "url": "https://t.me/vestelop"
    },
    {
        "name": "Abbos Mehmonaliyev",
        "username": "@karetsop",
        "url": "https://t.me/karetsop"
    },
]

DB_PATH = os.getenv("DB_PATH", "/app/data/mathbot.db")
CERT_DIR = "certificates"
DEFAULT_AUTHOR = "Test Muallifi"
