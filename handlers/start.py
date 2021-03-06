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
    await message.reply_photo("https://te.legra.ph/file/f25a47b16c4c0d19a580b.jpg")
    await message.reply_text(
        f"""<b>β¨ **ππ΄π»π²πΎπΌπ΄ {message.from_user.first_name}** \n
π₯ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) π°π»π»πΎπ ππΎπ ππΎ πΏπ»π°π πΌπππΈπ² πΈπ½ ππΎππ πΎπΏ πΆππΎππΏ π³π΄ππ΄π»πΎπΏπ΄π³ π±π @DARKAMAN !**

β‘ **π΅πΎπ πΈπ½π΅πΎ π°π±πΎππ π°π»π» π΅π΄π°ππππ΄.. πΉπππ πππΏπ΄ /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "β¨οΈΗΙΙ ΚΙ ΘΆΦ ΚΦΚΚ Ι’ΚΦΚΦβ¨οΈ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "β¨Ι¦ΦΥ‘ ΘΆΦ ΚΦΙ ΚΙβ¨", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "π₯³ΖΦΚΚΗΥΌΙΦπ₯³", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "β£οΈΖΚΙΗΘΆΙΚβ£οΈ", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "π₯°ΦΚΦΦΦΚΘΆ Ι’ΚΦΚΦπ₯°", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "π?π³ΚΦΙΗΘΆΙΦ ΖΙ¦ΗΥΌΥΌΙΚπ?π³", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "π±οΈΗΚΙΣΌΗ ΚΦΙ?ΦΘΆπ±οΈ", url="https://t.me/ALEXA_MANAGER_ROBOT")
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
    await message.reply_photo("https://te.legra.ph/file/f25a47b16c4c0d19a580b.jpg")
    await message.reply_text(
        f"""β **bot is running**\n<b>β‘ **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±οΈΦΚΦΦΦΚΘΆ Ι’ΚΦΚΦπ±οΈ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "π?π³ΚΦΙΗΘΆΙΦ ΖΙ¦ΗΥΌΥΌΙΚπ?π³", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo("https://te.legra.ph/file/f25a47b16c4c0d19a580b.jpg")
    await message.reply_text(
        f"""<b>ππ» **π·π΄π»π»πΎ** {message.from_user.mention()}</b>

**Please press the button below to read the explanation and see the list of available commands !**

β‘ __Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="π±οΈΙ¦ΦΥ‘ ΘΆΦ ΚΦΙ ΚΙπ±οΈ", callback_data="cbguide"
                    )
                ]
            ]
        ),
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_photo("https://te.legra.ph/file/f25a47b16c4c0d19a580b.jpg")
    await message.reply_text(
        f"""<b>π‘ Hello {message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β¨οΈΙ?ΗΦΙ¨Ζ ΖΚΙβ¨οΈ", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "β¨ΗΙΚΗΥΌΖΙΦ ΖΚΙβ¨", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π₯³ΗΙΚΙ¨ΥΌ ΖΚΙπ₯³", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "π₯°ΦΚΙΦ ΖΚΙπ₯°", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β£οΈΦΥ‘ΥΌΙΚ ΖΚΙβ£οΈ", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π±οΈΖΚΥΌ ΖΚΙπ±οΈ", callback_data="cbfun"
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
        "π₯ `ΦΙ¨ΥΌΙ’!!`\n"
        f"β‘οΈ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "π€ bot status:\n"
        f"β’ **uptime:** `{uptime}`\n"
        f"β’ **start time:** `{START_TIME_ISO}`"
    )
