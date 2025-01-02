from flask import render_template, Blueprint

payment_bp = Blueprint('payment', __name__)

@payment_bp.route("/simulate", methods=["GET"])
def simulate_payment():
    return render_template("order_success.html")
