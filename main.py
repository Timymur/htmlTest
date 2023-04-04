
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
bot = Bot('6110202136:AAH8LtiBjBdtcl8HVIUSsibshjiOf03dj8I')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Открыть страницу", web_app=WebAppInfo(url='https://google.com')))
    await message.answer("Hello, my friend", reply_markup=markup)


executor.start_polling(dp)