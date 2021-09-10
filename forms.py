from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class UserSearchForm(FlaskForm):
    email = StringField('email')
    idNumber = IntegerField('idNumber')
    search = SubmitField('search')


class CustomerInfo(FlaskForm):
    email = StringField('email')
    idNumber = IntegerField('idNumber')
    title = StringField('title')
    name = StringField('name')
    phoneNumber = StringField('phoneNumber')
    passportNumber = IntegerField('passportNumber')
    propertyAddress = StringField('propertyAddress')
    propertyListedValue = IntegerField('propertyListedValue')
    sellingMandateEndDate = StringField('sellingMandateEndDate')
    submit = SubmitField('submit')
