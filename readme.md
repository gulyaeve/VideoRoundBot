# Чат-бот для телеграм, превращающий видео в ведеосообщения в кружочках

Бот работает на aiogram 3.x.x и использует ffmpeg

Для работы нужно создать папку `temp` файл `.env` с переменными:
- `TOKEN` - токен бота
- `ADMIN_ID` - id администратора в телеграм

### Запуск через python
1) Устновить всё из requirements: `pip install -r requirements.txt`
2) Запустить `python3 main.py`

### Запуск через Docker
`docker-compose up -d`
