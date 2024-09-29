FROM ubuntu:22.04

FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    libnss3 \
    libgconf-2-4 \
    libxss1 \
    libappindicator3-1 \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libgbm-dev \
    libasound2 \
    libu2f-udev \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Fetch the latest stable Chrome version and install Chrome and ChromeDriver
RUN CHROME_VERSION=$(curl -sSL https://googlechromelabs.github.io/chrome-for-testing/ | awk -F 'Version:' '/Stable/ {print $2}' | awk '{print $1}' | sed 's/<code>//g; s/<\/code>//g') && \
CHROME_URL="https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chrome-linux64.zip" && \
echo "Fetching Chrome version: ${CHROME_VERSION}" && \
curl -sSL ${CHROME_URL} -o /tmp/chrome-linux64.zip && \
mkdir -p /opt/google/chrome && \
mkdir -p /usr/local/bin && \
unzip -q /tmp/chrome-linux64.zip -d /opt/google/chrome && \
rm /tmp/chrome-linux64.zip

# RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
#     && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
#     && apt-get update \
#     && apt-get install -y google-chrome-stable \
#     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV NAME Scraper

EXPOSE 5000

CMD ["python", "main.py"]