from flask import Flask, render_template, request, url_for
import pickle
import pandas as pandas
import numpy as np

app = Flask(__name__)

# Load the pickled KNN model
model = pickle.load(open("/home/mdpraz2/mysite/knn.pkl","rb"))

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    feature = [np.array(float_features)]
    prediction = model.predict(feature)
    if prediction[0] == 0:
        prediction = 'Besok cuaca akan cerah'
        image_filename = 'sun_image.png'
        comment = 'Sebaiknya anda memakai sunblock.'
    else :
        prediction = 'Besok cuaca akan hujan'
        image_filename = 'rain_image.png'
        comment = 'Sebaiknya anda membawa payung.'
    
    image_path = url_for('static', filename='images/' + image_filename)

    return render_template('index.html', RainTomorrow = "{}".format(prediction), image_path=image_path, comment=comment)

if __name__ == "__main__":
    # Fit the scaler on sample data
    app.run(debug=True)
