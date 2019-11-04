import requests
import json


def get_city_iata_code(city):
    link = f'http://autocomplete.travelpayouts.com/places2?term={city}&locale=ru&types[]=city'
    data = json.loads(requests.get(link).text)
    if data:
        return data[0]['code']
    else:
        return None


def get_price_one_way(origin, destination):
    link = f'http://min-prices.aviasales.ru/calendar_preload?one_way=true&origin={origin}&destination={destination}'
    data = json.loads(requests.get(link).text)
    if data['best_prices']:
        return data['best_prices'][0]
    else:
        return None


if __name__ == '__main__':
    origin = None
    destination = None

    while True:
        if not origin:
            city = input('Введите страну вылета: ')
            origin = get_city_iata_code(city)
            continue

        if not destination:
            city = input('Введите страну прибытия: ')
            destination = get_city_iata_code(city)
            continue

        print(f'Ищем цену билетов из {origin} в {destination}')
        data_info = get_price_one_way(origin, destination)
        if data_info:
            print(f'Дата отправления {data_info["depart_date"]}')
            print(f'Расстояние {data_info["distance"]}')
            print(f'Цена билета - {data_info["value"]} руб')
        else:
            print('Билеты не найдены')
        break
