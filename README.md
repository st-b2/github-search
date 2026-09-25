# 🔎 GitHub Search

Две версии CLI-утилиты для поиска репозиториев на GitHub через официальное API.

## 📦 Файлы

| Файл | Описание |
|---|---|
| `github_search_N_args.py` | Интерактивная версия. Запрашивает данные через `input()`. |
| `github_search_args.py` | Версия с CLI-флагами (`argparse`). Удобна для скриптов и автоматизации. |

## ⚙ Требования

- Python 3.11+
- requests

## 🚀 Установка:

```bash
pip install requests
```

## 🌟 Использование

1. Интерактивная версия (...`_N_args`)
```bash
python github_search_N_args.py
```
Скрипт спросит:
```text
Что вы ищите: cybersec
Сколько вы хотите видеть результатов: 5
```
Сортировка всегда по звёздам, число результатов — с проверкой на положительное целое.

2. Версия с аргументами (...`_args`)
```bash
python github_search_args.py cybersec
python github_search_args.py "web scraper" -n 10 -l python -s stars
```
## 📑 Аргументы github_search_args.py

| Флаг | Описание | По умолчанию
|---|---|---|
| query |	Поисковый запрос (обязательный) |	— |
| -n, --num	| Сколько результатов показать | 5 |
| -s, --sort	| Сортировка: stars, forks, updated, help-wanted-issues | stars |
| -l, --language | Фильтр по языку (например, python) |	— |

Справка:
```bash

python github_search_args.py --help
```
## 💡 Пример вывода
```text

Найдено репозиториев: 12345

torvalds/linux — 180000 ⭐
URL: https://github.com/torvalds/linux
```

## ☄ Примечания

- Обе версии используют публичное GitHub API без токена.
- Без токена лимит — ~10 запросов в минуту. 
- Максимум результатов за один запрос: 100.
