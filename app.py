from flask import Flask
from uuid import UUID

app = Flask(__name__)

@app.route("/")
def home():
    return "home page hello flask"

@app.route("/user/<int:id>")
def user(id):
    return f"hello {id}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"hello {amount}"

@app.route("/stringsaccept/<string:any>")
def stringsaccept(any):
    return f"hello {any}"


@app.route("/files/<path:file_path>")
def files(file_path):
    return f"hello {file_path}"

@app.route("/student/<uuid:user_id>")
def student(user_id):
    return f"hello {user_id}"

if __name__ == "__main__":
    app.run(debug=True)