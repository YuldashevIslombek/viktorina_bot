# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#
# levels_btn = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Level 1️⃣"), KeyboardButton(text="Level 2️⃣")],
#         [KeyboardButton(text="Level 3️⃣"), KeyboardButton(text="Level 4️⃣")],
#     ], resize_keyboard=True
# )
#
#
# def stop_btn():
#     return None


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

levels_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Level 1️⃣"), KeyboardButton(text="Level 2️⃣")],
        [KeyboardButton(text="Level 3️⃣"), KeyboardButton(text="Level 4️⃣")],
    ], resize_keyboard=True
)

stop_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="STOP")],
    ], resize_keyboard=True
)