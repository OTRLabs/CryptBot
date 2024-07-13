from dotenv import load_dotenv
import os
load_dotenv()


class Config:
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN") 