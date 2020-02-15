from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    fullname = StringField('Please enter your full name', validators=[DataRequired()])
    email = StringField('Please enter your e-mail address', validators=[DataRequired(), Email()])
    subject = StringField('Please enter the subject for your message', validators=[DataRequired()])
    message = TextAreaField('Please enter the message you would like to send', validators=[DataRequired()])