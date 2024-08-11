from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils import bot_sys_stats
from VIPMUSIC.utils.inline.extras import botplaylist_markup
from VIPMUSIC.utils.decorators.language import language
from config import BANNED_USERS, PING_IMG_URL
import aiohttp
import asyncio

 
@app.on_message(filters.command(["mping", "malive"]) & ~BANNED_USERS & filters.group)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    start = datetime.now()
    pytgping = await VIP.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit(
        _["ping_2"].format(
            resp,
            app.mention,
            UP,
            RAM,
            CPU,
            DISK,
            pytgping,
        ),
        reply_markup=InlineKeyboardMarkup(botplaylist_markup(_)),
        )
