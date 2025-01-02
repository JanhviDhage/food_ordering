from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import menu_bp, order_bp, payment_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Register Blueprints
app.register_blueprint(menu_bp, url_prefix='/menu')
app.register_blueprint(order_bp, url_prefix='/order')
app.register_blueprint(payment_bp, url_prefix='/payment')

if __name__ == "__main__":
    app.run(debug=True)
