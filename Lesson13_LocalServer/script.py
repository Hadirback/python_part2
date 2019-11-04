import requests
from time import sleep

link =  'http://127.0.0.1:5000/secret_page?key='

for n in range(70, 100):
    request_link = link + str(n)
    resp = requests.get(request_link).text
    if resp == "Incorrect Key!":
        print(f'Проверено значение {n}. оно не подошло!')
        sleep(1)
    else:
        print(f'FOUND - {n}')
        break