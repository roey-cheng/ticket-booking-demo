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

        params = {
            "from": "Ticket Booking Demo <tickets@mail.chruyi.com>",
            "to": [email],
            "subject": "Your ticket booking confirmation",
            "html": f"""
                <h1>Booking received!</h1>
                <p>Hi {name},</p>
                <p>You requested {tickets} ticket(s) for Summer Music Festival.</p>
            """
        }

        resend.Emails.send(params)

        return f"Hello, {name}! Your booking confirmation was sent to {email}."
    
    return render_template("book.html")

if __name__ == "__main__":
    app.run(debug=True)