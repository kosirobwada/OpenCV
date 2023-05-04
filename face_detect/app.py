from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
import numpy as np

app = Flask(__name__)

# 画像をアップロードするフォルダ
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 保存する画像のフォルダ
app.config['OUTPUT_FOLDER'] = 'static'

# Haar cascade分類器のパス
cascade_path = 'haarcascade_frontalface_default.xml'

# トップページ
@app.route('/')
def index():
    return render_template('index.html')

# 画像をアップロードして処理するページ
@app.route('/', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        # 画像ファイルを読み込む
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        # グレースケールに変換する
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Haar cascade分類器を読み込む
        cascade = cv2.CascadeClassifier(cascade_path)
        # 顔検出を行う
        faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        # 矩形を描画する
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 結果を保存する
        cv2.imwrite(os.path.join(app.config['OUTPUT_FOLDER'], 'result.jpg'), img)
        return redirect(url_for('result'))
    else:
        return redirect(request.url)

# 処理結果を表示するページ
@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
