import telebot
import requests
from telebot import types

# استخدم التوكن مباشرةً هنا
took = '7715679622:AAEyA6WvSSI5zKQOTF4j-tkr2UDoroCHbTg'
bot = telebot.TeleBot(took)

@bot.message_handler(commands=['start'])
def sd(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("يـوسـف الثـقفي", url="https://t.me/bsx_h2")
    markup.add(btn)
    
    sd.sd = message.from_user.first_name
    bot.send_message(
        message.chat.id, 
        f"أهلاً بكَ في بوت يـوسـف الثـقفي ❤️\n\n"
        f"✨ صَلِّ عَلَى رَسُولِ اللهِ، يَفْلَحُ وَجْهُكَ في دُنْيَاكَ قَبْلَ أُخْرَاكَ، وَيُكْفِي هَمَّكَ ويُغْفَرُ ذَنْبُكَ ✨\n\n"
        f"اسْأَلْ عن أيِّ شَيْءٍ يَخْطُرُ ببالِكَ، وسَأكونُ هُنَا للإجابةِ عَلَيْكَ بِإذْنِ اللّٰه 🌟\n\n"
        f"نُسخة مُصَغَّرَة من ChatGPT، مِن صُنعي ♥️\n\n"
        f"اضغَطْ عَلَى الزِّرِّ أَدْنَاهُ لِلْتَّوَاصُلِ مَعِي 👇🏻", 
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    saad = message.text

    headers = {
        'authority': 'api.binjie.fun',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://chat18.aichatos8.com',
        'referer': 'https://chat18.aichatos8.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'prompt': saad,
        'network': True,
        'system': '',
        'withoutContext': False,
        'stream': False,
    }

    try:
        ree = requests.post('https://api.binjie.fun/api/generateStream', headers=headers, json=json_data)
        ree.encoding = 'utf-8'
        bot.send_message(message.chat.id, ree.text)
    except Exception as e:
        bot.send_message(message.chat.id, f"حدث خطأ: {e}")

bot.infinity_polling()