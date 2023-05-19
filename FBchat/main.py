from flask import Flask, render_template, request

app = Flask(__name__)
messages = []

@app.route("/")
def home():
    return render_template("index.html", messages=messages)

@app.route("/send", methods=["POST"])
def send():
    message = request.form["message"]
    messages.append(message)
    return ""

@app.route("/delete/<int:message_id>", methods=["POST"])
def delete(message_id):
    del messages[message_id]
    return ""

if __name__ == "__main__":
    app.run(debug=True)
