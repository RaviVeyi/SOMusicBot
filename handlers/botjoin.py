from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["adding"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>ℹ️Məni əvvəlcə admim etməlisiniz.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 𝐀𝐬𝐢𝐬𝐬𝐭𝐚𝐧𝐬"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"İstəyinizlə Gəldim...🥳")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 𝐀𝐬𝐢𝐬𝐬𝐭𝐚𝐧𝐬 onsuzda qrupda var.</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>📛Gözləmə xətası.\n User {user.first_name} qrupa daxil ola bilmədiyindən, bot musiqi oxuda bilmir.\n {user.first_name}, Qrupda əvvəlcədən qadağan olmadığını yoxlayın,sonra yenidən cəhd edin."
            "\n\n və ya qrupa @TeleqramMusicAsisstant hesabını əlavə edin. </b>",
        )
        return
    await message.reply_text(
            "<b>𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 𝐀𝐬𝐢𝐬𝐬𝐭𝐚𝐧𝐬 onsuzda qrupda var.</b>",
        )
    
@USER.on_message(filters.group & filters.command(["leave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>İstifadəçi qrupunuzu tərk edə bilmədi!."
            "\n\nvə ya özünüz qrupdan çıxarın.</b>",
        )
        return
 
 
 
