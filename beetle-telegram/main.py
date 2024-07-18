import logging
from telegram import Update
import telegram
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram import Bot
import random
from datetime import datetime


# Defining poems as multiline strings
poem1 = """I can tell that you've never been true to me
I can smell that you're acting so fearfully
I can hear what you're hoping I want to hear
I can feel the alarm bells are ringing in me
I can touch but I know you don't feel a thing
I can pray but I know you commit a sin
I can sense now it's all become clear to see
You're no good, and you mean no good treacherously"""

poem2 = """
To every man there is a cause which he would gladly die for
Defend the right to have a place to which he can belong to
And every man will fight with his bare hands in desperation
And shed his blood to stem the flood, to barricade invasion

"""

poem3 = """
Game on, get your game on
Come on ya better play your cards right
Game on, get your game on
We'll make the grade and win this fight
"""

#creating a list of poems
lyrics = [poem1, poem2, poem3]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Asynchronous function to handle the start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello,I'm a bobbot")


# Asynchronous function to handle the help command
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
    Here's a list of all the available commands.
    Please type one of these commands:
        *start* : greetings
        *date_time* : show date & time
        *poem* : returns a random poem
        *about*: what you can do
        *help* : displays the available commands""")

# Asynchronous function to handle the poem command
async def poem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = random.randint(0,2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=lyrics[number])

# Asynchronous function to handle the date_time command
async def date_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_date = datetime.now()
    output = "Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{output}")

# Asynchronous function to handle the start command
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="""
    I'm excited to introduce you to bobbot, a Telegram bot designed to recieve commands.
    use the "/help" command to see the available commands.
""")

if __name__ == '__main__':
    application = ApplicationBuilder().token("7409868027:AAGGBtdVO0FHJxLuCQ9zFafakEupPHIL2ps"
).build()
    
    # Define command handlers for each command
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    poem_handler = CommandHandler('poem', poem)
    date_time_handler = CommandHandler('date_time', date_time)
    about_handler = CommandHandler('about', about)


    #  Add handlers to the application
    application.add_handlers([start_handler, help_handler, poem_handler, date_time_handler, about_handler])  
    application.run_polling()

