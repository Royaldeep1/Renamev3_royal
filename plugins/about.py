import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["help"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"**Hey, {message.from_user.mention }\nHere is My Help Section..\n\nSimple File Rename Bot 🔗\n\nMore Feature Coming Soon.... \n\nAnd Url Uploader Bot Coming Soon \nFor More Update @RoyalDwip\n\nHow To Use!! @RoyalRenamexBot\n\nSend Any File Or Document On Bot!! \n\nAnd Send New Name For Rename It Easily 😌\n\nDevoloper From India 🇮🇳\n\nNote - This Bot Make For Indian Users Only Not For Other Countries.\nLike Bd, Pak, Nepal, Etc.\n\nReport Here For Any Problem @RoyalDwip 🇮🇳**",quote=True)
