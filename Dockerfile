# Берем нужный базовый образ
FROM python:3.8-alpine
# Копируем все файлы из текущей директории в /app контейнера
COPY ./ /app
# Устанавливаем все зависимости
RUN apk update && python -m pip install --upgrade pip && python -m pip install flake8 pytest
# Устанавливаем приложение (Подробнее смотри Distutils)
CMD python /app/src/app.py
# Говорим контейнеру какой порт слушай
EXPOSE 8080
# Запуск нашего приложения при старте контейнера
CMD web_server