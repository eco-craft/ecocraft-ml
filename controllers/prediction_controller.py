from flask import request, jsonify
from services.ml_service import make_prediction


class_labels = ['Bohlam', 'Botol Plastik', 'Garpu', 'Gelas Plastik', 'Hanger', 'Kain', 'Kaleng', 'Kardus', 'Kertas', 'Kotak Susu', 'Sendok', 'Tutup Botol']


def predict_controller(request):
    # Validate the request
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    try:
        # Delegate to the service layer
        predictions = make_prediction(file , class_labels)
        return jsonify({"predictions": predictions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500