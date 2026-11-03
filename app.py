from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"


@app.route("/user/<name>/<course>")
def user(name, course):
    return f"hello {name},your course is {course}"

if __name__ == "__main__":
   app.run(debug=True)

