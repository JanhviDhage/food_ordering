from flask import Blueprint, redirect, url_for, render_template
import stripe

payment_blueprint = Blueprint('payment', __name__)

stripe.api_key = 'your-stripe-secret-key'

@payment_blueprint.route('/pay')
def process_payment():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': 'Food Order'},
                'unit_amount': 5000,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=url_for('payment.success', _external=True),
        cancel_url=url_for('payment.cancel', _external=True),
    )
    return redirect(session.url)

@payment_blueprint.route('/success')
def success():
    return render_template('success.html')

@payment_blueprint.route('/cancel')
def cancel():
    return render_template('cancel.html')
