from commands import *
from config import *
from datetime import datetime


updater = Updater(token=token)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('hello', hello))
dispatcher.add_handler(CommandHandler('hi', user_id))
dispatcher.add_handler(CommandHandler('summa', summa))
dispatcher.add_handler(CommandHandler('time', time))
dispatcher.add_handler(CommandHandler('time2', time2))
dispatcher.add_handler(CommandHandler('bad', bad))
dispatcher.add_handler(CommandHandler('test', test))
dispatcher.add_handler(CommandHandler('photo1', photo1))
dispatcher.add_handler(CommandHandler('photo2', photo2))
dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
updater.idle()


