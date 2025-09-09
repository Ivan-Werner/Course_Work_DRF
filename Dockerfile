FROM python:3.12

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONIOENCODING utf-8
ENV PYTHONUTF8 1
ENV PYTHONUNBUFFERED 1

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
