from flask import Flask,request,render_template
# from uuid import UUID

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html.j2")

@app.route("/about")
def about():
    return render_template("about.html.j2")


@app.route("/contact")
def contact():
    return render_template("contact.html.j2")

if __name__ == "__main__":
    app.run(debug=True)