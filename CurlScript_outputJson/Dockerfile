FROM python:3.9-alpine

WORKDIR /app
COPY CurlTelnetNslookup.py /app/CurlTelnetNslookup.py

RUN apk update && apk add --no-cache cron

RUN echo "0 9 * * * /usr/local/bin/python /app/CurlTelnetNslookup.py >> /var/log/cron.log 2>&1" >> /etc/crontabs/root && \
    echo "0 21 * * * /usr/local/bin/python /app/CurlTelnetNslookup.py >> /var/log/cron.log 2>&1" >> /etc/crontabs/root && \
    echo >> /etc/crontabs/root
    # empty line is required

RUN chmod 0644 /etc/cron.d/crontab

# RUN pip install some-package

CMD ["cron", "-f"]