# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config(object):
    # Bot Information 
    TECH_VJ_BOT_TOKEN = os.environ.get("TECH_VJ_BOT_TOKEN", "7610132838:AAFCZHxS96lqIejFQAfjcRjnjhm-GHMPZb0")
    TECH_VJ_BOT_USERNAME = os.environ.get("TECH_VJ_BOT_USERNAME", "SDV_uploader_bot") # Bot username without @.
    
    # The Telegram API things
    TECH_VJ_API_ID = int(os.environ.get("TECH_VJ_API_ID", "23801870"))
    TECH_VJ_API_HASH = os.environ.get("TECH_VJ_API_HASH", "9645cfafdfc9be9a7a46fb4874992cf6")
    
    # the download location, where the HTTP Server runs
    TECH_VJ_DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # Telegram maximum file upload size
    TECH_VJ_MAX_FILE_SIZE = 50000000
    TECH_VJ_TG_MAX_FILE_SIZE = 4194304000 #2097152000
    TECH_VJ_FREE_USER_MAX_FILE_SIZE = 50000000
    
    # chunk size that should be used with requests
    TECH_VJ_CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    TECH_VJ_HTTP_PROXY = ""
    
    # maximum message length in Telegram
    TECH_VJ_MAX_MESSAGE_LENGTH = 4096
    
    # set timeout for subprocess
    TECH_VJ_PROCESS_MAX_TIMEOUT = 3600
    
    # your telegram account id
    TECH_VJ_OWNER_ID = int(os.environ.get("TECH_VJ_OWNER_ID", "5443679321")) 
    TECH_VJ_SESSION_NAME = "VJ-URL-UPLOADER-BOT"
    
    # database uri (mongodb)
    TECH_VJ_DATABASE_URL = os.environ.get("TECH_VJ_DATABASE_URL", "mongodb+srv://shivamsh:shivamsh@cluster0.f9ge884.mongodb.net/?retryWrites=true&w=majority")
    TECH_VJ_MAX_RESULTS = "50"

    # channel information
    TECH_VJ_LOG_CHANNEL = int(os.environ.get("TECH_VJ_LOG_CHANNEL", "-1002404940304")) # your log channel id and make bot admin in log channel with full right 
    
    # if you want force subscribe then give your channel id below else leave blank
    tech_vj_update_channel = environ.get('TECH_VJ_UPDATES_CHANNEL', '-1002071359028') # your update channel id and make bot admin in update channel with full right
    TECH_VJ_UPDATES_CHANNEL = int(tech_vj_update_channel) if tech_vj_update_channel and id_pattern.search(tech_vj_update_channel) else None  
    
    # Url Shortner Information 
    TECH_VJ = bool(environ.get('TECH_VJ', True)) # Set False If you want shortlink off else True
    TECH_VJ_URL = environ.get('TECH_VJ_URL', 'omegalinks.in') # your shortlink url domain or url without https://
    TECH_VJ_API = environ.get('TECH_VJ_API', 'd587f6def6b4974a2bed804b7452f694815f0ee4') # your url shortner api
    TECH_VJ_TUTORIAL = os.environ.get("TECH_VJ_TUTORIAL", "https://t.me/How_To_Open_Linkl")


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
