# attivazione dell'ambiente virtuale
source .venv/bin/activate

# installazione delle dipendenze
pip install -r requirements.txt

# avvio del server Gunicorn con 4 worker process
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app &
sleep 10

# avvio del bot Selenium
python app.py