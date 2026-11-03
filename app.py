from flask import Flask
from uuid import UUID

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"


@app.route("/user/<int:id>")
def user(id):
    return f" your id is {id}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"the item you brought is of {amount}"


@app.route("/files/<path:file_path>")
def files(file_path):
    return f" your file path is {file_path}"



@app.route("/students/<uuid:u_id>")
def students(u_id):
    return str(u_id)

# @app.route("/user/<name>/<course>")
# def user(name, course):
#     return f"hello {name},your course is {course}"




if __name__ == "__main__":
   app.run(debug=True)

