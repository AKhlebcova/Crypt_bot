from extensions import APIException


def test_exception(text_list, crypto_dict):
    if len(text_list) != 3:
        raise APIException('Вы ввели неверное количество параметров. \nВведите: '
                           '<имя валюты покупки><имя валюты продажи><количество покупаемой валюты>')

    try:
        for i in text_list[:2]:
            crypto_dict[i]
    except KeyError:
        raise APIException(f'Вы ввели неверные или отсутствующие имена валют <{i}>: '
                           f'попробуйте заново или обратитесь к /values')

    if text_list[0] == text_list[1]:
        raise APIException(f'Вы ввели одинаковые имена валюты покупки <{text_list[0]}> и '
                           f'валюты продажи <{text_list[1]}>.\n'
                           'Повторите ввод заново.')

    try:
        float(text_list[2])
    except ValueError:
        raise APIException(f'Вы ввели невеpное <количество покупаемой валюты> <{text_list[2]}> - должно'
                           f' быть целое число или десятичная дробь.\n'
                           'Попробуйте заново.')

    if float(text_list[2]) <= 0:
        raise APIException(f'Вы ввели невеное <количество покупаемой валюты> <{text_list[2]}> - '
                           f'не должно быть меньше или равно нулю.\n'
                           'Попробуйте заново.')
