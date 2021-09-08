from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('my-dashboard.html')


@app.route('/initiate_contract')
def initiate_contract():
    return render_template('initiate-contract.html')


@app.route('/customer_info')
def customer_info():
    return render_template('customer-info.html')


@app.route('/contract_templates')
def contract_templates():
    return render_template('contract-templates.html')


@app.route('/sole_mandate')
def sole_mandate():
    return render_template('sole-mandate.html')


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
