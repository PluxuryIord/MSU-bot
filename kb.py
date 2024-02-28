import asyncio
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
import texts

info_button = types.InlineKeyboardButton(
    text="Информация",
    callback_data="info"
)

choose_button = types.InlineKeyboardButton(
    text="Выбрать свою категорию",
    callback_data="choose_category"
)

button1 = types.InlineKeyboardButton(
    text="1",
    callback_data="category1"
)

button2 = types.InlineKeyboardButton(
    text="2",
    callback_data="category2"
)

button3 = types.InlineKeyboardButton(
    text="3",
    callback_data="category3"
)

button4 = types.InlineKeyboardButton(
    text='4',
    callback_data="category4"
)
button5 = types.InlineKeyboardButton(
    text='5',
    callback_data="category5"
)
button6 = types.InlineKeyboardButton(
    text='6',
    callback_data="category6"
)
button7 = types.InlineKeyboardButton(
    text='7',
    callback_data="category7"
)
button8 = types.InlineKeyboardButton(
    text='8',
    callback_data="category8"
)
button9 = types.InlineKeyboardButton(
    text='9',
    callback_data="category9"
)
button10 = types.InlineKeyboardButton(
    text='10',
    callback_data="category10"
)
button11 = types.InlineKeyboardButton(
    text='11',
    callback_data="category11"
)
button12 = types.InlineKeyboardButton(
    text='12',
    callback_data="category12"
)
