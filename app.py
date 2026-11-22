from flask import Flask,request,render_template
# from uuid import UUID

app = Flask(__name__)


@app.route("/")
def home():
    first_name = "John"
    last_name = "wick"
    course = ["Flask","python",'DSA','FastAPI']
    city = "Delhi"
    price = 500
    return render_template("index.html",                first_name=first_name,
                           last_name=last_name,
                           course=course
                           ,city=city,
                           price=price)

if __name__ == "__main__":
    app.run(debug=True)