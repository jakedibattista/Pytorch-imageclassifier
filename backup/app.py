import os
from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the pre-trained model
model = MobileNetV2(weights='imagenet')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uploaded'
    
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'

    if file:
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Process the image
        img = Image.open(filepath)
        img = img.resize((224, 224))  # MobileNetV2 input size
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Make prediction
        predictions = model.predict(img_array)
        results = decode_predictions(predictions, top=3)[0]

        return render_template('result.html', 
                            image_file=file.filename,
                            predictions=results)

if __name__ == '__main__':
    app.run(debug=True) 