from flask import Flask, render_template
# from flask_sqlalchemy import SQLAchemy
from routes.menu import menu_bp
from routes.order import order_bp
from routes.payment import payment_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# Register Blueprints
app.register_blueprint(menu_bp, url_prefix='/menu')
app.register_blueprint(order_bp, url_prefix='/order')
app.register_blueprint(payment_bp, url_prefix='/payment')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
