import prometheus_client as prometheus_client
from flask import Flask, Response

from app_helper import setup_metrics

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
app = Flask(__name__)
setup_metrics(app)


@app.route('/test/')
def test():
    return 'rest'


@app.route('/test1/')
def test1():
    1/0
    return 'rest'


@app.errorhandler(500)
def handle_500(error):
    return str(error), 500


# The generate_latest() function generates the latest metrics and sets the content type to indicate the Prometheus
# server that we are sending the metrics in text format using the 0.0.4 version.
@app.route('/metrics/')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.run()