FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt /app/

RUN apk add --virtual .build-deps --no-cache postgresql-libs postgresql-dev gcc python3-dev musl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk --purge del .build-deps

COPY [^data]* /app/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
