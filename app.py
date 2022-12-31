import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://GeekyMovies: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@github.com/GeekyMovies/LazyPrincessV2 okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
