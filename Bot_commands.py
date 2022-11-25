from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import datetime
from pytube import YouTube
import requests
from telegram import Bot


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет! {update.effective_user.first_name}!\nЯ ТелеБот!\nДля просмотра списка команд введи /help')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Текущее время: {datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Мои функции:\n/hi\n/time\n/help\n/calc\n/edit\n/game\n/youtube\n/valute')

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/sum\n/sub\n/mult\n/div\n/exp')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x - y}')

async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x * y}')

async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} / {y} = {x / y}')

async def exp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} ** {y} = {x ** y}')

async def edit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    a = " ".join(list(filter(lambda x: 'абв' not in x, msg.split())))
    await update.message.reply_text(f'{a}')

async def youtube_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.split()[1]
    yt = YouTube(url)
    yt.streams.filter(res="360p").first().download(filename=f"{12345}.mp4")
    await update.message.reply_text(f'{yt.title}')
    chat_id = update.message.chat_id
    bot = Bot("Your_Token")
    await bot.send_video(chat_id = chat_id, video=open(f"{12345}.mp4", 'rb'))

async def valute_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Выбери валюту:\n/GBP\n/BYN\n/USD\n/EUR\n/CNY\n/JPY')
    await update.message.reply_text(f'Введи /type и код валюты')


async def well_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    currency_type = update.message.text.split()[1]
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    nominal = data['Valute'][currency_type]['Nominal']
    name = data['Valute'][currency_type]['Name']
    value = data['Valute'][currency_type]['Value']
    await update.message.reply_text(f'{nominal} {name} => {value} руб.')