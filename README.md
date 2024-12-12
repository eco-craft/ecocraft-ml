# EcoCraft Machine Learning

Welcome to the EcoCraft Machine Learning! This project leverages machine learning to classify different types of waste based on images uploaded by users. The system utilizes a pre-trained model to predict the category of waste and provide probabilities for each class.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)


## Features

- Upload images of waste for classification.
- Predictions with probabilities for each category.
- Handles various waste types including glass bottles, plastic bottles, forks, and more.
- Simple and intuitive API for easy integration.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **TensorFlow**: An open-source machine learning library for building and training models.
- **PIL (Pillow)**: A Python Imaging Library used for opening, manipulating, and saving image files.
- **NumPy**: A fundamental package for scientific computing in Python.

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   
   git clone https://github.com/eco-craft/ecocraft-ml.git

2. Install the required packages:
   ```bash
   
   pip install -r requirements.txt

## Usage

To run the Flask application, use the following command:

```bash
flask run
```
The application will run at http://127.0.0.1:5000/ by default.


## API Documentation

### Predict
- **Endpoint:** `/predict`
- **Method:** `POST`
- **Description:** Accepts an image file for making predictions.

#### Request:
The request should include an image file in `multipart/form-data`.

**Example with cURL:**
```bash
curl -X POST -F "file=@image.jpg" http://127.0.0.1:5000/predict
```

#### Response:
The response will be a JSON object containing the prediction result.

**Example Response:**
```json
{
    "prediction": "result_value"
}
```


### Health Check
- **Endpoint:** `/`
- **Method:** `GET`
- **Description:** Checks if the API is operational.

#### Response:
```text
OK
```















