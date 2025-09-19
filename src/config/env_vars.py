import os
from dotenv import load_dotenv

load_dotenv

GITHUB_URI = os.getenv("GITHUB_URI", "")
