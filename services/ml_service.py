import gc


import os
import numpy as np
import tensorflow as tf
from PIL import Image
from io import BytesIO

MODEL_PATH = "model/waste_detector.h5"
model = tf.keras.models.load_model(MODEL_PATH)




def prepare_image(file_path, target_size=(224, 224)):
      with Image.open(file_path) as image:
            # Convert grayscale to RGB
            if image.mode != 'RGB':
                  image = image.convert('RGB')

            # Resize 
            image = image.resize(target_size)
            image_array = np.array(image, dtype=np.float32) / 255.0  # Normalize pixel values
            return  np.expand_dims(image_array, axis=0)



def make_prediction(file, class_labels):

            file_content = file.read()
            image = prepare_image(BytesIO(file_content))
            predictions = model.predict(image).flatten()

            del image
            gc.collect()
        
            results = {class_labels[index]: float(prob) for index, prob in enumerate(predictions)}


            if results:
                  best_label = max(results, key=results.get)  
                  best_prob = results[best_label]
                  return {best_label: best_prob}  
            else:
                  return {'error': 'No categories found.'}
                  









