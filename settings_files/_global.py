import os
from dotenv import load_dotenv

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR, 'data')
IMAGES_DIR = os.path.join(ROOT_DIR, 'images')

# ----- IDs
load_dotenv()
GUILD_ID = int(os.getenv("GUILD_ID", False))
APPLICATION_ID = int(os.getenv("APPLICATION_ID", False))
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")

# ----- COLORES
EMBEDS_COLOR = 0x55FFFF
