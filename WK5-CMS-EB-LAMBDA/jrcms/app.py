from flask import Flask, request, render_template, Response, redirect
from data import ContentManager

app = Flask(__name__)
cm = ContentManager(app)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.ico')

@app.route('/content')
def get_content():
    contentKey = request.args.get('contentKey', default='Default')
    return Response(cm.get_content(contentKey), status=200)

@app.route('/content', methods=['PUT'])
def put_content():
    contentKey = request.form['contentKey']
    contentValue = request.form['contentValue']
    cm.set_content(contentKey, contentValue)
    return Response(status=200)

if __name__ == '__main__':
    import os
    port = os.environ.get("PORT", "8080")
    app.run(debug=True, host='0.0.0.0', port=port, threaded=True)
