from flask import Flask, jsonify, render_template
import math
from flask_cors import CORS
import logging
from threading import Lock

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

last_prime = 2
prime_lock = Lock()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_next_prime():
    global last_prime
    with prime_lock:
        candidate = last_prime + 1
        while not is_prime(candidate):
            candidate += 1
        last_prime = candidate
        logger.info(f"Generated new prime: {last_prime}")
    return last_prime

@app.route('/api/latestPrime')
def get_latest_prime():
    prime = generate_next_prime()
    logger.info(f"Returning prime: {prime}")
    return jsonify({'prime': prime})

@app.route('/')
def index():
    logger.info("Serving index page")
    return render_template('index.html')

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(debug=True)
