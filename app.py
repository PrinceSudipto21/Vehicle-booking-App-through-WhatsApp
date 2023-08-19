from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!
callers = {
    "+919608607860": "Sudipto",
    "+12349013030": "Finn",
    "+12348134522": "Chewy",
}

@app.route("/", methods=['GET', 'POST'])
def hello():
    """Respond with the number of text messages sent between two parties."""
    # Increment the counter
    counter = session.get('counter', 0)
    counter += 1

    # Save the new counter value in the session
    session['counter'] = counter

    from_number = request.values.get('From')
    if from_number in callers:
        name = callers[from_number]
    else:
        name = "Friend"

    # Build our reply
    SendersMsg = request.form.get('Body')
    print(SendersMsg)
    if '1' in SendersMsg or 'Book' in SendersMsg or 'book' in SendersMsg:
        message = '3. Book through live location\n4. Book through Pincode\n0. Start the conversation again'
    elif '2' in SendersMsg or 'Cancel' in SendersMsg or 'cancel' in SendersMsg:
        message = 'Please provide your booking code.'
    elif '3' in SendersMsg or 'live' in SendersMsg or 'Live' in SendersMsg or 'location' in SendersMsg or 'Location' in SendersMsg:
        message = 'Please provide your live location.'
    elif '4' in SendersMsg or 'pincode' in SendersMsg or 'Pincode' in SendersMsg:
        message = 'Please Enter your pincode.'
    else:
        message = 'Hi {}, this is NammaYatri Customer service bot which will provide you with the services regarding your bookings.\n\nSo, how can I help you?\n1. Book your auto\n2. Cancel your booking\n0. Start the conversation again' \
        .format(name)

    # Put it in a TwiML response
    resp = MessagingResponse()
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)