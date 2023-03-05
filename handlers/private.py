from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph//file/b43a6777263d5dc68390e.jpg",
                caption=(f"""**Salam {message.from_user.mention}. Mənim adım [𝐅𝐀𝐒𝐓 𝐌𝐔𝐒İ𝐂 🇦🇿](https://t.me/TeleqrammusicBot)\n\nℹ️Mənim {bot} bəzi faydalı xüsusiyyətləri olan teleqram musiqi botuyam.iQrup'lara əlavə edərək musiqi dinləyə bilərsiniz.\n\n⚡️Məni qruplarınıza əlavə etməkdən çəkinməyin.\n🤖𝐃𝐢𝐠ə𝐫 𝐁𝐨𝐭𝐥𝐚𝐫 :@Teleqrambots\n🎙𝐊𝐚𝐧𝐚𝐥 : @Teleqrambots **"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕Qʀᴜᴘᴀ ƏʟᴀᴠƏ ᴇᴛ➕", url=f"https://t.me/TeleqrammusicBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ƏᴍʀʟƏʀ 📚", callback_data= "cbbilgi"
                    ),
                    #InlineKeyboardButton(
                    #    "📑 Təkliflər", url="https://t.me/Hasbullahh"
                   # )
                ],
 #               [
  #                  InlineKeyboardButton(
   #                     "Sꜱᴀʜɪʙ🙎", url="https://t.me/lamRavi"
    #                )
     #           ],
                 [
                    InlineKeyboardButton(
                        "Sꜱᴀʜɪʙ🙎", url="https://t.me/lamRavi"
                    ),
                    InlineKeyboardButton(
                        "ᴋᴀɴᴀʟ 📺" , url="https://t.me/Teleqrambots"
                    )
                ]
                
           ]
        )
    )
  


@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text("**Bot'un Əmrlər üçün?.Bot'a daxil olub.**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "↬Bota Get↫", url="https://t.me/TeleqrammusicBot?start=start"),                     
                     InlineKeyboardButton(
                         "📑 ᴛƏᴋʟɪꜰʟƏʀ", url="https://t.me/lamRavi")
                 ],[
                     InlineKeyboardButton(
                         "➕Qʀᴜᴘᴀ ƏʟᴀᴠƏ ᴇᴛ➕", url=f"https://t.me/TeleqrammusicBot?startgroup=true")
                 ]
             ]
         )
    )
    
#**Salam {message.from_user.mention}. Mənim adım [𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐌𝐔𝐒𝐈𝐂](https://t.me/TeleqrammusicBot)\n\nℹ️Mənim {bot} bəzi faydalı xüsusiyyətləri olan teleqram musiqi botuyam. @lamRavi-dan dəsdək alaraq yaradılmışam. Qrup'lara əlavə edərək musiqi dinləyə bilərsiniz.\n\n⚡️Məni qruplarınıza əlavə etməkdən çəkinməyin.   
@Client.on_callback_query(filters.regex("herkess"))
async def herkess(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam {message.from_user.mention}. Mənim adım [𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐌𝐔𝐒𝐈𝐂](https://t.me/TeleqrammusicBot)\n\nℹ️Mənim {bot} bəzi faydalı xüsusiyyətləri olan teleqram musiqi botuyam. @lamRavi-dan dəsdək alaraq yaradılmışam. Qrup'lara əlavə edərək musiqi dinləyə bilərsiniz.\n\n⚡️Məni qruplarınıza əlavə etməkdən çəkinməyin.""",
    reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("➕Qʀᴜᴘᴀ ƏʟᴀᴠƏ ᴇᴛ➕", url=f"https://t.me/TeleqrammusicBot?startgroup=true" )],
             [InlineKeyboardButton("ƏᴍʀʟƏʀ 📚", callback_data= "cbbilgi")],
            # [InlineKeyboardButton("Sahib💥", url="https://t.me/Hasbullahh")],
             [InlineKeyboardButton("ꜱᴀʜɪʙ🙎", url="https://t.me/lamRavi"),
              InlineKeyboardButton("ᴋᴀɴᴀʟ 📺" , url="https://t.me/Teleqrambots")]]))    
   
@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text("ℹ️Bot səsdə musiqi oxuması üçün lazım olan yetkilər.\n\n\n•━━━━━━━━•••━━━━━━━━•\n✅Mesaj Silmə.\n✅Bağlantı ilə dəvət etmə.\n✅Səsli söhbəti yönətmə.\n•━━━━━━━━•••━━━━━━━━•", 
    reply_markup=InlineKeyboardMarkup(
      [[InlineKeyboardButton("ʙᴏᴛ ƏᴍʀʟƏʀi🤖",callback_data ="herkes"),
         InlineKeyboardButton("ᴀᴅᴍɪɴ ƏᴍʀʟƏʀɪ👮",callback_data ="admin")],
        [InlineKeyboardButton("◀️ɢᴇʀi", callback_data="herkess")]])) 


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b> {query.from_user.mention} Bot Əmrləri🤖' Əmrlər aşağıda qeyid olunub⚡️\n\n\n•━━━━━━━━•••━━━━━━━━•\n/play - Qrupda musiqi oxutmaq üçün isdifadə olunan əmr.\n\n/song - İstədiyiniz musiqi adı ve ya bi hissəsin yazın, mp3 şəkildə musiqi yükləmək üçün isdifadə olunan əmr.\n\n/download - İstədiyiniz video adı ve ya bi hissəsin yazın, mp4 şəkildə video yükləmək üçün isdifadə olunan əmr.\n\n/link - Link şəkildə musiqi axtarmaq üçün lazım olan əmr.\n\n/help - Qrup & Şəxsidə əmrlər üçün lazım olan əmr.\n\n/id - Qrup & Şəxs id.\n\n/leave - Asisstant hesabı qrupdan çıxarmaq üçün isdifadə olunan əmr.</b>""",
    reply_markup=InlineKeyboardMarkup(
             [[InlineKeyboardButton("️◀️ɢᴇʀi",callback_data="cbbilgi")]]))


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b> {query.from_user.mention}'Admin Əmrləri👮' Ərmlər aşağıda qeyid olunub⚡️\n\n\n•━━━━━━━━•••━━━━━━━━•\n/authority - İstifadəçinin botun 'Admin Əmrləri👮' əmrlərindən istifadə edmə yetkisini ver.\n\n/unauthorized - İstifadəçinin botun 'Admin Əmrləri👮' əmrlərindən istifadə edmə yetkisini al.\n\n/skip - Sırada gözləyən musiqi oynatmaqa başlat.\n\n/resume - Musiqini oxutmağa davam edir.\n\n/end - Oxuyan musiqini dayandır.\n\n/adding - Asisstant hesabı qrupa qoşmaq üçün, lazım olan əmr.\n\n/reload - Botu yenidən başlad.</b>""",
    reply_markup=InlineKeyboardMarkup(
             [[InlineKeyboardButton("️◀️ɢᴇʀi", callback_data="cbbilgi")]]))
    
    
