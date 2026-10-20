document.addEventListener("DOMContentLoaded", function () {
    if (typeof Chart === "undefined") {
        console.error("Chart.js has not loaded.");
        return;
    }

    const data = window.chartData || {};

    // YOUR CASH FLOW: Monthly income and expenses
    const monthlyCanvas = document.getElementById("monthlyChart");

    if (monthlyCanvas) {
        const monthly = data.monthlyData || [];
        console.log("Monthly chart data:", monthly);
console.log("Chart data received:", data);

        new Chart(monthlyCanvas, {
            type: "bar",
            data: {
                labels: monthly.map(row => row.month),
                datasets: [
                    {
                        label: "Income",
                        data: monthly.map(row => Number(row.income) || 0),
                        backgroundColor: "#16a34a",
                        borderRadius: 5
                    },
                    {
                        label: "Expenses",
                        data: monthly.map(row => Number(row.expenses) || 0),
                        backgroundColor: "#ef4444",
                        borderRadius: 5
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    }

    // SPENDING BREAKDOWN: Expenses by category
    const categoryCanvas = document.getElementById("categoryChart");

    if (categoryCanvas) {
        const categories = data.categoryData || [];
        const labels = categories.map(row => row.category);
        const values = categories.map(row => Number(row.total) || 0);

        new Chart(categoryCanvas, {
            type: "doughnut",
            data: {
                labels: labels.length ? labels : ["No expenses yet"],
                datasets: [{
                    data: values.length ? values : [1],
                    backgroundColor: [
                        "#6366f1", "#14b8a6", "#f59e0b",
                        "#ec4899", "#8b5cf6", "#0ea5e9"
                    ],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: "bottom" }
                }
            }
        });
    }
});
