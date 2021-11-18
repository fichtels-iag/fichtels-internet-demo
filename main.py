from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='')


@app.route("/")
def index():
    return send_from_directory('html', 'index.html')

@app.route("/1")
def send_static():
    return send_from_directory('html', 'static.html')

@app.route("/2")
def send_interaction():
    return send_from_directory('html', 'interaction.html')

@app.route("/3")
def send_dynamic():
    return send_from_directory('html', 'dynamic.html')

@app.route('/functions.js')
def send_js():
    return send_from_directory('html', 'functions.js')

@app.route('/style.css')
def send_css():
    return send_from_directory('html', 'style.css')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)