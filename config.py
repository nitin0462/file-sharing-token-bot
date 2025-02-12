import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7214363967:AAHN5j-w_QDWwGzJg8VBq2WlzMUSOZFb-aA")

# Your API ID & API HASH from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28123695"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6fcc0acacee23599eaa91208c854e879")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002378421557"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6922646979"))

# Port
PORT = os.environ.get("PORT", "8585")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://folk:folk@cluster0.dyiy7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "cluster0")

# Shortener (token system)
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "48962cd7932756e4ea3948f9fdacbd982d4fae40
")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/+PZfHvzjSiZc4OGE1") # Shareus tutorial video

# Force sub channel ID, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "5197673717 5069922547 6695586027 6998097697").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join my Channel/Group to use me\n\nKindly Please join Channel</b>")

# Set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We LeakHubd or its subsidiary channel don't produce any of them.")

# Set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set True if you want to Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly. I'm only a File Sharing bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(5197673717)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
