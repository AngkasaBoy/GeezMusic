from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Haiiiii Gays {bn} 🎵

Saya bisa memutar musik di panggilan suara grup Anda. Dikembangkan Oleh [Vckyyy](https://t.me/VckyouuBitch).

Tambahkan saya ke grup Anda dan mainkan musik dengan bebas!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Penjelasan Perintah Klik Disini", url="https://telegra.ph/text-04-11-2")
                  ],[
                    InlineKeyboardButton(
                        "✨ Group", url="https://t.me/VckyouuBitch"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Vckyouuu"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "⚡ Tambahkan Bot Ini Ke Grup Anda ⚡", url="https://t.me/{}?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Vckyouuu")
                ]
            ]
        )
   )


