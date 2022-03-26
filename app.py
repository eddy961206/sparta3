from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def main():
    return render_template("main.html")

@app.route('/make')
def make():
    return render_template("make.html")

@app.route('/result')
def result():
    return render_template("result.html")

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)