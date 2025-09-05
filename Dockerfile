# FROM python:3.12
#
# WORKDIR /app
#
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
#
# COPY ..
#
# EXPOSE 8000
#
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
COPY ./requirements.txt /app/

# Устанавливаем зависимости
RUN pip install -r /app/requirements.txt

# Копируем код приложения в контейнер
COPY . .