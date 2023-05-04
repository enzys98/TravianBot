# Usa l'immagine di Python 3.9
FROM python:3.9-slim-buster

# Imposta la directory di lavoro nella cartella del tuo progetto
WORKDIR /app

# Copia i file del tuo progetto all'interno della cartella del container
COPY app.py
COPY requirements.txt

# Installa Chrome e Chromedriver
RUN apt-get update && apt-get install -y wget gnupg
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable
RUN LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver

# Installa le dipendenze necessarie del tuo progetto
RUN pip install --no-cache-dir -r requirements.txt

# Esporta la porta 8080 che verrà utilizzata da Render.com per eseguire l'app
EXPOSE 8080

# Avvia l'app
CMD ["python", "app.py"]
