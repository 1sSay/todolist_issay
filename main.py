import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''
ISSAY_ID = -1

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hi\nIt's to do list for IsSay")


@dp.message_handler(commands=['add'])
async def add_note(message: types.Message):
    