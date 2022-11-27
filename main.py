import pyrogram, os, asyncio

try: app_id = int(os.environ.get("app_id", None))
except Exception as app_id: print(f"⚠️ App ID Invalid {app_id}")
try: api_hash = os.environ.get("api_hash", None)
except Exception as api_id: print(f"⚠️ Api Hash Invalid {api_hash}")
try: bot_token = os.environ.get("bot_token", None)
except Exception as bot_token: print(f"⚠️ Bot Token Invalid {bot_token}")
try: custom_caption = os.environ.get("custom_caption", "📂 File Name ➠  {file_name}\n\n🔘 𝑺𝒊𝒛𝒆 ➟ <i>{file_size}</i>\n\n〽️ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @tgnvs\n\nShare and Support us❤️\n\n🎯 𝐉𝐨𝐢𝐧 𝐍𝐨𝐰 👇\n\n<b>[🧲 ℂ𝕙𝕒𝕟𝕟𝕖𝕝 🧲](https://t.me/nvsmovielink)</b>\n\n<b>[🧩 𝐌ᴀɪ𝐍 𝐆ʀ𝐎ᴜ𝐏 🧩](https://t.me/+ONSD-vaHdJliOWQ9)</b>")
except Exception as custom_caption: print(f"⚠️ Custom Caption Invalid {custom_caption}")

AutoCaptionBot = pyrogram.Client(
   name="AutoCaptionBot", api_id=app_id, api_hash=api_hash, bot_token=bot_token)

start_message = """
<b>👋Hello {}</b>
<b>I am an AutoCaption bot</b>
<b>All you have to do is add me to your channel and I will show you my power</b>
<b>@tgnvs</b>"""

about_message = """
<b>• Name : [AutoCaption Bot](t.me/{username})</b>
<b>• Developer : [Muhammed](https://github.com/PR0FESS0R-99)
<b>• Language : Python3</b>
<b>• Library : Pyrogram v{version}</b>
<b>• Updates : <a href=https://t.me/tgnvs>Click Here</a></b>"""

@AutoCaptionBot.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
def start_command(bot, update):
  update.reply(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBot.on_callback_query(pyrogram.filters.regex("start"))
def strat_callback(bot, update):
  update.message.edit(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBot.on_callback_query(pyrogram.filters.regex("about"))
def about_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(about_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=about_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBot.on_message(pyrogram.filters.channel)
def edit_caption(bot, update: pyrogram.types.Message):
  if os.environ.get("custom_caption")
      motech, _ = get_file_details(update)
      try:
          try: update.edit(custom_caption.format(file_name=motech.file_name))
          except pyrogram.errors.FloodWait as FloodWait:
              asyncio.sleep(FloodWait.value)
              update.edit(custom_caption.format(file_name=motech.file_name, mote))
      except pyrogram.errors.MessageNotModified: pass 
  else:
      return
    
def get_file_details(update: pyrogram.types.Message):
  if update.media:
    for message_type in (
        "photo",
        "animation",
        "audio",
        "document",
        "video",
        "video_note",
        "voice",
        # "contact",
        # "dice",
        # "poll",
        # "location",
        # "venue",
        "sticker"
    ):
        obj = getattr(update, message_type)
        if obj:
            return obj, obj.file_id

def start_buttons(bot, update):
  bot = bot.get_me()
  buttons = [[
   pyrogram.types.InlineKeyboardButton("❤ Donation Link', url='https://upier.vercel.app/pay/tgnvs@airtel")
   ],[
   pyrogram.types.InlineKeyboardButton("Updates", url="t.me/tgnvs"),
   pyrogram.types.InlineKeyboardButton("About 🤠", callback_data="about")
   ],[
   pyrogram.types.InlineKeyboardButton("➕️ Add To Your Channel ➕️", url=f"http://t.me/{bot.username}?startchannel=true")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def about_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("🏠 Back To Home 🏠", callback_data="start")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

print("Telegram AutoCaption Bot Bot Start")
print("Bot Created By TGNVS")

AutoCaptionBot.run()
