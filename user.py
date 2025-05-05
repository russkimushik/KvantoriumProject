import config as cfg
from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
import app.keyboard as kb
from app.database.requests import set_user

user = Router()

@user.message(CommandStart)
async def start(message: Message):
    await set_user(message.from_user.id, message.from_user.username)
    await message.answer('Добро пожаловать. Это бот для Кванториума 36', reply_markup=kb.start)

@user.callback_query(F.data == 'directions')
async def directions(callback: CallbackQuery):
    await callback.message.answer('У нас существуют множество различных напрвалений.', reply_markup=await kb.show_direction())
