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


@app.route("/upload", methods=['POST'])
def upload():
    ## file upload ##
    img = request.files['image']

    ## GridFs를 통해 파일을 분할하여 DB에 저장하게 된다
    fs = gridfs.GridFS(db)
    file_img_id = fs.put(img)

    db.contents.insert_one({'img':file_img_id})

    return jsonify({'msg': '저장에 성공했습니다.'})


@app.route('/result')
def result():
    return render_template("result.html")

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)