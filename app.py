import os
import resend
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

resend.api_key = os.environ["RESEND_API_KEY"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book", methods=["GET","POST"])
def book():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        tickets = request.form["tickets"]

        return f"Hello, {name}! You requested {tickets} ticket(s). We would send confirmation to {email}."
    return render_template("book.html")

if __name__ == "__main__":
    app.run(debug=True)