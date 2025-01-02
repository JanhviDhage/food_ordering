from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from menu_routes import menu_bp

from order import order_bp
from payment import payment_bp

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for local development)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_ordering_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(menu_bp, url_prefix='/menu')
app.register_blueprint(order_bp, url_prefix='/order')
app.register_blueprint(payment_bp, url_prefix='/payment')

# Define the homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Initialize database models
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
