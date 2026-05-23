import os
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters

async def start(update, context):
    await update.message.reply_text("Hello! I am AJP Bot 🤖")

async def reply(update, context):
    await update.message.reply_text("I received your message!")

token = os.environ.get("BOT_TOKEN")
app = ApplicationBuilder().token(token).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, reply))
app.run_polling()
