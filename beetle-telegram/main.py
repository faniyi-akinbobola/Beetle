import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from commands import Command

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Alright talk to me!")

if __name__ == '__main__':
    application = ApplicationBuilder().token("7409868027:AAGGBtdVO0FHJxLuCQ9zFafakEupPHIL2ps"
).build()
    
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler("help", help)
    application.add_handlers([start_handler, help_handler])  
    application.run_polling()