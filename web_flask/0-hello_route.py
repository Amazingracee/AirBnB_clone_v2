#!/usr/bin/python3
"""
Starts a simple web application listening on 0.0.0.0:5000
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_Hbnb():
    """ Displays Hello HBNB on ::0:5000 """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
