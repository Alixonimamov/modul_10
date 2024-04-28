from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

location_delev = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='share_location', request_location=True)],

], resize_keyboard=True)

contact = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='поделиться контактом', request_contact=True),
     KeyboardButton(text='поделиться местоположением', request_location=True)],

], resize_keyboard=True)

# Inlinekeyboard
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Контакт', callback_data='Контакт'),
     InlineKeyboardButton(text="расположение", callback_data="расположение")],
    [InlineKeyboardButton(text="оплатить", callback_data="оплатить"), InlineKeyboardButton(text="Меню", callback_data="Меню")],
    [InlineKeyboardButton(text="о нас", callback_data="о нас")],
    [InlineKeyboardButton(text="помощь", callback_data="помощь")],
    [InlineKeyboardButton(text="Доставка", callback_data="Доставка")]
])
