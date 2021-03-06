# (C) 2021 VeezMusic-Project

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME
from handlers.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>â¨ **đđ´đťđ˛đžđźđ´, đ¸'đź {query.message.from_user.mention}** \n
đĽ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) đ°đťđťđžđ đđžđ đđž đżđťđ°đ đźđđđ¸đ˛ đ¸đ˝ đđžđđ đžđż đśđđžđđż đłđ´đđ´đťđžđżđ´đł đąđ @DARKAMAN !**

âĄ **đľđžđ đ¸đ˝đľđžđđźđ°đđ¸đžđ˝ đ°đąđžđđ đ°đťđť đľđ´đ°đđđđ´.., đšđđđ đđđżđ´ /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "â¨ď¸ÇÉÉ ĘÉ ČśÖ ĘÖĘĘ É˘ĘÖĘÖâ¨ď¸", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "â¨ÉŚÖŐĄ ČśÖ ĘÖÉ ĘÉâ¨", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "đĽłĆÖĘĘÇĘÉÖđĽł", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "âŁď¸ĆĘÉÇČśÉĘâŁď¸", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "đĽ°ÖĘÖÖÖĘČś É˘ĘÖĘÖđĽ°", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "đŽđłĘÖÉÇČśÉÖ ĆÉŚÇŐźŐźÉĘđŽđł", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "đąď¸ÇĘÉÓźÇ ĘÖÉŽÖČśđąď¸", url="https://t.me/ALEXA_MANAGER_ROBOT")
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>đĄ Hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

âĄ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â¨ď¸ÉŽÇÖÉ¨Ć ĆĘÉâ¨ď¸", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "â¨ÇÉĘÇŐźĆÉÉ ĆĘÉâ¨", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đĽłÇÉĘÉ¨Őź ĆĘÉđĽł", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "đĽ°ÖĘÉÖ ĆĘÉđĽ°", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "âŁď¸ÖŐĄŐźÉĘ ĆĘÉâŁď¸", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đąď¸ĆĘŐź ĆĘÉđąď¸", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đď¸ÉŽŐŚĆÓ ČśÖ ÉŚÉĘÖđď¸", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>đŽ here is the basic commands</b>

đ§ [ GROUP VC CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name)Â - search video from youtube detailed
/vsong (video name)Â - download video from youtube detailed
/lyric - (song name) lyrics scrapper
/vk (song name) - download song from inline mode

đ§ [ CHANNEL VC CMD ]

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/admincache - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

âĄ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đď¸ÉŽÇĆÓđď¸", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>đŽ here is the advanced commands</b>

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/cache - refresh the admin cache
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

âĄ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đď¸ÉŽÇĆÓđď¸", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>đŽ here is the admin commands</b>

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/musicplayer (on / off) - disable / enable music player in your group
/b and /tb (ban / temporary ban) - banned permanently or temporarily banned user in group
/ub - to unbanned user you're banned from group
/m and /tm (mute / temporary mute) - mute permanently or temporarily muted user in group
/um - to unmute user you're muted in group

âĄ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đď¸ÉŽÇĆÓđď¸", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>đŽ here is the sudo commands</b>

/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic
/rmd - remove all downloaded files
/clean - Remove all raw files

âĄ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đď¸ÉŽÇĆÓđď¸", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>đŽ here is the owner commands</b>

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

đ note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

âĄ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đď¸ÉŽÇĆÓđď¸", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>đŽ here is the fun commands</b>

/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself
/tts (text) - text to speech

âĄ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đď¸ÉŽÇĆÓđď¸", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""â HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

âĄ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đąď¸ĆÖĘĘÇŐźÉ ĘÉ¨ÖČśđąď¸", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đĆĘÖÖÉđď¸", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**đĄ here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â¸ pause", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "âśď¸ resume", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "âŠ skip", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "âš end", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "â anti cmd", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đ group tools", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đ Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>

đĄ **Feature:** this feature contains functions that can ban, mute, unban, unmute users in your group.

and you can also set a time for the ban and mute penalties for members in your group so that they can be released from the punishment with the specified time.

â **usage:**

1ď¸âŁ ban & temporarily ban user from your group:
   Âť type `/b username/reply to message` ban permanently
   Âť type `/tb username/reply to message/duration` temporarily ban user
   Âť type `/ub username/reply to message` to unban user

2ď¸âŁ mute & temporarily mute user in your group:
   Âť type `/m username/reply to message` mute permanently
   Âť type `/tm username/reply to message/duration` temporarily mute user
   Âť type `/um username/reply to message` to unmute user

đ note: cmd /b, /tb and /ub is the function to banned/unbanned user from your group, whereas /m, /tm and /um are commands to mute/unmute user in your group.

âĄ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đď¸ÉŽÇĆÓđď¸", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>
        
**đĄ Feature:** delete every commands sent by users to avoid spam in groups !

â usage:**

 1ď¸âŁ to turn on feature:
     Âť type `/delcmd on`
    
 2ď¸âŁ to turn off feature:
     Âť type `/delcmd off`
      
âĄ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đď¸É˘Ö ÉŽÇĆÓđď¸", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>đĄ Hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

âĄ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â¨ď¸ÉŽÇÖÉ¨Ć ĆĘÉâ¨ď¸", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "â¨ÇÉĘÇŐźĆÉÉ ĆĘÉâ¨", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đĽłÇÉĘÉ¨Őź ĆĘÉđĽł", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "đĽ°ÖĘÉÖ ĆĘÉđĽ°", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "âŁď¸ÖŐĄŐźÉĘ ĆĘÉâŁď¸", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đąď¸ĆĘŐź ĆĘÉđąď¸", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đď¸ÉŽÇĆÓđď¸", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""â HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

âĄ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đď¸ÉŽÇĆÓđď¸", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
