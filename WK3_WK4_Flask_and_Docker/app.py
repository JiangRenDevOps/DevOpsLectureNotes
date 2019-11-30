from flask import Flask, request, render_template, Response, url_for
from werkzeug.utils import secure_filename, redirect

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/abc')
def abc():
    return 'Hello abc'


@app.route('/upload')
def upload():
    return render_template('upload.html')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def send_content_to_process(person: Person):
    pass


@app.route('/post_my_info', methods=['POST'])
def post_my_info():
    content = request.json
    if "name" not in content or "age" not in content:
        return Response(status=404)
    print(content)
    send_content_to_process(Person(content["name"], content["age"]))
    return Response(status=201)


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        import os
        f.save(os.path.dirname(os.path.realpath(__file__)) + '/uploaded_files/' + secure_filename(f.filename))
        return Response("file uploaded successfully", status=201)

# Redirect
@app.route('/secrets')
def secrets():
    token = request.cookies.get('token')
    if not token or token != USERNAME + PASSWORD:
        return redirect(url_for('login'))
    return Response("The secret is you have successfully set the token via cookie when you login\n")


USERNAME = 'admin'
PASSWORD = 'admin'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            response = redirect(url_for('secrets'))
            response.set_cookie("token", USERNAME + PASSWORD)
            return response
        else:
            print("Invalid Credentials. Please try again")
            error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
