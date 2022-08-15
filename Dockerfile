FROM python:alpine as build
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt 

FROM python:alpine as production
COPY --from=build /install /usr/local
COPY src /usr/src/bot
WORKDIR /usr/src/bot
CMD python InsultBot.py
