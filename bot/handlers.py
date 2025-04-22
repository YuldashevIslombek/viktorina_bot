import os
import random

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from keyboards import levels_btn

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):

    image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "math_img.jpg"))
    from_user = message.from_user
    first_name = from_user.first_name
    last_name = from_user.last_name
    full_name = f"{first_name} {last_name if last_name else ''}"
    await message.answer(f"Salom {full_name}")
    await message.answer_photo(photo=image, caption=f"Xush kelibsiz {full_name}bilag'on, "
                                                    f"sizga bir nechta savollar berib "
                                                    f"bilimingizni tekshirib beramiz!", reply_markup=levels_btn)


@router.message(F.text == "Level 1️⃣")
async def level_1(message: Message):
    question = f"{random.randint(1, 11)} {random.choice(['+', '-', '*'])} {random.randint(1, 11)}"
    await message.answer(text=f"SAVOL: {question} = ?")

@router.message(F.text == "Level 2️⃣")
async def level_1(message: Message):
    question = f"{random.randint(100, 1000)} {random.choice(['+', '-', '*'])} {random.randint(10, 100)}"
    await message.answer(text=f"SAVOL: {question} = ?")

@router.message(F.text == "Level 3️⃣")
async def level_1(message: Message):
    question = f"{random.randint(1000, 10000)} {random.choice(['+', '-', '*'])} {random.randint(100, 1000)}"
    await message.answer(text=f"SAVOL: {question} = ?")

@router.message(F.text == "Level 4️⃣")
async def level_1(message: Message):
    question = f"{random.randint(1000, 10000)} {random.choice(['+', '-', '*'])} {random.randint(1000, 10000)}"
    await message.answer(text=f"SAVOL: {question} = ?")