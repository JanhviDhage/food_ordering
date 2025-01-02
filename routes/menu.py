from flask import render_template, Blueprint
from app.models import MenuItem

menu_bp = Blueprint('menu', __name__)

@menu_bp.route('/menu')
def menu():
    items = MenuItem.query.all()
    return render_template('menu.html', items=items)
