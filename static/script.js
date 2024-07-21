function updatePrimeNumber(number) {
    document.getElementById('prime-number').textContent = number;
}

async function fetchLatestPrime() {
    try {
        const response = await fetch('/api/latestPrime');
        if (response.ok) {
            const data = await response.json();
            updatePrimeNumber(data.prime);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

setInterval(fetchLatestPrime, 1000);
