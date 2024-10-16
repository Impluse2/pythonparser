from aiogram import Bot, Dispatcher
import logging

TG_TOKEN = ('8046045883:AAG17Ohsln323bbOk0B_MRxuYlqnVRU-InM')
bot = Bot(token=TG_TOKEN)
dp = Dispatcher()

def on_startup():
    print('Бот запущен')


