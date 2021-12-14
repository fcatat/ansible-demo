from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! This is production ENV ver 1.0'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        # this is production
        port=6000
    )
