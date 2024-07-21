const express = require('express');
const app = express();

let lastPrime = 0;

// Function to check if a number is prime
function isPrime(n) {
    if (n <= 1) {
        return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

// Endpoint to fetch the latest prime number
app.get('/api/latestPrime', (req, res) => {
    while (true) {
        if (isPrime(lastPrime)) {
            res.json({ prime: lastPrime });
            lastPrime++;
            break;
        }
        lastPrime++;
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
