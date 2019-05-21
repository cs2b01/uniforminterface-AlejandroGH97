from flask import Flask,render_template, request, session, Response, redirect
from database import connector
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/usuarios', methods = ['GET'])
def usuarios():
    db_session = db.getSession(engine)
    return render_template('db.json')

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))
