from flask import Flask, jsonify, render_template
import math
from flask_cors import CORS
import threading
import time

app = Flask(__name__)
CORS(app)

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
        time.sleep(0.1)  # Adjust this value to control the speed of generation

@app.route('/api/latestPrime')
def get_latest_prime():
    with prime_lock:
        return jsonify({'prime': last_prime - 1})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    prime_thread = threading.Thread(target=generate_primes, daemon=True)
    prime_thread.start()
    app.run(debug=True, use_reloader=False)