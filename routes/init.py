from flask import Blueprint
menu_bp = Blueprint('menu', __name__)
order_bp = Blueprint('order', __name__)
payment_bp = Blueprint('payment', __name__)

from . import menu, order, payment
