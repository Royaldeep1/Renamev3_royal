"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2 GB
	Price 0
	
	**💠 **Plan 1** 💠** 
	Daily  Upload  limit 20GB
	Price Rs 35 🇮🇳
	
	**💠 **Plan 2** 💠**
	Daily Upload limit 50GB
	Price Rs 80 🇮🇳 
	
	**💠 **Plan 3** 💠**
	Daily Upload limit 100GB
	Price Rs 190 🇮🇳
	
	__[For Indian Users Not For Other Countries Users.. ]__
	**Contact Devoloper For Payment Method...**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Devoloper 🇮🇳",url = "https://t.me/RoyalDwip")], 
        			[InlineKeyboardButton("Movies Channel",url = "https://t.me/worldofmovies8"),
        			InlineKeyboardButton("Movies Bot",url = "https://t.me/gopalbharbot")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["buy"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2 GB
	Price 0
	
	**💠 **Plan 1** 💠** 
	Daily  Upload  limit 20GB
	Price Rs 35 🇮🇳
	
	**💠 **Plan 2** 💠**
	Daily Upload limit 50GB
	Price Rs 80 🇮🇳 
	
	**💠 **Plan 3** 💠**
	Daily Upload limit 100GB
	Price Rs 190 🇮🇳
	
	__[For Indian Users Not For Other Countries Users.. ]__
	**Contact Devoloper For Payment Method...**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Devoloper 🇮🇳",url = "https://t.me/RoyalDwip")], 
        			[InlineKeyboardButton("Movies Channel",url = "https://t.me/worldofmovies8"),
        			InlineKeyboardButton("Movies Bot",url = "https://t.me/gopalbharbot")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
