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
    let i = 0;
    const primeList = document.getElementById('prime-numbers');

    setInterval(function() {
        if (isPrime(i)) {
            const primeItem = document.createElement('p');
            primeItem.textContent = i;
            primeList.appendChild(primeItem);
        }
        i++;
    }, 100); // Adjust interval (milliseconds) for performance
}

// Call the function to start printing prime numbers
printPrimes();
