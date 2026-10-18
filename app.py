from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return print("/")

@app.route("/audio/")
def audio():
    return render_template("audio.html")

@app.route("/audio/bar/")
def audio_bar():
    return render_template("bar.html")

@app.route("/audio/line/")
def audio_line():
    return render_template("line.html")

if __name__ == "__main__":
    app.run(debug=True, port=55555)