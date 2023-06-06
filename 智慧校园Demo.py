from flask import Flask, request, render_template, redirect, url_for
import threading
import time

app = Flask(__name__)

# 定义一个每分钟打印一次信息的函数
def print_message_every_minute():
    while True:
        print("\033[91m 注意：请在浏览器打开 127.0.0.1 \033[0m")
        print("\033[91m       请勿关闭此命令行窗口！ \033[0m")
        time.sleep(60)  # 等待60秒

# 在一个新的线程中启动这个函数
threading.Thread(target=print_message_every_minute, daemon=True).start()

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'admin':
        return redirect(url_for('index'))
    else:
        return redirect(url_for('home', failed='true'))

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/1')
def page1():
    return render_template('1.html')

@app.route('/2')
def page2():
    return render_template('2.html')

@app.route('/3')
def page3():
    return render_template('3.html')

@app.route('/4')
def page4():
    return render_template('4.html')

@app.route('/5')
def page5():
    return render_template('5.html')

@app.route('/6')
def page6():
    return render_template('6.html')

@app.route('/7')
def page7():
    return render_template('7.html')

@app.route('/8')
def page8():
    return render_template('8.html')

@app.route('/9')
def page9():
    return render_template('9.html')

@app.route('/10')
def page10():
    return render_template('10.html')

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)
