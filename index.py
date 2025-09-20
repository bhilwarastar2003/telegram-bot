from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📢 #news\n"
        "💎 #ton\n"
        "💰 #btc\n"
        "📚 #educational\n\n"
        "✅ GENUINE SERVICE AVAILABLE ✅\n"
        "🔥 ONLY PAID SERVICE 🔥\n\n"
        "💃 Sexy & Hot Service Available 💃\n\n"
        "🍓 https://t.me/+3OsXCKGgVjQxYTA1\n"
        "🍑 https://t.me/+3OsXCKGgVjQxYTA1\n"
        "💦 https://t.me/+3OsXCKGgVjQxYTA1\n"
        "💋 https://t.me/+3OsXCKGgVjQxYTA1\n"
        "🔥 https://t.me/+3OsXCKGgVjQxYTA1\n\n"
        "DM for PRIVATE 👉 https://t.me/+3OsXCKGgVjQxYTA1 😘🔥"
    )

    await update.message.reply_text(text, disable_web_page_preview=True)

# Main
if __name__ == "__main__":
    TOKEN = "7950030892:AAHHhkgJtTHPDA8_K0kOCtZgxLfcTc0HPRA"  # apna token dalna

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot is running...")
    app.run_polling()
