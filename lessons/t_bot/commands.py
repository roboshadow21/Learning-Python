from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}, {update.effective_user.id}')


def user_id(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Привет {update.effective_user.first_name} {update.effective_user.last_name}!')


def summa(update: Update, context: CallbackContext) -> None:
    msg = update.message.text.split()
    update.message.reply_text(f'Сумма = {int(msg[1]) + int(msg[2])}')


def time(update: Update, context: CallbackContext) -> None:
    current_time = datetime.now().time()
    update.message.reply_text(f'Сейчас {current_time}')


def bad(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Ибать вас некому!')


def test(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{update.message.text}')