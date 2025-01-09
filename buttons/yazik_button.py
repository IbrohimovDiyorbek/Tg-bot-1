from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

name_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Услуги по переезду дома"),
            KeyboardButton(text="До 3 тонн"),
            KeyboardButton(text="3 Tonna +")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)