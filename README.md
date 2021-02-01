# Flask Web API for payment
## author: S Pal
## linkedin: https://www.linkedin.com/in/pals/

 # how to run the program:
 
 ## step 1: install necessary python packages
 
 ```
 pip install -r requirements.txt
 ```
 
 ## step 2: open first terminal window and use command from same directory 
 
```
python main.py
```
## step 4: open browser and hit the URL
    http://127.0.0.1:5000/pay

## step 5: Submit the Payment form using values like:
    Enter Credit Card Number: 3521226789123444
    Confirm Credit Card Number: 3521226789123444
    Card Holder: Andrew
    Expiration Date (YYYY-MM-DD): 2021-10-23
    Amount: 564.90
    Security Code: 123

## step 6: Alternative Testing: open second terminal and use the following command for running unit tests

```
python TEST/test.py
```

================================================
Coding exercise:
Write a Flask Web API with only 1 method called “ProcessPayment” that receives a request
like this
- CreditCardNumber (mandatory, string, it should be a valid credit card number)
- CardHolder: (mandatory, string)
- ExpirationDate (mandatory, DateTime, it cannot be in the past)
- SecurityCode (optional, string, 3 digits)
- Amount (mandatoy decimal, positive amount)
The response of this method should be 1 of the followings based on
- Payment is processed: 200 OK
- The request is invalid: 400 bad request
- Any error: 500 internal server error
The payment could be processed using different payment providers (external services)
called:
- PremiumPaymentGateway
- ExpensivePaymentGateway
- CheapPaymentGateway.
The payment gateway that should be used to process each payment follows the next set of
business rules:
a) If the amount to be paid is less than £20, use CheapPaymentGateway.
b) If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
Otherwise, retry only once with CheapPaymentGateway.
c) If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times
in case payment does not get processed.
Recommendations:
- The classes should be written in such way that they are easy to test.
- Write as many tests as you think is enough to be certain about your solution works -
Use SOLID principles.
- Decouple the logic the prediction logic from the API as much as possible