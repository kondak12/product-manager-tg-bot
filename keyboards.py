from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram import types


def default_keyboard_builder(buttons_list: list, keyboard_size: int):
    builder = ReplyKeyboardBuilder()

    for button in buttons_list:
        builder.add(types.KeyboardButton(text=str(button)))

    builder.adjust(keyboard_size)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

async def date_inline_keyboard_builder():
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(text="День", callback_data="day_label"),
        types.InlineKeyboardButton(text="Месяц", callback_data="month_label"),
        types.InlineKeyboardButton(text="Год", callback_data="year_label"),
        types.InlineKeyboardButton(text="Минута", callback_data="minute_label"),
        types.InlineKeyboardButton(text="Час", callback_data="hour_label")
    )

    builder.row(
        types.InlineKeyboardButton(text="+1", callback_data="day_decr"),
        types.InlineKeyboardButton(text="+1", callback_data="month_decr"),
        types.InlineKeyboardButton(text="+1", callback_data="year_decr"),
        types.InlineKeyboardButton(text="+1", callback_data="minute_decr"),
        types.InlineKeyboardButton(text="+1", callback_data="hour_decr")
    )

    builder.row(
        types.InlineKeyboardButton(text="-1", callback_data="day_incr"),
        types.InlineKeyboardButton(text="-1", callback_data="month_incr"),
        types.InlineKeyboardButton(text="-1", callback_data="year_incr"),
        types.InlineKeyboardButton(text="-1", callback_data="minute_incr"),
        types.InlineKeyboardButton(text="-1", callback_data="hour_incr")
    )

    builder.row(types.InlineKeyboardButton(text="Подтвердить", callback_data="date_finish"))

    return builder.as_markup()