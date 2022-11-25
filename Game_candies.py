from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from random import randint

# Функция вывода этапов игры


async def game_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/start')

# Функция жеребьёвки


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Давай сыграем!\nУсловия игры:\nНа столе лежит 2021 конфета.\nДелаем ходы по очереди.\nПервый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты достаются сделавшему последний ход.')
    await update.message.reply_text(f'Проводим жеребьёвку. Кидаем кубик:')
    A = randint(1, 6)
    B = randint(1, 6)
    await update.message.reply_text(f'Опа!\nТебе выпало {A}\nМне выпало {B}')
    if A == B:
        await update.message.reply_text(f'У нас одинаковые числа!\nПовоторяем жеребьёвку\nНабери снова /draw')
    else:
        if A > B:
            await update.message.reply_text('У тебя больше\nПервый ход за тобой')
            await update.message.reply_text(f'Начинаем игру.\nНабери /s и количество конфет')
        elif A < B:
            await update.message.reply_text('У меня больше\nПервый ход за мной')
            await update.message.reply_text(f'Начинаем игру.')
            y = randint(1, 28)
            await update.message.reply_text(f'Я беру {y} конфет')
            b = number_candies[len(number_candies) - 1]
            b -= y
            number_candies.append(b)
            await update.message.reply_text(f'На столе осталось {b} конфет\nТвой ход\nНабери /s и количество конфет')

number_candies = [2021]

# Функция игры


async def game_candies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    b = number_candies[len(number_candies) - 1]
    msg = update.message.text
    items = msg.split()
    a = int(items[1])
    b -= a
    await update.message.reply_text(f'Ты взял {a} конфет.\nНа столе осталось {b} конфет')
    number_candies.append(b)
    print(number_candies)
    if b == 0:
        await update.message.reply_text(f'Конфеты кончились!\nМолодец! Ты выйграл!\n')
        await update.message.reply_text(f'Для новой игры перезапустите скрипт в VSCode')
    else:
        if b > 28:
            y = randint(1, 28)
            await update.message.reply_text(f'Я беру {y} конфет')
            b -= y
            await update.message.reply_text(f'На столе осталось {b} конфет\nТвой ход\nНабери /s и количество конфет')
        else:
            await update.message.reply_text(f'Я беру {b} конфет.\nКонфеты кончились!\nБот выйграл!')
            await update.message.reply_text(f'Для новой игры перезапустите скрипт в VSCode')

    number_candies.append(b)