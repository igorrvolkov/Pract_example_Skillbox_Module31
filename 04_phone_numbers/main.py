import re


def is_valid_num(phone_num: str) -> bool:
    """Функция валидации телефонного номера"""
    if re.match(r'[89][0-9]{9}', phone_num):
        return True
    return False


if __name__ == '__main__':
    # тестовые данные взяты отсюда: https://habr.com/ru/articles/110731/
    test_numbers = ['+79261234567',
                    '89261234567',
                    '79261234567',
                    '+7 926 123 45 67',
                    '8(926)123-45-67',
                    '123-45-67',
                    '9261234567',
                    '79261234567',
                    '(495)1234567',
                    '(495) 123 45 67',
                    '89261234567',
                    '8-926-123-45-67',
                    '8 927 1234 234',
                    '8 927 12 12 888',
                    '8 927 12 555 12',
                    '8 927 123 8 123']

    for index, number in enumerate(test_numbers, 1):
        if is_valid_num(number):
            result = 'всё в порядке'
        else:
            result = 'не подходит'
        print(f'{index}. {number}: {result}')
