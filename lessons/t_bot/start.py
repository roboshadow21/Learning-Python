from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from commands import *

# def hello(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5159704813:AAHhPWKp9RbyGk4a4F5SEhwphAPiwxGXfvk')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()

# first_test_dreamer_bot
# fancy_bot