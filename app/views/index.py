from flask import jsonify, Blueprint


index_bp = Blueprint('index', __name__)


@index_bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello, World!"})
