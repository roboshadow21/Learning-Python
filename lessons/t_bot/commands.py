import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from datetime import datetime


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Привет {update.effective_user.first_name}")


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}, {update.effective_user.id}')


def user_id(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Привет {update.effective_user.first_name} {update.effective_user.last_name}!')


def summa(update: Update, context: CallbackContext) -> None:
    msg = update.message.text.split()
    update.message.reply_text(f'Сумма = {int(msg[1]) + int(msg[2])}')


def time(update: Update, context: CallbackContext) -> None:
    current_time = str(datetime.now().time())[:-7]
    update.message.reply_text(f'Сейчас {current_time}')


def time2(update, context):
    t = datetime.now().time()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f'Точное время {str(t)[:-7]}')


def bad(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Никого нет дома!')


def test(update: Update, context: CallbackContext) -> None:
    msg = update.message.text.split()
    if msg[1] == 'привет':
        update.message.reply_text(f'Привет! Чем помочь?')
    else:
        update.message.reply_text(f'Я занят')


def photo1(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://yandex.ru/images/search?utm_source='
                           'main_stripe_big&text='
                           '%D0%A1%D0%BE%D0%B2%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BD%D1%8B%D0%B5&nl=1&source=morda')


def photo2(update, context):
    update.message.reply_text('https://yandex.ru/images/search?utm_source='
                           'main_stripe_big&text='
                           '%D0%A1%D0%BE%D0%B2%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BD%D1%8B%D0%B5&nl=1&source=morda')


def unknown(update, context):
    update.message.reply_text("Это что за команда?")