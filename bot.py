import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import config
import database

bot = Bot(config.TOKEN)
dp = Dispatcher()


def main_keyboard():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎰 Казино",
                    web_app=WebAppInfo(url=https://mywebaddppbrotby.vercel.app)
                )
            ]
        ]
    )
    return kb


@dp.message(F.text == "/start")
async def start(msg: Message):
    user_id = msg.from_user.id
    username = msg.from_user.username
    database.add_user(user_id, username)
    await msg.answer(
        "Добро пожаловать в Ultimate Casino 🎰",
        reply_markup=main_keyboard()
    )


@dp.message(F.web_app_data)
async def webapp_handler(msg: Message):
    user_id = msg.from_user.id
    user = database.get_user(user_id)
    if not user:
        return

    if user[4] == 1:
        await msg.answer("🚫 Ты забанен")
        return

    data = msg.web_app_data.data.split(":")
    action = data[0]

    if action == "buy":
        price = int(data[1])
        if user[3] < price:
            await msg.answer("❌ Недостаточно монет")
            return
        database.remove_balance(user_id, price)

    elif action == "win":
        amount = int(data[1])
        database.add_balance(user_id, amount)
        await msg.answer(f"🎉 Ты выиграл {amount} монет!")

    elif action == "item":
        item_name = data[1]
        rarity = data[2]
        database.add_item(user_id, item_name, rarity)
        await msg.answer(f"✨ Вы получили предмет: {item_name} ({rarity})")

    elif action == "admin":
        username = msg.from_user.username
        if username == config.ADMIN_USERNAME:
            await msg.answer("🛠 Админ панель")
        else:
            await msg.answer("❌ Доступ запрещен")


async def main():
    print("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())