from flask import Blueprint, request, redirect, url_for
from app.models import Order, db

order_blueprint = Blueprint('order', __name__)

@order_blueprint.route('/order', methods=['POST'])
def order():
    items = request.form.get('items')
    total_price = request.form.get('total_price')
    new_order = Order(items=items, total_price=total_price)
    db.session.add(new_order)
    db.session.commit()
    return redirect(url_for('payment.process_payment'))
