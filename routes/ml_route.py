from flask import Blueprint, request, jsonify
from controllers.prediction_controller import predict_controller

ml_route = Blueprint("main", __name__)


# prediction route
@ml_route.route("/", methods=["POST","GET"])
def prediction():
    if request.method == "POST":
        return predict_controller(request)
    return "OK"