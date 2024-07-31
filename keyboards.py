from telebot import types

def get_main_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text="Краткий пересказ", callback_data='brief_retelling')
    button2 = types.InlineKeyboardButton(text="Улучшенный текст", callback_data='improved_text')
    button3 = types.InlineKeyboardButton(text="Абзацы с таймкодами", callback_data='timecodes')
    button4 = types.InlineKeyboardButton(text="Что ответить", callback_data='to_answer')
    button5 = types.InlineKeyboardButton(text="Неверный язык?", callback_data='lang')
    button6 = types.InlineKeyboardButton(text="Добавить бота в группу", url="https://t.me/VoiceMessage_AI_Bot?startgroup=pm")
    keyboard.add(button1, button2, button3, button4, button5, button6)
    return keyboard
