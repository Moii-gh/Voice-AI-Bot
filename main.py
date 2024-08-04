from telebot import TeleBot, types
import re
from keyboards import get_main_keyboard
from gpt import GPT
from audio_utils import download_file, convert_to_pcm16, progress_audio_file
from config import Tg_Key, max_message_size, max_message_duration

bot = TeleBot(Tg_Key)
user_texts = {}
gpt = GPT()

start_text = """
🗣️Возможности:
– Очень быстрое и точное распознавание голоса📊 и краткий пересказ✍️
– Мы не храним ваши данные 🔒 
– Поддержка групповых чатов и Телеграм-каналов 💬
- и многое другое🧩\n\nЖдем вашего голосового сообщения"""

@bot.message_handler(["start"])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"{start_text}\n\n")


@bot.message_handler(content_types=["voice"])
def echo_voice(message):
    data = message.voice
    if(data.file_size > max_message_size) or (data.duration > max_message_duration):
        reply = "Сообщение слишком большое"
        bot.reply_to(message, reply)
        return
    file_url = f"https://api.telegram.org/file/bot{bot.token}/{bot.get_file(data.file_id).file_path}"
    file_path = download_file(file_url)
    convert_to_pcm16(file_path)
    text = progress_audio_file("new.wav")
    
    if text:
        reply_text = f"{text}\n\nСоздано ботом <a href='https://t.me/VoiceMessage_AI_Bot'>Voice Message - AI</a>"
        user_texts[message.chat.id] = text
    else:
        reply_text = "Не удалось распознать текст."
    bot.reply_to(message, reply_text, reply_markup=get_main_keyboard(), parse_mode='HTML')


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    text = user_texts.get(chat_id, "")
    options = {
        'model': 'gpt-4',
        'markdown': False,
    }

    if text:
        if call.data == "brief_retelling":
            bot.answer_callback_query(call.id, "Идет пересказ...")
            messages = [
                {
                    'role': 'user',
                    'content': "Максимально сократи данный текст: " + text
                }
            ]
            response = gpt.fetch_data(messages, options)
            bot.send_message(chat_id, response)

        elif call.data == "improved_text":
            messages = [
                {
                    'role': 'user',
                    'content': "Улучши данный текст: " + text
                }
            ]
            response = gpt.fetch_data(messages, options)
            bot.send_message(chat_id, response)
        elif call.data == "timecodes":
            bot.answer_callback_query(call.id, "Данная функция пока не работает")

        elif call.data == "to_answer":
             messages = [
                {
                    'role': 'user',
                    'content': "Ответь на данный текст 3 разными ответами : " + text
                }
            ]
             response = gpt.fetch_data(messages, options)
             bot.send_message(chat_id, response)
        elif call.data == "lang":
            bot.send_message(chat_id, "Пока я говорю только известных мне языках, но если вам нужно, я постараюсь использовать все свои способности, чтобы понять и говорить на вашем языке <b>попозже</b>.", parse_mode="HTML")
    
    else:
        bot.send_message(chat_id, "Текст для пересказа не найден.")

if __name__ == "__main__":
    bot.delete_webhook()
    bot.polling()
