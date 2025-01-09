from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Uy ko'chirish hizmati"),
            KeyboardButton(text="3 Tonna gacha"),
            KeyboardButton(text="3 Tonna +")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
