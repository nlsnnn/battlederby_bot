from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON, LINKS


def get_markup(width, *args, **kwargs):
    kb_builder = InlineKeyboardBuilder()
    buttons = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button
            ))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button
            ))

    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()


def get_markup_url(*args):
    kb_buidler = InlineKeyboardBuilder()
    buttons = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=button,
                url=LINKS[button]
            ))

    kb_buidler.row(*buttons)
    return kb_buidler.as_markup()