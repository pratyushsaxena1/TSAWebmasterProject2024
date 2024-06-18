from flask import Flask, render_template, redirect, request, url_for
import smtplib, ssl
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/problem')
def greenenergy():
    return render_template("problem.html")

@app.route('/solutions')
def solutions():
    return render_template("solutions.html")

@app.route('/contact', methods=('GET', 'POST'))
def contact():
    if request.method == 'POST':
        firstName = request.form['first-name']
        lastName = request.form['last-name']
        email = request.form['email']
        message = request.form['message']

        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        sender = "pureearthweb2024@gmail.com"
        password = "xudo xxax ghym mree"

        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)

        server.ehlo()
        server.starttls(context=context)
        server.ehlo()

        server.login(sender, password)

        msg = EmailMessage()
        msg.set_content(message)
        msg["Subject"] = "NEW EMAIL - " + firstName + " " + lastName + " - " + email
        msg["From"] = sender
        msg["To"] = sender

        server.send_message(msg)

        server.quit()
        return redirect(url_for('home'))
    return render_template("contact.html")

@app.route('/sources')
def sources():
    return render_template("sources.html")

if __name__ == "__main__":
    app.run(port=5001, debug=True)
