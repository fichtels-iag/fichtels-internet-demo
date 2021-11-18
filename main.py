import os

from flask import Flask, send_from_directory, render_template, request

from database import create_table, get_all_messages, add_data

app = Flask(__name__, static_url_path='')


@app.route("/")
def index():
    return render_template('index.html', messages=get_all_messages())


@app.route("/statisch")
def send_static():
    return render_template('static.html', messages=get_all_messages())


@app.route('/interaktion', methods=['POST', 'GET'])
def send_interaction():
    if request.method == 'POST':
        form_data = request.form
        add_data(form_data['message'])
    return render_template('interaction.html', messages=get_all_messages())

@app.route('/style.css')
def send_css():
    return send_from_directory('static', 'style.css')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
