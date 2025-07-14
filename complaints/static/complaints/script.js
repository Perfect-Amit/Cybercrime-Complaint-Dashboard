document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('complaintChart');

    if (ctx) {
        const chart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: complaintData.labels,  // Provided via Django context
                datasets: [{
                    label: 'Number of Complaints',
                    data: complaintData.data,
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                    borderRadius: 4,
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Complaints Count'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Complaint Categories'
                        }
                    }
                }
            }
        });
    }
});
