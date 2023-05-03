# attivazione dell'ambiente virtuale
#source .venv/bin/activate
export PATH=$PATH:/.chromedriver
export PORT=8080
# installazione delle dipendenze
pip install -r requirements.txt

# avvio del server Gunicorn con 4 worker process
gunicorn app:app -b 0.0.0.0:$PORT

sleep 10

# avvio del bot Selenium
#python app.py
