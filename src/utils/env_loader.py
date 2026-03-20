import os
from dotenv import load_dotenv

import logging

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
logging.info(f"Loading environment variables from: {BASE_DIR}")
env = os.getenv("TEST_ENV", "dev")
env_path = os.path.join(BASE_DIR, "env", f".env.{env}")

load_dotenv(env_path)

class Env:
    BASE_URL = os.getenv("BASE_URL")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    BROWSER = os.getenv("BROWSER", "chromium")