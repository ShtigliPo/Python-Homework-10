from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from Bot_commands import *
from Game_candies import *

app = ApplicationBuilder().token(
    "Your_Token").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("exp", exp_command))
app.add_handler(CommandHandler("edit", edit_command))
app.add_handler(CommandHandler("game", game_command))
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("s", game_candies))
app.add_handler(CommandHandler("youtube", youtube_command))
app.add_handler(CommandHandler("valute", valute_command))
app.add_handler(CommandHandler("type", well_command))

print('starting....')
app.run_polling()