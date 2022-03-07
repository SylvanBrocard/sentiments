from flask import Flask, render_template
from forms import ContactForm
from flask import request
import pandas as pd

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
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv')
        return "<p>Merci de nous avoir contactés.</p>"
    else:
        return render_template('contact.html', form=form)

@app.route("/about")
def about():
    return render_template('about.html')


app.run(debug=True)