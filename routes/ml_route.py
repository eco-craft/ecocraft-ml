from flask import Blueprint, request, jsonify
from controllers.prediction_controller import predict_controller

ml_route = Blueprint("main", __name__)

@ml_route.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return predict_controller(request)
    return "OK"