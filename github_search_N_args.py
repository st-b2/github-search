import requests

res = input('Что вы ищите: ')

while True:
    try:
        num = int(input('Сколько вы хотите видеть результатов: '))
        if num > 0:
            break
        print('Введите число больше 0')
    except ValueError:
        print('Это не число !')

pyload = {'q':res, 'sort':'stars'}
r = requests.get('https://api.github.com/search/repositories', params=pyload)

if r.status_code == 200:
    data = r.json()
    print('Найдено репозиториев: ', data['total_count'])
    for repo in data['items'][:num]:
        print(repo['full_name'], '-', repo['stargazers_count'], '⭐')
        print('URL: ', r.url, '\n')
