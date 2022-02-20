import telebot
from udpy import UrbanClient
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)
client = UrbanClient()

def remove_char(line):
    '''removes square brackets surrounding words for a cleaner look'''
    line=line.replace('[','')
    line=line.replace(']','')
    return line

def get_def(term):
    '''returns definition of term'''
    defs = client.get_definition(term) # list of definitions
    return remove_char(defs[0].definition)

@bot.message_handler(commands=['start', 'help'])
def start(message):
	bot.reply_to(message, "just type the word you want to look up")

@bot.message_handler(func=lambda message: True)
def definition(message):
	bot.reply_to(message, get_def(message.text))

bot.infinity_polling()

