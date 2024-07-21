from flask import Flask, jsonify, render_template
import math
from flask_cors import CORS
import threading
import time
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

last_prime = 2
prime_lock = threading.Lock()

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(math.sqrt(n)) + 1))

def generate_primes():
    global last_prime
    while True:
        with prime_lock:
            while not is_prime(last_prime):
                last_prime += 1
            last_prime += 1
            logger.info(f"Generated new prime: {last_prime - 1}")
        time.sleep(0)  # Adjust this value to control the speed of generation

@app.route('/api/latestPrime')
def get_latest_prime():
    with prime_lock:
        prime = last_prime - 1
    logger.info(f"Returning prime: {prime}")
    return jsonify({'prime': prime})

@app.route('/')
def index():
    logger.info("Serving index page")
    return render_template('index.html')

if __name__ == '__main__':
    logger.info("Starting prime generation thread")
    prime_thread = threading.Thread(target=generate_primes, daemon=True)
    prime_thread.start()
    logger.info("Starting Flask application")
    app.run(debug=True, use_reloader=False)
