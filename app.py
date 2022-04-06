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


@app.route('/findresult')
def findresult():
    return render_template('findresult.html')


@app.route('/findemail', methods=['POST'])
def findemail():
    femail = request.form['femail']
    db.findEmail.insert_one({'femail': femail})



@app.route("/make_photo", methods=['GET', 'POST'])
def image_save():
    # id값 받아오는 중복 부분 중복 제거
    newdata = list(db.contents.find({}))[-1]
    _id = newdata['email']
    if request.method == 'POST':
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
        photo_present.save(newfolder + 'a_photo_present' + secure_filename(photo_present.filename))
        photo_family.save(newfolder + 'b_photo_family' + secure_filename(photo_family.filename))
        photo_1d.save(newfolder + 'c_photo_1d' + secure_filename(photo_1d.filename))
        photo_50d.save(newfolder + 'd_photo_50d' + secure_filename(photo_50d.filename))
        photo_100d.save(newfolder + 'e_photo_100d' + secure_filename(photo_100d.filename))
        photo_4mth.save(newfolder + 'f_photo_4mth' + secure_filename(photo_4mth.filename))
        photo_5mth.save(newfolder + 'g_photo_5mth' + secure_filename(photo_5mth.filename))
        photo_6mth.save(newfolder + 'h_photo_6mth' + secure_filename(photo_6mth.filename))
        photo_7mth.save(newfolder + 'i_photo_7mth' + secure_filename(photo_7mth.filename))
        photo_8mth.save(newfolder + 'j_photo_8mth' + secure_filename(photo_8mth.filename))
        photo_9mth.save(newfolder + 'k_photo_9mth' + secure_filename(photo_9mth.filename))
        photo_10mth.save(newfolder + 'l_photo_10mth' + secure_filename(photo_10mth.filename))
        photo_11mth.save(newfolder + 'm_photo_11mth' + secure_filename(photo_11mth.filename))
        photo_12mth.save(newfolder + 'n_photo_12mth' + secure_filename(photo_12mth.filename))

        return 'uploads 디렉토리 -> 파일 업로드 성공!'

    else: # if request.method == 'GET':
        photos = os.listdir('./static/' + str(_id) + '/') # static/id로 만든 폴더 안의 파일 리스트를 photos 변수에 저장
        return jsonify({'all_photos': photos, 'id': str(_id)}) # photos 변수에 담긴 파일리스트와 id값을 함께 json 형태로 전달


@app.route('/upload', methods=['POST'])
def upload():
    email = request.form['email']
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
         'birthMonth': birthmonth, 'birthDay': birthday,'birthHour':birthhour, 'birthMinute': birthminute, 'email': email })


@app.route('/info', methods=['GET'])
def read_info():
    info = list(db.contents.find({}, {'_id': False}))
    return jsonify({'all_info': info})



@app.route('/find_photo', methods=['GET'])
def find_photo():
    findinfo = list(db.findEmail.find({}, {'_id': False}))[-1]
    print(findinfo)
    _id = findinfo['femail']
    print(id)
    photos = os.listdir('./static/' + str(_id) + '/')
    print(photos)
    return jsonify({'all_photos': photos, 'id': str(_id)})



@app.route('/find_info', methods=['GET'])
def find_info():
    findinfo = list(db.findEmail.find({}, {'_id': False}))[-1]
    print(findinfo)
    _id = findinfo['femail']
    newdata = list(db.contents.find({'email': _id}, {'_id': False}))
    print(newdata)
    return jsonify({'all_info': newdata})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)