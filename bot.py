import telebot
from config import TOKEN
from telebot import types
import requests
import json

def tg_bot(TOKEN):
    bot = telebot.TeleBot(TOKEN)
    
    # вызов стартавой команды, прикрепление кнопок по вызову 4 криптовалют
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
    
    # ответ на запрос после нажатия одной из кнопки или ввода текста 
    @bot.message_handler(content_types=['text'])
    def send_message2(message):
        if message.text == 'BTCUSDT':
            response = requests.get(url="https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT").text
            # формирование словаря
            dic = json.loads(response.replace("'", '"'))
            # вывод значения из сформированного словаря по ключу 'lastPrice' по BTCUSDT
            price = float(dic.get('lastPrice'))
            # вывод значения из сформированного словаря по ключу 'bidPrice' по BTCUSDT
            bid_price = float(dic.get('bidPrice')) 
            # вывод значения из сформированного словаря по ключу 'askPrice' по BTCUSDT
            ask_price = float(dic.get('askPrice'))           
            bot.send_message(message.from_user.id, 'Последняя цена: '+ str(price)\
                 + '\nЦена предложения покупателя (bid price): ' + str(bid_price)\
                 + '\nЦена предложения продавца (ask price): ' + str(ask_price))
        # при запросе другой криптомонеты
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
        # при запросе на несуществующей команды выведем ошибку
        else:
            bot.send_message(message.from_user.id, 'Выберите только эту криптовалюту из списка:\
                \nBTCUSDT \nLTCUSDT \nETHUSDT \nDOGEUSDT')
    bot.polling()

def main():
    tg_bot(TOKEN)

if __name__ == "__main__":
    main()
