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

Tambahkan saya ke grup Anda dengan cara salin username saya lalu invite, jangan lupa invite juga @GeezMusicAssitant dengan bebas!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Untuk Penjelasan Perintah klik Disini", url="https://telegra.ph/text-04-11-2")
                  ],[
                    InlineKeyboardButton(
                        "✨ Pemilik", url="https://t.me/Vckyouubitch"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Vckyouuu"
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


