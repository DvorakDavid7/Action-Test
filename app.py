from flask import Flask
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return f"Hello World {os.getenv('TEST')}"


if __name__ == '__main__':
    app.run()
