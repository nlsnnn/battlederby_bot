from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON

other_router = Router()


@other_router.message()
async def other_msg(message: Message):
    await message.answer(LEXICON['other'])