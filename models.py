from app import db


class Customer(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    idNumber = db.Column(db.Integer, unique=True)
    title = db.Column(db.String(120))
    name = db.Column(db.String(120))
    phoneNumber = db.Column(db.String(120))
    passportNumber = db.Column(db.String(120), nullable=True)
    propertyAddress = db.Column(db.String(120))
    propertyListedValue = db.Column(db.Integer)
    sellingMandateEndDate = db.Column(db.String(120))

    def __repr__(self):
        return '<User {}>'.format(self.name)
