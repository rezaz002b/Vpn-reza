from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import json
import os

TOKEN = "8104196841:AAHucmMu12DUXlvszym_RwKjuUpN3Loq91w"
ADMIN_ID = "6624180200"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# خواندن لیست محصولات از فایل
def load_products():
    with open("products.json", "r", encoding="utf-8") as file:
        return json.load(file)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    products = load_products()
    response = "📌 لیست محصولات:\n\n"
    for product in products:
        response += f"🔹 {product['name']} | {product['price']} تومان\nموجودی: {product['stock']} عدد\n\n"
    await message.reply(response + "برای خرید، مقدار مورد نظر را ارسال کنید.")

@dp.message_handler()
async def handle_buy(message: types.Message):
    products = load_products()
    for product in products:
        if message.text in product["name"]:
            await message.reply(f"✅ لطفاً مبلغ {product['price']} تومان را به شماره کارت زیر واریز کنید و رسید را ارسال کنید:\n\n💳 ۶۲۱۹۸۶۱۰۲۳۴۵۶۷۸۹\n\nپس از ارسال رسید، منتظر تأیید باشید.")
            return

    await message.reply("❌ محصول مورد نظر یافت نشد!")

executor.start_polling(dp)
