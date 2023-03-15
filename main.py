from flask import Flask, render_template
import json
from datetime import datetime
from flask import request


# download mess from file
def load_mess():
    with open('db.json', 'r') as json_file:
        data = json.load(json_file)
    return data['messages']


# add new mess
def add_mess(sender, text):
    new_message = {
        'text': text,
        'sender': sender,
        'time': datetime.now().strftime('%H:%M')
    }

    all_messages.append(new_message)


# save mess to file
def save_mes():
    data = {
        'messages': all_messages
    }

    with open('db.json', 'w') as f:
        json.dump(data, f)


all_messages = load_mess()

app = Flask(__name__)


@app.route('/')
def index_page():
    return 'hi'


@app.route('/chat')
def display_chat():
    return render_template('index.html', contextvars='stylesheet.html')


@app.route('/get_messages')
def get_messages():
    return {'messages': all_messages}


@app.route('/send_message')
def send_message():
    sender = request.args['name']
    text = request.args['text']
    add_mess(sender, text)
    save_mes()
    return 'ok'


@app.route('/future')
def future():
    return render_template('future.html')


@app.route('/donats')
def donats():
    return render_template('donats.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(host='0.0.0.0', port=80)
