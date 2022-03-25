from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
# code business logic

@app.route('/')
def home():
    return render_template('dia.html')

@app.route('/predict', methods=['post'])
def predict():

    #load the model
    model= joblib.load('diabetes_80.pkl')

    preg= request.form.get('preg')
    plasma= request.form.get('plasma')
    pres= request.form.get('pres')
    skin= request.form.get('skin')
    test= request.form.get('test')
    mass= request.form.get('mass')
    pedi= request.form.get('pedi')
    age= request.form.get('age')



    print(preg, plasma, pres, skin, test, mass, pedi, age)
    output = model.predict([[preg, plasma, pres, skin, test, mass, pedi, age]])

    if output[0]==0:
       data= 'the person is not diabetic'
    else:
       data= 'the person is diabetic'




    return render_template('predict.html', data=data)



if __name__ == "main":
    app.run(debug=True)

