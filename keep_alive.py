from flask import Flask
from threading import Thread
import logging

app = Flask('')
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

@app.route('/')
def home():
    return "I'm alive 1"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()