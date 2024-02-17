from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.filters import CommandStart
from keyboards.inline_kb import get_markup, get_markup_url
from lexicon.lexicon import LEXICON, MEDIA

user_router = Router()


@user_router.message(CommandStart())
async def start_cmd(message: Message):
    markup = get_markup(3, 'faq_btn', 'sneak_peeks_btn', 'links_btn', 'how_wl_btn')
    await message.answer_photo(
        photo=MEDIA['photo1'],
        caption=LEXICON['/start'],
        reply_markup=markup
    )


@user_router.callback_query(F.data == 'faq_btn')
async def faq_msg(callback: CallbackQuery):
    markup = get_markup(1, 'backward')
    await callback.message.edit_media(
        reply_markup=markup,
        media=(InputMediaPhoto(
            media=MEDIA['photo2'],
            caption=LEXICON['faq']
        ))
    )


@user_router.callback_query(F.data == 'how_wl_btn')
async def how_wl_msg(callback: CallbackQuery):
    markup = get_markup(1, 'backward')
    await callback.message.edit_media(
        reply_markup=markup,
        media=InputMediaPhoto(
            media=MEDIA['photo3'],
            caption=LEXICON['how_wl']
        )
    )


@user_router.callback_query(F.data == 'links_btn')
async def links_msg(callback: CallbackQuery):
    markup = get_markup_url(2, 'Twitter', 'Discord', 'Website')
    await callback.message.edit_media(
        reply_markup=markup,
        media=InputMediaPhoto(
            media=MEDIA['photo3'],
            caption=LEXICON['links']
        )
    )


@user_router.callback_query(F.data == 'backward')
async def backward(callback: CallbackQuery):
    markup = get_markup(3, 'faq_btn', 'sneak_peeks_btn', 'links_btn', 'how_wl_btn')
    await callback.message.edit_media(
        reply_markup=markup,
        media=InputMediaPhoto(
            media=MEDIA['photo1'],
            caption=LEXICON['/start']
        )
    )
