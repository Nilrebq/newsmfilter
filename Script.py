#### This Code Was Devloped By _LinkZzz ####

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://dulink.in/')
    START_TXT = environ.get("START_TXT", "<b> ʜᴇʟᴏ {}\n\nᴍʏ ɴᴀᴍᴇ ɪꜱ <a href=https://t.me/Smritii_mandhanaa_bot>{SMRITI MANDHANA}</a>,ɪ ᴀᴍ ᴀ ᴀᴜᴛᴏꜰɪʟᴛᴇʀ + ᴍᴀɴᴜᴀʟ ꜰɪʟᴛᴇʀ + ꜰɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ. ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘᴍ ᴀʟsᴏ ! ᴀʟsᴏ ɪ ᴄᴀɴ sᴛᴏʀᴇ ꜰɪʟᴇs\n\n🍃ᴍʏ ᴏᴡɴᴇʀ : <a href=https://t.me/TalkWithadminzbot>ʙᴇʀʟɪɴ</a> </b>")
    HELP_TXT = """ʜᴇʏ {}
ʜᴇʀᴇ ɪꜱ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ."""
    ABOUT_TXT = """<b>𝗔𝗕𝗢𝗨𝗧 𝗠𝗦𝗚
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰ SMFILTER ❱═❍⊱❁۪۪
║┏━━━━━━━━━━━━━━━➣
║┣⪼ ADMIN - BERLIN 
║┣⪼ CREATOR - <a href=https://t.me/Talkwithadminzbot>BERLIN</a>
║┣⪼ LIBRARY - PYROGRAM
║┣⪼ LANGUAGE - PYTHON 4
║┣⪼ DATABASE - MONGO DB
║┣⪼ SERVER - HEROKU
║┣⪼ SOURCE - PAID ONLY
║┣⪼ BUILD STATUS - v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
║┗━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>"""
    SOURCE_TXT = """<b>𝐇𝐄𝐘 𝐁𝐑𝐔𝐇
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰ SMFILTER ❱═❍⊱❁۪۪
║┏━━━━━━━━━━━━━━━➣
║┣🎯✨ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sʀɪʟɪɴᴋs𝟺ᴋ ɴᴇᴛᴡᴏʀᴋ
║┣⚡️🍬ᴊᴏɪɴ ᴏᴜʀ ᴍᴏᴠɪᴇꜱ ᴄʜᴀɴɴᴇʟꜱ 🦋✨
║┗━━━━━━━━━━━━━━━➣
║┏━━━━━━━━━━━━━━━➣
║┣
║┣<a href=https://t.me/Srilinks4k>MAIN CHANNEL</a>
║┣
║┣<a href=https://t.me/+riua0Y3YXHo4NjY1>FILES GROUP</a>
║┣
║┣<a href=https://t.me/+-vgsERpDl5w0NDM9>STREAM LINKS GROUP</a>
║┣
║┣<a href=https://t.me/Srilinks4ksupport>SUPPORT GROUP</a>
║┣
║┗━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>"""
    MANUELFILTER_TXT = """ʜᴇʟᴩ: <b>ꜰɪʟᴛᴇʀꜱ</b>

• ꜰɪʟᴛᴇʀ ɪꜱ ᴛʜᴇ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ

<b>ɴᴏᴛᴇ:</b>
1. ꜰʟɪᴍꜱ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- SMFILTER Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. SMFILTER supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Srilinks4k)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of SMFILTER

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """⚡★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
⚡★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
⚡★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
⚡★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
⚡★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫-new 
    
<b>᚛› 𝐈𝐃⚡ - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞⚡ - {}</b>
"""
