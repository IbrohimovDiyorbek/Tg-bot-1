from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

til_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="УЗБ "),
            KeyboardButton(text="РУС")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)