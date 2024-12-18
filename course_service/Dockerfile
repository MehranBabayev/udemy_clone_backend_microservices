# Используем официальный образ Python как базовый
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Обновляем систему и устанавливаем зависимости для работы с PostgreSQL и Pillow
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . .

# Добавьте эту строку перед запуском Gunicorn
RUN python manage.py collectstatic --noinput

# Указываем, на каком порту будет работать Django
EXPOSE 8000

# Запускаем приложение с помощью Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "course_service.wsgi:application"]
