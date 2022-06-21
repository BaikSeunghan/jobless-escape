import json
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

# Flask
app = Flask(__name__)
# .env
load_dotenv()
ID = os.environ.get('DB_ID')
PW = os.environ.get('DB_PW')
# DB
client = MongoClient("mongodb+srv://"+ID+":"+PW+"@joblessescape.dvnaltz.mongodb.net/?retryWrites=true&w=majority")
db = client.joblessescape

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/quiz/<index>', methods=["GET"])
def quiz(index):
    quiz_list = list(db.quiz.find({}, {'_id': False}))
    quiz_index = db.quiz.find_one({'id': index})['id']
    quiz_content = db.quiz.find_one({'id': index})['quiz']
    quiz_answer = db.quiz.find_one({'id': index})['quiz_answer']

    return render_template('quiz.html', quiz_list=quiz_list, quiz_index=quiz_index, quiz_content=quiz_content, quiz_answer=quiz_answer)

@app.route('/quiz/<index>', methods=["POST"])
def checking(index):
    quiz_list = list(db.quiz.find({}, {'_id': False}))

    return render_template('quiz.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=4000, debug=True)
