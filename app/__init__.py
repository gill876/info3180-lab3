from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '}5[nY*(3%#nknmh"5K3X[+]LCj2g*Z#%^a<ez#U{'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'fb4f67bdb72464'
app.config['MAIL_PASSWORD'] = '07bf8323576841'
mail = Mail(app)
from app import views