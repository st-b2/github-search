import argparse
import requests


def parse_args():
    parser = argparse.ArgumentParser(
        description='Поиск репозиториев на GitHub'
    )
    parser.add_argument(
        'query',
        help='Поисковый запрос (что искать)'
    )
    parser.add_argument(
        '-n', '--num',
        type=int,
        default=5,
        help='Сколько результатов показать (по умолчанию: 5)'
    )
    parser.add_argument(
        '-s', '--sort',
        choices=['stars', 'forks', 'updated', 'help-wanted-issues'],
        default='stars',
        help='Сортировка результатов (по умолчанию: stars)'
    )
    parser.add_argument(
        '-l', '--language',
        default=None,
        help='Фильтр по языку программирования (например: python)'
    )
    return parser.parse_args()


def search_repos(query, num, sort, language):
    q = query
    if language:
        q += f' language:{language}'

    payload = {'q': q, 'sort': sort}
    r = requests.get('https://api.github.com/search/repositories',
                     params=payload,
    )
    return r

def main():
    args = parse_args()



if __name__ == '__main__':
    main()