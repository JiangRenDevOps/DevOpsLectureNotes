from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    import city_matcher
    return city_matcher.get_cities(request.args.get('city'))

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
