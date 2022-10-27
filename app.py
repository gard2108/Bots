from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = r"5679091627:AAFsmPDghvzjsDsay64GO-HIPIdE8vRtox0"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(text=['Привет', 'Начать'])
@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Привет!'
                              f'\nМое почтение!')

@dp.message_handler(commands='add')
async def choice(message: types.Message):
    await message.answer(text=f'Доступны следующие овощи:'
                              f'\nпомидор'
                              f'\nредис'
                              f'\nогурец')

@dp.message_handler(text=['редис'])
async def answer_redis(message: types.Message):
    await message.answer(text=f'cам такой и он горький')

@dp.message_handler(text='помидор')
async def answer_pomidorka(message: types.Message):
    await message.answer(text=f'люблю их')

@dp.message_handler(text='огурец')
async def answer_pomidorka(message: types.Message):
    await message.answer(text=f'можно салат сделать с помидоркой')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
