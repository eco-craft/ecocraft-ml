from flask import Blueprint, request, jsonify
from controllers.prediction_controller import predict_controller

ml_route = Blueprint("main", __name__)


# prediction route
@ml_route.route("/predict", methods=["POST"])
def predict():
    return predict_controller(request)


@ml_route.route("/", methods=["GET"])
def index():
    return "OK"