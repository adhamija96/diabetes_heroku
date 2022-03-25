from flask import Flask, render_template, request

app = Flask(__name__)
# code business logic

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['post'])
def predict():
    exp= request.form.get('experience')
    phone= request.form.get('phone')
    mail= request.form.get('email')

    print(exp)
    print(phone)
    print(mail)

    return "got the values.... Thank you"




app.run(debug=True)

