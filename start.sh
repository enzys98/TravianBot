source ./venv/bin/activate

# avvio del server Gunicorn con 4 worker process
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app &

# attesa per il completamento dell'avvio del server
sleep 10

pip install -r requirements.txt

# avvio del bot Selenium
python app.py