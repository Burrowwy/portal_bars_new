FROM python

RUN mkdir /app


COPY requirements.txt /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#RUN pip install -r requirements.txt

RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY ../../Desktop /app

WORKDIR /app

CMD ["python3", "manage.py", "runserver", "0:8000"]

EXPOSE 8000
