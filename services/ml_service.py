import os
import numpy as np
import tensorflow as tf
from PIL import Image

MODEL_PATH = "model/waste_detector.h5"
model = tf.keras.models.load_model(MODEL_PATH)


def prepare_image(file_path, target_size=(128, 128)):

    image = Image.open(file_path)
    image_resized = image.resize((128, 128))
    image_array = np.array(image_resized) / 255.0
    image_input = np.expand_dims(image_array, axis=0)
    return image_input




def make_prediction(file, class_labels):
    # Save the uploaded file
    file_path = os.path.join(file.filename)  
    file.save(file_path)

    # Prepare the image for prediction
    image = prepare_image(file_path)
    predictions = model.predict(image).flatten()  
    os.remove(file_path)  

   
    results = {}
    for index, probability in enumerate(predictions):
        if probability > 0.40 : 
            results[class_labels[index]] = float(probability)

 
    if results:
        return results
    else:
        return {'error': 'No categories exceed 40% probability.'} 