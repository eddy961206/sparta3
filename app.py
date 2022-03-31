import codecs

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

@app.route("/make_photo", methods=['POST'])
def image_save():
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
    fs = gridfs.GridFS(db)
    photo_1d_img = fs.put(photo_1d)
    photo_50d_img = fs.put(photo_50d)
    photo_100d_img = fs.put(photo_100d)
    photo_4mth_img = fs.put(photo_4mth)
    photo_5mth_img = fs.put(photo_5mth)
    photo_6mth_img = fs.put(photo_6mth)
    photo_7mth_img = fs.put(photo_7mth)
    photo_8mth_img = fs.put(photo_8mth)
    photo_9mth_img = fs.put(photo_9mth)
    photo_10mth_img = fs.put(photo_10mth)
    photo_11mth_img = fs.put(photo_11mth)
    photo_12mth_img = fs.put(photo_12mth)
    db.photos.insert_one({'img_1d': photo_1d_img})
    db.photos.insert_one({'img_50d': photo_50d_img})
    db.photos.insert_one({'img_100d': photo_100d_img})
    db.photos.insert_one({'img_4mth': photo_4mth_img})
    db.photos.insert_one({'img_5mth': photo_5mth_img})
    db.photos.insert_one({'img_6mth': photo_6mth_img})
    db.photos.insert_one({'img_7mth': photo_7mth_img})
    db.photos.insert_one({'img_8mth': photo_8mth_img})
    db.photos.insert_one({'img_9mth': photo_9mth_img})
    db.photos.insert_one({'img_10mth': photo_10mth_img})
    db.photos.insert_one({'img_11mth': photo_11mth_img})
    db.photos.insert_one({'img_12mth': photo_12mth_img})
    return jsonify({'msg': '저장이 완료되었습니다!'})

    item = photos.find_one({'img_50d': photo_50d_img})
    img_50d_binary = fs.get(item['img_50d']).read()
    base64_img_50d = codecs.encode(img_50d_binary.read(), 'base64')
    decoded_img_50d = base64_img_50d.decode('utf-8')
    item['img_50d'] = decoded_img_50d




@app.route('/upload', methods=['POST'])
def upload():
    babyname = request.form['baby_name']
    mothername = request.form['mother_name']
    fathername = request.form['father_name']
    birthyear = request.form['birth_year']
    birthmonth = request.form['birth_month']
    birthday = request.form['birth_day']
    db.contents.insert_one({'babyName': babyname, 'motherName': mothername, 'fatherName': fathername, 'birthYear': birthyear, 'birthMonth': birthmonth, 'birthDay': birthday})


# @app.route("/make_photo", methods=['GET'])
# def image_saves():




if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
