# app.py

from flask import Flask, jsonify, render_template
import math
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


last_prime = 0

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

# Endpoint to fetch the latest prime number
@app.route('/api/latestPrime')
def get_latest_prime():
    global last_prime
    while True:
        if is_prime(last_prime):
            last_prime += 1  # Increment last_prime to find the next prime number
            return jsonify({'prime': last_prime - 1})  # Return the found prime number
        last_prime += 1


# Route to render index.html
@app.route('/')
def index():
    return render_template('index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
