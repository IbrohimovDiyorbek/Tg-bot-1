from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from buttons.start_buttons import start_buttons
from buttons.til_button import til_buttons
from buttons.yazik_button import name_buttons

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("UZB/РУС", reply_markup=til_buttons)


@router.message(lambda message: message.text == "УЗБ")
async def uzb(message: Message):
    await message.answer("Yuk vaznini belgilang:", reply_markup=start_buttons)


@router.message(lambda message: message.text == "Uy ko'chirish hizmati")
async def name(message: Message):
    await message.answer("Tel: 900270350")


@router.message(lambda message: message.text == "3 Tonna gacha")
async def name(message: Message):
    await message.answer("Tel: 900270350")


@router.message(lambda message: message.text == "3 Tonna +")
async def name(message: Message):
    await message.answer("Tel: 900270350")


@router.message(lambda message: message.text == "РУС")
async def rus(message: Message):
    await message.answer("Укажите вес груза:", reply_markup=name_buttons)


@router.message(lambda message: message.text == "Услуги по переезду дома")
async def name_rus(message: Message):
    await message.answer("Tel: 900270350")


@router.message(lambda message: message.text == "До 3 тонн")
async def name_rus(message: Message):
    await message.answer("Tel: 900270350")


@router.message(lambda message: message.text == "3 Tonna +")
async def name_rus(message: Message):
    await message.answer("Tel: 900270350")
