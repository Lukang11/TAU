from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data
users = [
    {"id": 1, "email": "test1@test.com", "password": "password1"},
    {"id": 2, "email": "test2@test.com", "password": "password2"}
]

payments = []

# Endpoint for user authentication
@app.route('/api/auth', methods=['POST'])
def authenticate_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    for user in users:
        if user['email'] == email and user['password'] == password:
            # Return success response with access token
            return jsonify({'access_token': 'sample_token', 'expires_in': 3600}), 200
    # Return unauthorized error
    return jsonify({'message': 'Invalid credentials'}), 401

# Endpoint for payment processing
@app.route('/api/payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    access_token = data.get('access_token')
    amount = data.get('amount')
    card_number = data.get('card_number')
    expiry_date = data.get('expiry_date')
    cvv = data.get('cvv')
    # Check if access token is valid
    if access_token != 'sample_token':
        # Return unauthorized error
        return jsonify({'message': 'Invalid access token'}), 401
    # Check if there are sufficient funds in the account
    if amount > 100:
        # Return payment required error
        return jsonify({'message': 'Insufficient funds'}), 402
    # Add payment to list of payments
    payment = {'amount': amount, 'card_number': card_number, 'expiry_date': expiry_date, 'cvv': cvv}
    payments.append(payment)
    # Return success response with transaction details
    return jsonify({'message': 'Payment processed successfully', 'transaction': payment}), 200

# Endpoint for retrieving payment history
@app.route('/api/payments', methods=['GET'])
def get_payment_history():
    access_token = request.args.get('access_token')
    # Check if access token is valid
    if access_token != 'sample_token':
        # Return unauthorized error
        return jsonify({'message': 'Invalid access token'}), 401
    # Return list of payments
    return jsonify({'payments': payments}), 200

# Endpoint for retrieving user account details
@app.route('/api/user', methods=['GET'])
def get_user_details():
    access_token = request.args.get('access_token')
    # Check if access token is valid
    if access_token != 'sample_token':
        # Return unauthorized error
        return jsonify({'message': 'Invalid access token'}), 401
    # Return user details
    user = users[0] # For demo purposes, returning first user from the list
    return jsonify({'user': user}), 200

# Endpoint for changing user password
@app.route('/api/user/password', methods=['PUT'])
def change_user_password():
    data = request.get_json()
    access_token = data.get('access_token')
    current_password = data.get('current_password')
    new_password = data.get('new_password')
    # Check if access token is valid and current password matches
    if access_token != 'sample_token' or users[0]['password'] != current_password:
        # Return unauthorized error
        return jsonify({'message': 'Invalid access token or password'}), 
