from dotenv import load_dotenv
import os
load_dotenv()


class Config:
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN") 
    SQLITE_DATABASE_PATH: str = os.getenv("SQLITE_DATABASE_PATH", "sqlite:///cryptbot.db")
    DUCKDB_DATABASE_PATH: str = os.getenv("DUCKDB_DATABASE_PATH", "duckdb://cryptbot.duckdb")