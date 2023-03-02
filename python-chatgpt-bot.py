#Author: Arman Idrisi

import telebot
import openai


#Bot Api Token
API_TOKEN = '5887169615:AAE3iwbisaMrp8uhQpEpgP4JhcQD5O1E0ac'
#Openai Api Key
openai.api_key="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"


bot = telebot.TeleBot(API_TOKEN)

#Generate The Response
def get_response(msg):
	completion = openai.Completion.create(
    engine="text-davinci-003",
    prompt=msg,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
	return completion.choices[0].text

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	 # bot.send_message(message.chat.id,message.text)
	   bot.send_message(message.chat.id, """\
Hi there, I am A Ai ChatBot.

I am here to Give Answers Of Your Question.

I Am Created Using Chatgpt Api ! 

Use /ask  To Ask Questions\
""")

#Handle The '/ask'
@bot.message_handler(commands=['ask'])
def send_answer(message):
	question=message.text[len("/ask"):]
	if len(question)==0:
		bot.send_message(message.chat.id,"Send Like This /ask Your Question") 
	else:
		bot.send_message(message.chat.id,get_response(question))


#run the Bot
bot.infinity_polling()
