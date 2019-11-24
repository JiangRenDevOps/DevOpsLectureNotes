from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route("/stock/<code>")
def get_stock(code):
    return send_from_directory("csv_files/", code+".csv")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
