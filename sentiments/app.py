from time import sleep
from flask import Flask, render_template
from forms import ContactForm, SummarizeForm
from flask import request
import psycopg2
import requests
import json

###############################################
#          Define flask app                   #
###############################################
app = Flask(__name__)
app.secret_key = 'secretKey'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


###############################################
#       Render Contact page                   #
###############################################
@app.route("/contact", methods=["GET", "POST"])
def get_contact():
    form = ContactForm()
    # here, if the request type is a POST we get the data on contat
    #forms and save them else we return the contact forms html page
    if request.method == 'POST':
        name =  "'" + request.form["name"] + "'"
        email = "'" + request.form["email"] + "'"
        subject = "'" + request.form["subject"] + "'"
        message = "'" + request.form["message"] + "'"
        global id
        
        conn = get_connection()

        curr = conn.cursor()

        curr.execute(f"""INSERT INTO clients (id, name, email, subject, message) VALUES ({id},{name}, {email},{subject},{message});""")
        id+=1

        conn.close()
        # res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        # res.to_csv('./contactusMessage.csv')
        return "<p>Merci de nous avoir contactés.</p>"

    else:
        return render_template('contact.html', form=form)

@app.route("/about")
def about():
    return render_template('about.html')



###############################################
#       Connection to postgres database       #
###############################################
def get_connection():
    try:
        conn = psycopg2.connect(
            database="messages",
            user="wym_admin",
            password="admin",
            host="db",
            port=5432,
        )
        conn.autocommit = True
        return conn
    except:
        return False

conn = False
while not conn:
    conn = get_connection() # create connection object

    if conn:
        print("Connection to the PostgreSQL established successfully.", flush=True)
        curr = conn.cursor() # cursor object
        # create table in database
        curr.execute("""CREATE TABLE IF NOT EXISTS clients (
                        id serial PRIMARY KEY,
                        name TEXT,
                        email TEXT,
                        subject TEXT,
                        message TEXT);
                        """)
        id = 0 # initialize id at 0

        conn.close() # close connection to database
    else:
        print("Waiting for connection to PostgreSQL...", flush=True)
        sleep(2)


###############################################
#         Post on IBM text Summarizer         #
###############################################
@app.route("/model", methods=["GET", "POST"])
def summarize():
    form = SummarizeForm()
    # here, if the request type is a POST we get the data from
    #forms and save them else we return the forms html page
    if request.method == 'POST':
        userTxt =  "'" + request.form["text"] + "'"

        url = "http://model:5000/model/predict"
        data = {
        "text": [
            userTxt
            ]
        }

        res = requests.post(url, json=data)
        test = json.loads(res.text)

        return f"<h2>Your text</h2> <p> {userTxt} </p> <h2>Your text summarized </h2> <p>{test['summary_text'][0]}</p>"

    else:
        return render_template('model.html', form=form)


app.run(host="0.0.0.0", port=8000, debug=True)