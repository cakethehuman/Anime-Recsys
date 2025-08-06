from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    print("gg")
    

if __name__ == "main":
    app.run(debug=True)