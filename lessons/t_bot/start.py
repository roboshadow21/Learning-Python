from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from commands import *


updater = Updater('')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('hi', user_id))
updater.dispatcher.add_handler(CommandHandler('summa', summa))
updater.dispatcher.add_handler(CommandHandler('time', time))
updater.dispatcher.add_handler(CommandHandler('bad', bad))
updater.dispatcher.add_handler(CommandHandler('test', test))

updater.start_polling()
updater.idle()

# first_test_dreamer_bot
# fancy_bot
