from aiogram import types
from parser.parser import main
from tg_bot.loader import dp, bot
from aiogram.filters import Command
from aiogram.types import BotCommand, CallbackQuery

@dp.message(Command(commands='start'))
async def process_start_command(message: types.Message):
    await message.answer('Чтобы получить рассписание матчей нажмите: < /match_schedule >')


@dp.message(Command(commands='match_schedule'))
async  def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, main())

if __name__ == '__main__':
    dp.run_polling(bot)