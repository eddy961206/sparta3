import codecs

from flask import Flask, render_template, request, jsonify
import gridfs
from werkzeug.utils import secure_filename

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.baby_photo
fs = gridfs.GridFS(db)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/make')
def make():
    return render_template("make.html")

@app.route('/result')
def result():
    return render_template("result.html")

@app.route("/make_photo", methods=['get', 'POST'])
def image_save():
    if request.method == 'POST':
        photo_1d = request.files['photo1d']
        photo_50d = request.files['photo50d']
        photo_100d = request.files['photo100d']
        photo_4mth = request.files['photo4mth']
        photo_5mth = request.files['photo5mth']
        photo_6mth = request.files['photo6mth']
        photo_7mth = request.files['photo7mth']
        photo_8mth = request.files['photo8mth']
        photo_9mth = request.files['photo9mth']
        photo_10mth = request.files['photo10mth']
        photo_11mth = request.files['photo11mth']
        photo_12mth = request.files['photo12mth']
        photo_1d.save('./static/' + secure_filename(photo_1d.filename))
        photo_50d.save('./static/' + secure_filename(photo_50d.filename))
        photo_100d.save('./static/' + secure_filename(photo_100d.filename))
        photo_4mth.save('./static/' + secure_filename(photo_4mth.filename))
        photo_5mth.save('./static/' + secure_filename(photo_5mth.filename))
        photo_6mth.save('./static/' + secure_filename(photo_6mth.filename))
        photo_7mth.save('./static/' + secure_filename(photo_7mth.filename))
        photo_8mth.save('./static/' + secure_filename(photo_8mth.filename))
        photo_9mth.save('./static/' + secure_filename(photo_9mth.filename))
        photo_10mth.save('./static/' + secure_filename(photo_10mth.filename))
        photo_11mth.save('./static/' + secure_filename(photo_11mth.filename))
        photo_12mth.save('./static/' + secure_filename(photo_12mth.filename))
        return 'uploads 디렉토리 -> 파일 업로드 성공!'



@app.route('/upload', methods=['POST'])
def upload():
    babyname = request.form['baby_name']
    mothername = request.form['mother_name']
    fathername = request.form['father_name']
    birthyear = request.form['birth_year']
    birthmonth = request.form['birth_month']
    birthday = request.form['birth_day']
    db.contents.insert_one({'babyName': babyname, 'motherName': mothername, 'fatherName': fathername, 'birthYear': birthyear, 'birthMonth': birthmonth, 'birthDay': birthday})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, debug=True)