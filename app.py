import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

import kb
import texts

TOKEN = "TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    photo = FSInputFile("hello_picture.jpg")
    builder = InlineKeyboardBuilder()
    builder.row(kb.info_button, kb.choose_button, width=1)
    await message.answer_photo(photo=photo, caption=texts.hello_text, reply_markup=builder.as_markup())


@dp.callback_query(F.data == "choose_category")
async def choose_category(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(kb.button1, kb.button2, kb.button3, kb.button4, kb.button5, kb.button6, kb.button7, kb.button8,
                kb.button9, kb.button10, kb.button11, kb.button12, width=3)
    await callback.message.answer(texts.choose_text, reply_markup=builder.as_markup())
    await callback.answer()


@dp.message(Command('info'))
async def echo(message: types.Message):
    await message.answer(texts.info_text)


@dp.callback_query(F.data == "info")
async def choose_category(callback: types.CallbackQuery):
    await callback.message.answer(texts.info_text)
    await callback.answer()


@dp.callback_query(F.data == "category1")
async def call_back_accept(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.category1_text)
    await callback.answer()


@dp.callback_query(F.data == "category2")
async def call_back_accept(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.category2_text)
    await callback.answer()


@dp.callback_query(F.data == "category3")
async def call_back_accept(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.category3_text)
    await callback.answer()


@dp.callback_query(F.data == "category4")
async def call_back_accept(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.category4_text)
    await callback.answer()


@dp.callback_query(F.data == "category5")
async def call_back_accept(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.category5_text)
    await callback.answer()


@dp.callback_query(F.data == "category6")
async def call_back_accept(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.category6_text)
    await callback.answer()


@dp.callback_query(F.data == "category7")
async def call_back_accept(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.category7_text)
    await callback.answer()


@dp.callback_query(F.data == "category8")
async def call_back_accept(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.category8_text)
    await callback.answer()


@dp.callback_query(F.data == "category9")
async def call_back_accept(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.category9_text)
    await callback.answer()


@dp.callback_query(F.data == "category10")
async def call_back_accept(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.category10_text)
    await callback.answer()


@dp.callback_query(F.data == "category11")
async def call_back_accept(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.category11_text)
    await callback.answer()


@dp.callback_query(F.data == "category12")
async def call_back_accept(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.category12_text)
    await callback.answer()


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
