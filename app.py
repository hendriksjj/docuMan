from flask import Flask, request, redirect, url_for
from flask import render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from forms import UserSearchForm, CustomerInfo


dummy_data = {'jFerreira@gmail.com':
    {
        'email': 'jFerreira@gmail.com',
        'idNumber': 8109156184084,
        'title': 'Mr',
        'name': 'Johann Ferreira',
        'phoneNumber': '0824675464',
        'passportNumber': '',
        'propertyAddress': '134 Peterson Drive, Randburg',
        'propertyListedValue': 1600000,
        'sellingMandateEndDate': '31-10-2021'

    }

}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Customer
db.create_all()

for key, my_customer in dummy_data.items():
    Customer = Customer(
        email=my_customer['email'],
        idNumber=my_customer['idNumber'],
        title=my_customer['title'],
        name=my_customer['name'],
        phoneNumber=my_customer['phoneNumber'],
        passportNumber=my_customer['passportNumber'],
        propertyAddress=my_customer['propertyAddress'],
        propertyListedValue=my_customer['propertyListedValue'],
        sellingMandateEndDate=my_customer['sellingMandateEndDate']
    )
    db.session.add(Customer)
    db.session.commit()

customers = Customer.query.all()

for c in customers:
    print(c.idNumber)

def helper_read_customer(idNumber=None):
    if idNumber:
        return Customer.query.filter(Customer.idNumber == idNumber).first()


@app.route('/')
def hello_world():
    return render_template('login.html')


@app.route('/login')
def login():
    if request.method == "POST":
        return redirect(
            url_for('dashboard')
        )
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('my-dashboard.html')


@app.route('/initiate_contract', methods=['GET', 'POST'])
def initiate_contract():
    userSearchForm = UserSearchForm(request.form)
    if request.method == "POST":
        print(userSearchForm.email.data)
        print(userSearchForm.idNumber.data)

        return redirect(
            url_for('customer_info', idNumber=userSearchForm.idNumber.data)
        )
    return render_template('initiate-contract.html', userSearchForm=userSearchForm)


@app.route('/customer_info', methods=['GET', 'POST'])
@app.route('/customer_info/<idNumber>', defaults={'idNumber': None}, methods=['GET', 'POST'])
def customer_info(idNumber=None):
    idNumber = request.args.get('idNumber')
    if idNumber:
        idNumber = int(idNumber)
    customerInfoForm = CustomerInfo(request.form)

    customer = helper_read_customer(idNumber)

    if customer:
        customerInfoForm.email.default = customer.email
        customerInfoForm.idNumber.default = customer.idNumber
        customerInfoForm.title.default = customer.title
        customerInfoForm.name.default = customer.name
        customerInfoForm.phoneNumber.default = customer.phoneNumber
        customerInfoForm.passportNumber.default = customer.passportNumber
        customerInfoForm.propertyAddress.default = customer.propertyAddress
        customerInfoForm.propertyListedValue.default = customer.propertyListedValue
        customerInfoForm.sellingMandateEndDate.default = customer.sellingMandateEndDate

    if request.method == 'POST':
        return redirect(url_for('sole_mandate'))

    return render_template('customer-info.html', customerInfoForm=customerInfoForm)


@app.route('/contract_templates')
def contract_templates():
    return render_template('contract-templates.html')


@app.route('/sole_mandate')
def sole_mandate():
    return render_template('contract_generic.html')


@app.route('/initiate_contract_from_crm')
def initiate_contract_from_crm():
    return render_template('initiate-contract-from-crm.html')


@app.route('/view_contracts')
def view_contracts():
    return render_template('create_contracts.html')

@app.route('/contract-monitoring')
def contract_monitoring():
    return render_template('contract-monitoring.html')


if __name__ == '__main__':
    app.run()
