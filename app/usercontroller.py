from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

#No hacer en produccion 0.0.0.0


if __name__ == '__main__':
    app.run(host='0.0.0.0')
