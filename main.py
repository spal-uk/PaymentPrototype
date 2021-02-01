from flask import Flask, render_template, url_for, flash, redirect, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from APPLICATION.forms import PaymentForm
from APPLICATION.invalidAbort import dataAbort

base = "http://127.0.0.1:5000/"
app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'd1d0f00f285cbc3a5837b6abb385b8e0'

def paymentGateway(Amount):
    Amount = int(Amount)
    if Amount <= 20:
        return f"Paid: {Amount} though Gateway: CheapPaymentGateway"
    elif 21 <= Amount <= 500:
        tries = 1
        for i in range(tries):
            try:
                return f"Paid: {Amount} though Gateway: ExpensivePaymentGateway"
            except KeyError as e:
                if i < tries - 1:  # i is zero indexed
                    continue
                else:
                    raise
            break
    else:
        tries = 3
        for i in range(tries):
            try:
                return f"Paid: {Amount} though Gateway: PremiumPaymentGateway"
            except KeyError as e:
                if i < tries - 1:  # i is zero indexed
                    continue
                else:
                    raise
            break



class Payment(Resource):
    def get(self, CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount):
        dataAbort(CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount)
        return paymentGateway(Amount)


class PaymentTest(Resource):
    def get(self, CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount):
        dataAbort(CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount)
        print(paymentGateway(Amount))
        return 200

api.add_resource(PaymentTest,
                 "/ProcessPayment/<string:CreditCardNumber>/<string:CardHolder>/<string:ExpirationDate>/<string:SecurityCode>/<float:Amount>")


@app.route("/")

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/login")
def login():
    return render_template('underDevelopment.html', title='Login')

@app.route("/register")
def register():
    return render_template('underDevelopment.html', title='Register')

@app.route("/pay", methods=['GET', 'POST'])
def pay():
    form = PaymentForm()
    if form.validate_on_submit():
        response = Payment.get("ProcessPayment", form.creditCardNumber.data, form.cardHolder.data,
                               form.expirationDate.data, form.securityCode.data, form.amount.data)
        flash(response,'success')
        return redirect(url_for('pay'))
    return render_template('payment.html' , title ='Payment', form = form)


@app.errorhandler(400)
def custom400(error):
    flash(error.description,'danger')
    return redirect(url_for('pay'))

if __name__ == "__main__":
    app.run(debug=True)
