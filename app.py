import os

from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

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


@app.route("/make_photo", methods=['get', 'POST'])
def image_save():
    if request.method == 'POST':
        newdata = list(db.contents.find({}))[-1]
        _id = newdata['_id']
        current_path = './static/'
        if not os.path.isdir(current_path + "/" + str(_id)): os.makedirs(current_path + "/" + str(_id))
        newfolder = current_path + "/" + str(_id) + "/"

        photo_present = request.files['photopresent']
        photo_family = request.files['photofamily']
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

        photo_present.save(newfolder + 'photo_present' + secure_filename(photo_present.filename))
        photo_family.save(newfolder + 'photo_family' + secure_filename(photo_family.filename))
        photo_1d.save(newfolder + 'photo_1d' + secure_filename(photo_1d.filename))
        photo_50d.save(newfolder + 'photo_50d' + secure_filename(photo_50d.filename))
        photo_100d.save(newfolder + 'photo_100d' + secure_filename(photo_100d.filename))
        photo_4mth.save(newfolder + 'photo_4mth' + secure_filename(photo_4mth.filename))
        photo_5mth.save(newfolder + 'photo_5mth' + secure_filename(photo_5mth.filename))
        photo_6mth.save(newfolder + 'photo_6mth' + secure_filename(photo_6mth.filename))
        photo_7mth.save(newfolder + 'photo_7mth' + secure_filename(photo_7mth.filename))
        photo_8mth.save(newfolder + 'photo_8mth' + secure_filename(photo_8mth.filename))
        photo_9mth.save(newfolder + 'photo_9mth' + secure_filename(photo_9mth.filename))
        photo_10mth.save(newfolder + 'photo_10mth' + secure_filename(photo_10mth.filename))
        photo_11mth.save(newfolder + 'photo_11mth' + secure_filename(photo_11mth.filename))
        photo_12mth.save(newfolder + 'photo_12mth' + secure_filename(photo_12mth.filename))
        return 'uploads 디렉토리 -> 파일 업로드 성공!'


@app.route('/upload', methods=['POST'])
def upload():
    babyname = request.form['baby_name']
    mothername = request.form['mother_name']
    fathername = request.form['father_name']
    birthyear = request.form['birth_year']
    birthmonth = request.form['birth_month']
    birthday = request.form['birth_day']
    birthhour = request.form['birth_hour']
    birthminute = request.form['birth_minute']

    db.contents.insert_one(
        {'babyName': babyname, 'motherName': mothername, 'fatherName': fathername, 'birthYear': birthyear,
         'birthMonth': birthmonth, 'birthDay': birthday,'birthHour':birthhour, 'birthMinute': birthminute })


@app.route('/info', methods=['GET'])
def read_info():
    info = list(db.contents.find({}, {'_id': False}))
    return jsonify({'all_info': info})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
