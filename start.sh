# attivazione dell'ambiente virtuale
#source .venv/bin/activate

export PATH=$PATH:/.chromedriver

# installazione delle dipendenze
pip install -r requirements.txt

# avvio del server Gunicorn con 4 worker process
gunicorn app:app -b 0.0.0.0:8000

sleep 10

# avvio del bot Selenium
#python app.py
