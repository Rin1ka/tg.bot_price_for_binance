import telebot
from config import TOKEN
from telebot import types
import requests
import json

def tg_bot(TOKEN):
    bot = telebot.TeleBot(TOKEN)
    
    @bot.message_handler(commands=['start'])
    def start_message(message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('BTCUSDT')
        itembtn2 = types.KeyboardButton('LTCUSDT')
        itembtn3 = types.KeyboardButton('ETHUSDT')
        itembtn4 = types.KeyboardButton('DOGEUSDT')

        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
        
        bot.send_message(message.chat.id, "Привет! \nБот выводит информацию по криптовалютам.\
                \nВыбери криптовалюту", reply_markup=markup)

    # bot.infinity_polling() # Метод infinity_polling нужен только для обхода падения бота путем его перезапуска
    
    @bot.message_handler(content_types=['text', 'document', 'audio'])
    def send_message2(message):
        if message.text == 'BTCUSDT':
            response = requests.get(url="https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT").text
            dic = json.loads(response.replace("'", '"'))
            price = float(dic.get('lastPrice'))
            bid_price = float(dic.get('bidPrice')) 
            ask_price = float(dic.get('askPrice'))           
            bot.send_message(message.from_user.id, 'Последняя цена: '+ str(price)\
                 + '\nЦена предложения покупателя (bid price): ' + str(bid_price)\
                 + '\nЦена предложения продавца (ask price): ' + str(ask_price))
        elif message.text == 'LTCUSDT':
            response = requests.get(url="https://api.binance.com/api/v3/ticker/24hr?symbol=LTCUSDT").text
            dic = json.loads(response.replace("'", '"'))
            price = float(dic.get('lastPrice'))
            bid_price = float(dic.get('bidPrice')) 
            ask_price = float(dic.get('askPrice'))           
            bot.send_message(message.from_user.id, 'Последняя цена: '+ str(price)\
                 + '\nЦена предложения покупателя (bid price): ' + str(bid_price)\
                 + '\nЦена предложения продавца (ask price): ' + str(ask_price))
        elif message.text == 'ETHUSDT':
            response = requests.get(url="https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT").text
            dic = json.loads(response.replace("'", '"'))
            price = float(dic.get('lastPrice'))
            bid_price = float(dic.get('bidPrice')) 
            ask_price = float(dic.get('askPrice'))           
            bot.send_message(message.from_user.id, 'Последняя цена: '+ str(price)\
                 + '\nЦена предложения покупателя (bid price): ' + str(bid_price)\
                 + '\nЦена предложения продавца (ask price): ' + str(ask_price))
        elif message.text == 'DOGEUSDT':
            response = requests.get(url="https://api.binance.com/api/v3/ticker/24hr?symbol=DOGEUSDT").text
            dic = json.loads(response.replace("'", '"'))
            price = float(dic.get('lastPrice'))
            bid_price = float(dic.get('bidPrice')) 
            ask_price = float(dic.get('askPrice'))           
            bot.send_message(message.from_user.id, 'Последняя цена: '+ str(price)\
                 + '\nЦена предложения покупателя (bid price): ' + str(bid_price)\
                 + '\nЦена предложения продавца (ask price): ' + str(ask_price))
        else:
            bot.send_message(message.from_user.id, 'Выберите только эту криптовалюту из списка:\
                \nBTCUSDT \nLTCUSDT \nETHUSDT \nDOGEUSDT')
    bot.polling()


if __name__ == "__main__":
    tg_bot(TOKEN)
