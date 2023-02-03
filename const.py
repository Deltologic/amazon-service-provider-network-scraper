

import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_EMAIL = os.environ["ACCOUNT_EMAIL"]
ACCOUNT_PASSWORD = os.environ["ACCOUNT_PASSWORD"]
TOKEN_2FA = os.environ["TOKEN_2FA"]