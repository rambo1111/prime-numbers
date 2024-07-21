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

// Function to print prime numbers indefinitely to the page
function printPrimes() {
    let i = parseInt(localStorage.getItem('lastPrime')) || 0; // Get last printed prime or start from 0
    const primeList = document.getElementById('prime-numbers');

    setInterval(function() {
        if (isPrime(i)) {
            const primeItem = document.createElement('p');
            primeItem.textContent = i;
            primeList.appendChild(primeItem);
            localStorage.setItem('lastPrime', i); // Store the last printed prime
        }
        i++;
    }, 100); // Adjust interval (milliseconds) for performance
}

// Call the function to start printing prime numbers
printPrimes();
