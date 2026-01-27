let myChart;

async function analyzeSentiment() {
    const text = document.getElementById('reviewInput').value;
    if (!text) return alert("Please enter a review");

    const response = await fetch('/analyze', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({review: text})
    });

    const data = await response.json();
    
    document.getElementById('results').classList.remove('hidden');
    document.getElementById('statusText').innerText = data.label;
    
    updateChart(data.scores);
}

function updateChart(scores) {
    const ctx = document.getElementById('sentimentChart').getContext('2d');
    if (myChart) myChart.destroy();
    
    myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Positive', 'Neutral', 'Negative'],
            datasets: [{
                data: [scores.pos, scores.neu, scores.neg],
                backgroundColor: ['#10B981', '#6B7280', '#EF4444']
            }]
        },
        options: { responsive: true }
    });
}