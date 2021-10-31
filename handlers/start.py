from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import sudo_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ **Welcome {message.from_user.first_name}** \n
🔥 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝙰𝙻𝙻𝙾𝚆 𝚈𝙾𝚄 𝚃𝙾 𝙾𝙻𝙰𝚈 𝙼𝚄𝚂𝙸𝙲 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙾𝙿 𝙶𝚁𝙾𝚄𝙿 𝙼𝙰𝙳𝙴 𝙱𝚈 @DARKAMAN !**

⚡ **𝙵𝙾𝚁 𝙸𝙽𝙵𝙾 𝙰𝙱𝙾𝚄𝚃 𝙰𝙻𝙻 𝙵𝙴𝙰𝚃𝚄𝚁𝙴... 𝙹𝚄𝚂𝚃 𝚃𝚈𝙿𝙴 /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "♨️ǟɖɖ ʍɛ ȶօ ʏօʊʀ ɢʀօʊք♨️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "✨ɦօա ȶօ ʊֆɛ ʍɛ✨", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "🥳ƈօʍʍǟռɖֆ🥳", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "☣️ƈʀɛǟȶɛʀ☣️", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "🥰ֆʊքքօʀȶ ɢʀօʊք🥰", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🇮🇳ʊքɖǟȶɛֆ ƈɦǟռռɛʟ🇮🇳", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "🖱️ǟʟɛӼǟ ʀօɮօȶ🖱️", url="https://t.me/ALEXA_MANAGER_ROBOT")
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **bot is running**\n<b>💠 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🖱️ֆʊքքօʀȶ ɢʀօʊք🖱️", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🇮🇳ʊքɖǟȶɛֆ ƈɦǟռռɛʟ🇮🇳", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **𝙷𝙴𝙻𝙻𝙾** {message.from_user.mention()}</b>

**Please press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🖱️ɦօա ȶօ ʊֆɛ ʍɛ🖱️", callback_data="cbguide"
                    )
                ]
            ]
        ),
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>💡 Hello {message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♨️ɮǟֆɨƈ ƈʍɖ♨️", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "✨ǟɖʋǟռƈɛֆ ƈʍɖ✨", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🥳ǟɖʍɨռ ƈʍɖ🥳", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "🥰ֆʊɖօ ƈʍɖ🥰", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "☣️օառɛʀ ƈʍɖ☣️", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🖱️ƒʊռ ƈʍɖ🖱️", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🔥 `քɨռɢ!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
