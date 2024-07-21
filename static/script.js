// static/script.js

// Function to update the displayed prime number
function updatePrimeNumber(number) {
    const primeNumberDisplay = document.getElementById('prime-number');
    primeNumberDisplay.textContent = number;
}

// Function to fetch the latest prime number from backend
async function fetchLatestPrime() {
    try {
        const response = await fetch('/api/latestPrime'); // Adjust URL as per your deployment
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        updatePrimeNumber(data.prime);
    } catch (error) {
        console.error('Error fetching latest prime:', error.message);
    }
}

// Function to continuously fetch and display prime numbers
function continuousFetch() {
    setInterval(fetchLatestPrime, 1000); // Adjust interval as needed
}

// Call the function to start fetching prime numbers
continuousFetch();
