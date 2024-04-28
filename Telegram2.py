import os
import asyncio

from aiogram.types import FSInputFile

from keyboards import keyboard, contact, location_delev

import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN=os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#start
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Hi im Cafe&restaurant De pari", reply_markup=keyboard)


#contact

@dp.callback_query(F.data == "Контакт")
async def Contacts(callback: types.CallbackQuery):
    await callback.message.answer_contact("(+998) 909080109", "Nigora", "Vaxidova")


#location
@dp.message(Command("расположение"))
async def get_locations(message: types.Message):
    await message.answer_location(41.3239474, 69.241994)

@dp.callback_query(F.data == "расположение")
async def location(callback: types.CallbackQuery):
    await callback.message.answer_location(41.3239474, 69.241994)


#card
@dp.callback_query(F.data == "оплатить")
async def card(callback: types.CallbackQuery):
    await callback.message.answer("оплатите по этой номер карты, номер карты 2505 0144 0635 0147🗃️")


#About
@dp.callback_query(F.data == "о нас")
async def about(callback: types.CallbackQuery):
    await callback.message.answer("это кафе-ресторан был открыт в 2023 году")

@dp.message(Command("о нас"))
async def get_about(message: types.Message):
    await message.answer("это кафе-ресторан был открыт в 2023 году")


#Help
@dp.callback_query(F.data == "помощь")
async def help(callback: types.CallbackQuery):
    await callback.message.answer("Чем мы можем вам помочь? (+998) 981010202", "Doston")

@dp.message(Command("помощь"))
async def get_help(message: types.Message):
    await message.answer("Чем мы можем вам помочь? (+998) 981010202")


#Menu
@dp.callback_query(F.data == "Меню")
async def Menu(callback: types.CallbackQuery):
    await callback.message.answer_photo(photo=FSInputFile('867.png',), reply_markup=contact)

@dp.message(Command("Меню"))
async def get_Menu(message: types.Message):
    await message.answer_photo(photo=FSInputFile('867.png'), reply_markup=contact)


#delivery
@dp.callback_query(F.data == "Доставка")
async def Delivery(callback: types.CallbackQuery):
    await callback.message.answer("Поделитесь своим местоположением и поделитесь своим контактом", reply_markup=contact)








async def main():
    print("Bot started")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
