from flask import Flask, render_template, request, jsonify
import gridfs

app = Flask(__name__)

from pymongo import MongoClient
<<<<<<< HEAD

client = MongoClient('localhost', 27017)

db = client.baby_photo

=======
client = MongoClient('localhost', 27017)
db = client.baby_photo


>>>>>>> aadbb7e3ca604a49004e2f3c5ed53a99441c3eb2
@app.route('/')
def main():
    return render_template("main.html")

<<<<<<< HEAD
=======

>>>>>>> aadbb7e3ca604a49004e2f3c5ed53a99441c3eb2
@app.route('/make')
def make():
    return render_template("make.html")

<<<<<<< HEAD
@app.route('/upload', methods=['POST'])
=======
@app.route('/result')
def result():
    return render_template("result.html")



@app.route("/make", methods=['POST'])
>>>>>>> aadbb7e3ca604a49004e2f3c5ed53a99441c3eb2
def upload():
    babyname = request.form['baby_name']
    mothername = request.form['mother_name']
    fathername = request.form['father_name']
    birthyear = request.form['birth_year']
    birthmonth = request.form['birth_month']
    birthday = request.form['birth_day']
<<<<<<< HEAD
    db.contents.insert_one({'babyName': babyname, 'motherName': mothername, 'fatherName': fathername, 'birthYear': birthyear, 'birthMonth': birthmonth, 'birthDay': birthday})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
=======

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
>>>>>>> aadbb7e3ca604a49004e2f3c5ed53a99441c3eb2
