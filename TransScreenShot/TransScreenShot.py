import os
import sys
from PIL import Image
import pyocr
#Tesseractのインストール場所をOSに教える
tesseract_path = "C:\Program Files\Tesseract-OCR"
if tesseract_path not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + tesseract_path
    #OCRエンジンを取得する
tools = pyocr.get_available_tools() 
if len(tools) == 0:
    print("OCRエンジンが指定されていません")
    sys.exit(1)
else:
    tool = tools[0]
#画像の読み込み
img = Image.open("img.png")
#文字を読み取る
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
result = tool.image_to_string(img,lang="jpn",builder=builder)
#結果を出力する
print(result)
import openai

# OpenAI APIの設定
openai.api_key = ""  # 自分のAPIキーに置き換えてください

# ChatGPTへの質問と応答の関数
def ask_question(question):
    prompt = f"ディープラーニングに関する問題について選択肢を選んでください。質問: {question}\n回答:"

    # ChatGPTに質問を送信して応答を取得
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,  # 応答の最大トークン数を設定
        n=1,  # 取得する応答の数
        stop=None,  # 自動的に応答を終了させない
        temperature=0.3,  # 応答の多様性を調整
    )

    # 応答から回答部分のテキストを取得
    answer = response.choices[0].text.strip()

    return answer

# 画像からテキストを読み取る
img = Image.open("img.png")
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
result = tool.image_to_string(img, lang="jpn", builder=builder)

# テキストをChatGPTに送信して質問する
question = result  # 画像から読み取ったテキストを質問として使用
answer = ask_question(question)

# 結果を出力する
print("質問:", question)
print("回答:", answer)
