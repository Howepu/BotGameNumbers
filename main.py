import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Инициализация бота и диспетчера
TOKEN = '5700582521:AAGEfvd7KAIYzteTDFR1Cn6QuHpIMxPZhyg'
bot = Bot(TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я загадал число от 1 до 10. Угадай его!")

# Глобальные переменные для игры
number = random.randint(1, 10)
attempts = 0
max_attempts = 5

# Обработчик сообщений с числом
@dp.message_handler(lambda message: message.text.isdigit())
async def process_number(message: types.Message):
    global attempts, number
    # Проверка, что игра идет
    if attempts >= max_attempts:
        await message.reply(f"Игра окончена! Я загадал число {number}\n\nЧтобы начать игру введите /start")
        return

    # Попытка угадать число
    guess = int(message.text)
    attempts += 1

    if guess > number:
        text = "Мое число меньше"
    elif guess < number:
        text = "Мое число больше"
    else:
        text = f"Ты угадал число {number} с {attempts} попыток!\n\n\n" \
               f"Я загадал новое число от 1 до 10. Угадай его!"
        attempts = 0
        number = random.randint(1, 10)
    await message.reply(text)

# Обработчик всех остальных сообщений
@dp.message_handler()
async def process_other_messages(message: types.Message):
    await message.reply("Я не понимаю, о чем вы...")

if __name__ == '__main__':
    executor.start_polling(dp)
