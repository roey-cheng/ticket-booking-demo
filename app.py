from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book", methods=["GET","POST"])
def book():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}! Your booking form was received."
    return render_template("book.html")

if __name__ == "__main__":
    app.run(debug=True)