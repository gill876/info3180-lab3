from flask import Flask
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
#REMOVED app.config['SECRET_KEY'], app.config['MAIL_SERVER'], app.config['MAIL_PORT'], app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']

mail = Mail(app)
csrf = CSRFProtect(app)
csrf.init_app(app)

from app import views