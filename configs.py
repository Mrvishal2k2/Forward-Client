# (c) @AbirHasan2005

import os

class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = os.environ.get("STRING_SESSION")
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = os.environ.get("FORWARD_FROM_CHAT_ID", -1001458807892)
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = os.environ.get("FORWARD_TO_CHAT_ID", -1001283040775)
    # Your User ID
    USER_ID = os.environ.get("USER_ID", 1406976373)
    # Sleep Time while Kang
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 9))
    OWNER = os.environ.get("OWNER","Mrvishal_2k2")
    OFFSET = os.environ.get("OFFSET", 1)
