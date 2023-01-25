import telebot
from bot_token import TOKEN, crypto_dict
from exeption_func import test_exception
from extensions import Currency, APIException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def greeting_func(message):
    bot.send_message(message.chat.id,
                     f'Привет, {message.chat.username}!\nЧтобы начать работу введите команду боту в следующем формате:\n'
                     f'<имя валюты покупки><имя валюты продажи><количество покупаемой валюты>\n'
                     f'Для просмотра возможных валют воспользуйтесь командой: /values')


@bot.message_handler(commands=['values'])
def show_currency(message):
    text = ''
    for cur in crypto_dict:
        text = text + cur + '\n'
    bot.reply_to(message, f'Возможна конвертация следующих валют:\n'
                          f'{text}')


@bot.message_handler(content_types=['text'])
def converter(message):
    # print(message.text)
    text_list = message.text.lower().replace(',', '.').split()
    # print(text_list)
    try:
        test_exception(text_list, crypto_dict)
    except APIException as a:
        bot.reply_to(message, a.ex_message)
        return
    except Exception as e:
        bot.reply_to(message, f'Что-то пошло не так...\n{e}')
        return

    else:
        convert = Currency(
            str(crypto_dict[text_list[0]]),
            str(crypto_dict[text_list[1]]),
            float(text_list[2])
        )
        result = convert.get_price()
        bot.reply_to(message, f'{convert.amount} {convert.base} это {result:.2f} {convert.quote}')


bot.polling(none_stop=True)
