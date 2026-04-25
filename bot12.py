import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
APK_MSG_ID = int(os.getenv("APK_MSG_ID"))
VIDEO_MSG_ID = int(os.getenv("VIDEO_MSG_ID"))
VOICE_MSG_ID = int(os.getenv("VOICE_MSG_ID"))

async def handle_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    user_id = user.id
    username = user.first_name  # 👈 user name

    try:
        # 👋 FIRST MESSAGE
        await context.bot.send_message(
            chat_id=user_id,
            text=f"""Hlo {username} 👋

Aapki request jldi hi approve ho jayegi ✅

Video aur hack APK neeche diya gaya hai 👇"""
        )

        # 🎬 VIDEO
        await context.bot.copy_message(
            chat_id=user_id,
            from_chat_id=CHANNEL_ID,
            message_id=VIDEO_MSG_ID
        )

        # 📦 APK
        await context.bot.copy_message(
            chat_id=user_id,
            from_chat_id=CHANNEL_ID,
            message_id=APK_MSG_ID
        )

        # 📩 LOSS RECOVER MESSAGE
        await context.bot.send_message(
            chat_id=user_id,
            text="""Loss recover karne ke liye message karlo mujhe aap 👇
https://t.me/m/x59DOH0UZDVl"""
        )

        # 🔊 VOICE LAST
        await context.bot.copy_message(
            chat_id=user_id,
            from_chat_id=CHANNEL_ID,
            message_id=VOICE_MSG_ID
        )

    except Exception as e:
        print(e)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(ChatJoinRequestHandler(handle_join))

app.run_polling()
