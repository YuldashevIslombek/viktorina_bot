# import os
# import random
#
# from aiogram import Router, F
# from aiogram.filters import CommandStart, StateFilter
# from aiogram.fsm.context import FSMContext
# from aiogram.types import Message, FSInputFile
#
# from states import LevelStates
# from keyboards import levels_btn
#
# router = Router()
#
# @router.message(CommandStart())
# async def start_command(message: Message):
#
#     image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "math_img.jpg"))
#     from_user = message.from_user
#     first_name = from_user.first_name
#     last_name = from_user.last_name
#     full_name = f"{first_name} {last_name if last_name else ''}"
#     await message.answer(f"Salom {full_name}")
#     await message.answer_photo(photo=image, caption=f"Xush kelibsiz {full_name}bilag'on, "
#                                                     f"sizga bir nechta savollar berib "
#                                                     f"bilimingizni tekshirib beramiz!", reply_markup=levels_btn)
#
#
# @router.message(F.text == "Level 1️⃣")
# async def level_1(message: Message, state: FSMContext):
#     question = f"{random.randint(1, 11)} {random.choice(['+', '-', '*'])} {random.randint(1, 11)}"
#     answer = eval(question)
#     await state.update_data(answer=answer, question=question, level="Leval 1️⃣",
#                             correct=0, incorrect=0)
#     await message.answer(text=f"SAVOL: {question} = ?")
#     await state.set_state(LevelStates.javob)
#
#
# @router.message(F.text == "Level 2️⃣")
# async def level_1(message: Message, state: FSMContext):
#     question = f"{random.randint(100, 1000)} {random.choice(['+', '-', '*'])} {random.randint(100, 1000)}"
#     answer = eval(question)
#     await state.update_data(answer=answer, question=question, level="Leval 1️⃣",
#                             correct=0, incorrect=0)
#     await message.answer(text=f"SAVOL: {question} = ?")
#     await state.set_state(LevelStates.javob)
#
# @router.message(F.text == "Level 3️⃣")
# async def level_1(message: Message, state: FSMContext):
#     question = f"{random.randint(1000, 10000)} {random.choice(['+', '-', '*'])} {random.randint(1000, 10000)}"
#     answer = eval(question)
#     await state.update_data(answer=answer, question=question, level="Leval 1️⃣",
#                             correct=0, incorrect=0)
#     await message.answer(text=f"SAVOL: {question} = ?")
#     await state.set_state(LevelStates.javob)
#
# @router.message(F.text == "Level 4️⃣")
# async def level_1(message: Message, state: FSMContext):
#     question = f"{random.randint(10000, 100000)} {random.choice(['+', '-', '*'])} {random.randint(10000, 10000)}"
#     answer = eval(question)
#     await state.update_data(answer=answer, question=question, level="Leval 1️⃣",
#                             correct=0, incorrect=0)
#     await message.answer(text=f"SAVOL: {question} = ?")
#     await state.set_state(LevelStates.javob)
#
# @router.message(StateFilter(LevelStates.javob))
# async def process_answer(message: Message, state: FSMContext):
#     data = await state.get_data()
#     print(data)
#     correct_answer = data.get("answer")
#     print(correct_answer)
#     if correct_answer == int(message.text):
#         await message.answer("To'g'ri!")
#     else:
#         await message.answer(f"No To'g'ri! ")





import os
import random

from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, MessageAutoDeleteTimerChanged

from states import LevelState
from keyboards import levels_btn, stop_btn

router = Router()

def get_min_max_number(level):
    # funksiyani qolgan lever uchun xam moslash kerak
    if level == "Level 1️⃣":
        return 1, 11
    elif level == "Level 2️⃣":
        return 10, 101

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
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(1, 11)} {random.choice(['+', '-', '*'])}"
                f" {random.randint(1, 11)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="Level 1️⃣",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_btn)
    await state.set_state(LevelState.javob)

@router.message(F.text == "Level 2️⃣")
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(11, 101)} {random.choice(['+', '-', '*'])}"
                f" {random.randint(11, 101)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="Level 2️⃣",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_btn)
    await state.set_state(LevelState.javob)


@router.message(F.text == "Level 3️⃣")
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(101, 1001)} {random.choice(['+', '-', '*'])}"
                f" {random.randint(101, 1001)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="Level 3️⃣",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_btn)
    await state.set_state(LevelState.javob)


@router.message(F.text == "Level 4️⃣")
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(1001, 2001)} {random.choice(['+', '-', '*'])}"
                f" {random.randint(1001, 2001)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="Level 4️⃣",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_btn)
    await state.set_state(LevelState.javob)









@router.message(StateFilter(LevelState.javob))
async def process_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    correct_answer = data.get("answer")
    correct = data.get("correct", 0)
    incorrect = data.get("incorrect", 0)
    level = data.get("level")
    if message.text == "STOP":
        # Stop button bosilganda slayga o'xshash xabar qaytsin
        pass
    try:
        user_answer = int(message.text)
        if user_answer == correct_answer:
            correct += 1
            await message.answer("Javob to'g'ri!")
        else:
            incorrect += 1
            await message.answer("Javob noto'g'ri!")
    except ValueError:
        await message.answer("LEVEL 1️⃣"
                             "Savollarning soni:"
                             "✅️ To'g'ri javob:"
                             "❌️ Noto'g'ri javoblar:")

    min_number, max_number = get_min_max_number(level)
    question = (f"{random.randint(min_number, max_number)}"
                f"{random.choice(['+', '-', '*'])}"
                f"{random.randint(min_number, max_number)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, correct=correct, incorrect=incorrect)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_btn)
