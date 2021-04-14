# (c) @AbirHasan2005 | Thomas Shelby
# This is Telegram Messages Forwarder UserBot!
# Use this at your own risk. I will not be responsible for any kind of issue while using this!

# Re-edited by Mrvishal2k2 as per I need 
# Don't use  this (It's your own risk 🙄🤦😂)

import time
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserDeactivatedBan
from configs import Config

User = Client(session_name=Config.STRING_SESSION, api_hash=Config.API_HASH, api_id=Config.API_ID)

async def kanger(msg):
    await msg.edit(text="Forwarding Now ...")
    async for message in User.iter_history(chat_id=int(Config.FORWARD_FROM_CHAT_ID), reverse=True):
#        media = message.document or message.video or message.audio or message.photo 
        media = message.document or message.video
        if media:
            await asyncio.sleep(Config.SLEEP_TIME)
            try:
                 await message.copy(int(Config.FORWARD_TO_CHAT_ID))
            except FloodWait as e:
                print(f"#FloodWait: Stopping Forwarder for `{e.x}s`!")
                await asyncio.sleep(e.x)
                pass
            except UserDeactivatedBan:
                print("Congratulations!\nYour Account Banned Successfully!\nI already told you use a Fake Account. Hope you remember.")
                break
            except Exception as err:
                await User.send_message(chat_id=Config.OWNER, text=f"#ERROR: `{err}`")
        else:
            pass
    await msg.edit(text="Channel Files Successfully Kanged!\n\n©️ A Forwarder Userbot by @AbirHasan2005")


@User.on_message((filters.text) & ~filters.edited)
async def main(client, message):
    # Checks
    if message.text == "!start" and (message.from_user.id == int(Config.USER_ID)):
        await message.edit(text="Hi, Myself!\nThis is a Forwarder Userbot by @AbirHasan2005", parse_mode="Markdown",
                           disable_web_page_preview=True)
    elif message.text == "!help" and (message.from_user.id == int(Config.USER_ID)):
        await message.edit(
            text="This UserBot can forward messages from any Chat to any other Chat also you can kang all messages from one Chat to another Chat.\n\n👨🏻‍💻 **Commands:**\n• `!start`\n• `!help`\n• `!kang`\n\n©️ **Developer:** @AbirHasan2005\n👥 **Support Group:** [【★ʟя★】](https://t.me/linux_repo)",
            parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text.startswith("!kang") and (message.from_user.id == int(Config.USER_ID)):
        editable = await message.edit(
            text=f"Trying to Get All Messages from `{str(Config.FORWARD_FROM_CHAT_ID)}` and Forwarding to `{str(Config.FORWARD_TO_CHAT_ID)}` ...",
            parse_mode="Markdown", disable_web_page_preview=True)
        await asyncio.sleep(5)
        await kanger(editable)


User.run()
