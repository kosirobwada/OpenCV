from flask import Flask, render_template, request
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # アップロードされたファイルを取得
    file = request.files['file']
    img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)

    # Canny法でエッジ検出を行う
    edges = cv2.Canny(img, 100, 200)

    # エッジ画像をbase64形式に変換
    _, buffer = cv2.imencode('.jpg', edges)
    edge_img_str = base64.b64encode(buffer).decode('utf-8')

    # 元画像をbase64形式に変換
    _, buffer = cv2.imencode('.jpg', img)
    img_str = base64.b64encode(buffer).decode('utf-8')

    # HTMLに渡すデータを設定
    data = {'img_str': img_str, 'edge_img_str': edge_img_str}

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
