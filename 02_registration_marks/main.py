import re

if __name__ == '__main__':
    raw_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
    private_numbers = re.findall(r'[АВЕКМНОРСТУХ][0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}', raw_numbers)
    taxi_numbers = re.findall(r'[АВЕКМНОРСТУХ]{2}[0-9]{5,6}', raw_numbers)
    print(f'Список номеров частных автомобилей: {private_numbers}')
    print(f'Список номеров такси: {taxi_numbers}')
