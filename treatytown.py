from chatbot import chatbot
from flask import Flask, render_template, request
import time

app  = Flask(__name__)


@app.route("/")
def home():
    return render_template("Chat.html")

@app.route("/chatbot")
def chatbotter():
    return render_template("Chatbot.html")

@app.route("/get")
def get_bot_response():
    time.sleep(0.5)
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
