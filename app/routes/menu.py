from flask import Blueprint, render_template
from app.models import MenuItem

menu_blueprint = Blueprint('menu', __name__)

@menu_blueprint.route('/menu')
def menu():
    items = MenuItem.query.all()
    return render_template('menu.html', items=items)
