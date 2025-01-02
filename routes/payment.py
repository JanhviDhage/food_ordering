from flask import Blueprint, render_template, request

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        order_id = request.form['order_id']
        amount = request.form['amount']
        payment_method = request.form['payment_method']

        # Simulate a successful payment
        if payment_method in ['credit_card', 'debit_card', 'UPI']:
            return render_template('success.html', order_id=order_id, amount=amount)
        else:
            return render_template('cancel.html', message="Payment method not supported.")
    
    # Show a mock payment form
    return render_template('payment.html')
