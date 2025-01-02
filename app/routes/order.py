from flask import request, render_template, Blueprint
from app import db
from app.models import Order

order_bp = Blueprint('order', __name__)

@order_bp.route("/place", methods=["POST"])
def place_order():
    customer_name = request.form.get("customer_name")
    items = request.form.get("items")
    total_price = request.form.get("total_price")
    
    new_order = Order(customer_name=customer_name, items=items, total_price=total_price)
    db.session.add(new_order)
    db.session.commit()

    return render_template("order_success.html", order=new_order)
