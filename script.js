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

// Function to update the displayed prime number
function updatePrimeNumber(number) {
    const primeNumberDisplay = document.getElementById('prime-number');
    primeNumberDisplay.textContent = number;
}

// Function to print prime numbers indefinitely and update display
function printPrimes() {
    let i = parseInt(localStorage.getItem('lastPrime')) || 0; // Get last printed prime or start from 0

    const intervalId = setInterval(function() {
        if (isPrime(i)) {
            updatePrimeNumber(i);
            localStorage.setItem('lastPrime', i); // Store the last printed prime
        }
        i++;
    }, 100); // Adjust interval (milliseconds) for performance

    // Save interval ID to localStorage to resume when tab is closed and reopened
    localStorage.setItem('intervalId', intervalId.toString());
}

// Call the function to start printing prime numbers
printPrimes();

// Function to resume printing primes when the tab is reopened
window.onload = function() {
    const intervalId = parseInt(localStorage.getItem('intervalId'));
    if (!isNaN(intervalId)) {
        clearInterval(intervalId); // Clear previous interval if any
        printPrimes(); // Start printing primes again
    }
};
