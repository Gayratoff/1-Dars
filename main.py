from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import CommandStart,CommandHelp
from aiogram.utils import executor

from config import TOKEN

bot=Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(CommandStart())
async def MistrUz(message: types.Message):
    await message.reply("Salom Test Botimizga XuSh Kelibisiz")

@dp.message_handler(CommandHelp())
async def Help(message: types.Message):
    await message.answer("Bu /Help buyrugi")


if __name__ =="__main__":
    executor.start_polling(dp)