# app.py

from flask import Flask, jsonify
import math
from flask_cors import CORS
import threading  # Import threading to run a separate thread for prime number calculation

app = Flask(__name__)
CORS(app)

last_prime = 0
prime_calculation_thread = None  # Initialize a variable to hold the thread object

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, max_divisor + 1, 2):
        if n % d == 0:
            return False
    return True

# Function to continuously calculate prime numbers
def calculate_primes():
    global last_prime
    while True:
        if is_prime(last_prime):
            last_prime += 1
        last_prime += 1

# Start a thread for continuous prime number calculation
def start_prime_calculation():
    global prime_calculation_thread
    prime_calculation_thread = threading.Thread(target=calculate_primes)
    prime_calculation_thread.start()

# Endpoint to fetch the latest prime number
@app.route('/api/latestPrime')
def get_latest_prime():
    global last_prime
    return jsonify({'prime': last_prime})

# Start the prime number calculation thread when the app starts
start_prime_calculation()

if __name__ == '__main__':
    app.run(debug=True)
