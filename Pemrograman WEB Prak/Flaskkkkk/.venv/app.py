from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    hari = ["senin", "selasa", "rabu", "Kamis", "Jumattt"]
    return render_template("main_layout.html", value = hari)

if __name__=="__main__":
    app.run(debug=True)