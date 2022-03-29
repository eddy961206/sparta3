from flask import Flask, render_template, request, jsonify
import gridfs

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.baby_photo


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/make')
def make():
    return render_template("make.html")

@app.route('/result')
def result():
    return render_template("result.html")



@app.route("/make", methods=['POST'])
def upload():
    babyname = request.form['baby_name']
    mothername = request.form['mother_name']
    fathername = request.form['father_name']
    birthyear = request.form['birth_year']
    birthmonth = request.form['birth_month']
    birthday = request.form['birth_day']

    doc = {
        'babyName': babyname,
        'motherName': mothername,
        'fatherName': fathername,
        'birthYear': birthyear,
        'birthMonth': birthmonth,
        'birthDay': birthday,
    }

    db.contents.insert_one(doc)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
