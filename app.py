from flask import Flask,request,render_template
# from uuid import UUID

app = Flask(__name__)


@app.route("/")
def home():
    name = "Shahid"
    course = "Flask"
    city = "Delhi"
    age = 28
    return render_template("index.html",                name=name,
                           course=course
                           ,city=city,
                           age=age)

if __name__ == "__main__":
    app.run(debug=True)