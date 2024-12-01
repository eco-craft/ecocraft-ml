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
    predictions = model.predict(image).flatten()  # Flatten to 1D array if needed
    os.remove(file_path)  # Remove the saved file after prediction

   
    results = {}
    for index, probability in enumerate(predictions):
        if probability > 0.0:  # Check if the probability is greater than 40%
            results[class_labels[index]] = float(probability)  # Store the class and its probability

    # Check if any results were found
    if results:
        return results  # Return all classes that exceed 40% probability
    else:
        return {'error': 'No categories exceed 40% probability.'}  # Return error message