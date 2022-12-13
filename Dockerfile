FROM alpine:3.16.2

# installazione python e pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

EXPOSE 80

WORKDIR /
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# docker build -t orders-customers .
# docker run -p 80:80 orders-customers
