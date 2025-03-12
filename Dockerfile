FROM python:3.13-slim-bookworm
# Debian 12 release (bookworm)
MAINTAINER Amit Pandey

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    make \
    build-essential \
    unixodbc \
    unixodbc-dev \
    gnupg2 \
    cron \
    procps \
    libfuzzy-dev \
    rsyslog \
    jq \
    bash \
    && rm -rf /var/lib/apt/lists/*

ADD src/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt

ADD src /
CMD ["uvicorn", "app.main:fapp", "--host", "0.0.0.0", "--port", "80"]
