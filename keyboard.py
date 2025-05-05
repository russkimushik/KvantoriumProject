from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from app.database.requests import get_directions


start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Напрвления', callback_data='directions')]
])

async def show_direction():
    all_direction = await get_directions()
    keyboard = InlineKeyboardBuilder()

    for direction in all_direction:
        keyboard.add(InlineKeyboardButton(text = direction.title, callback_data=f'direction_{direction.id}'))

    return keyboard.adjust(2).as_markup()