import os
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from dotenv import load_dotenv
import sqlite3

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Configure Flask-Mail using environment variables
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')  # Get from environment variable
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')  # Get from environment variable
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('EMAIL_USER')

mail = Mail(app)

# Create the database
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS contacts (name TEXT, email TEXT)')
    conn.close()

# Initialize the database
init_db()

@app.route('/')
def index():
    return render_template('index.html')  # Ensure your HTML file is in the templates folder

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']

    # Save to database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

    # Send an email
    msg = Message('New Contact Form Submission',
                  sender=email,
                  recipients=[os.getenv('EMAIL_USER')])
    msg.body = f"Name: {name}\nEmail: {email}"
    
    try:
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")  # Log the error if email sending fails

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
