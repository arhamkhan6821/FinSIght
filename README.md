# FinSight

## A Personal Finance Dashboard

## About the Project

FinSight is my final project for CS50x 2026. I built it as a way to bring personal financial tracking into one place. The idea behind it is simple: keeping track of income, expenses, and transactions shouldn't have to be complicated. With FinSight, the recorded financial activity can be viewed through a single dashboard, along with charts that make the information easier to understand.

Building this project also gave me an opportunity to bring together different things I learned while working through CS50x, from Python and databases to HTML, CSS, and JavaScript.

## Features

* **Transaction Management:** Add new transactions and delete existing ones when necessary.
* **Financial Summary:** View total income, total expenses, and the resulting balance based on recorded transactions.
* **Cash Flow Chart:** Visualize financial activity over time.
* **Category Breakdown:** Use a doughnut chart to see how transactions are distributed across categories.
* **Data Persistence:** Transaction records are stored in an SQLite database and remain available after refreshing the page, provided the database file is preserved.

## Technologies Used

* **Python and Flask** for the application's server-side logic and web routes.
* **SQLite** for storing transaction records.
* **HTML** for the structure of the dashboard.
* **CSS** for the layout and appearance.
* **JavaScript** for client-side interactions and chart functionality.

## Project Files

* `app.py` — Contains the Flask application, routes, database operations, and financial calculations.
* `templates/index.html` — Contains the HTML template for the dashboard.
* `static/style.css` — Defines the dashboard's styling and layout.
* `static/script.js` — Handles client-side interactions and chart-related functionality.
* The SQLite database is created automatically on first run. The local database file is excluded from this repository to protect private transaction data.
* `README.md` — Provides information about the project and instructions for running it.

## How to Run

Python 3 and Flask are required to run the application.

1. Open a terminal in the project directory.

2. Install Flask if it isn't already installed:

   `pip install Flask`

3. Start the application:

   `python app.py`

4. Open the local URL displayed in the terminal, usually `http://127.0.0.1:5000`. When using GitHub Codespaces, open the forwarded port instead.

The terminal must remain active while the development server is running. If the server stops, it can be started again by running `python app.py` from the project directory.

## Testing

I tested the main features by adding transactions, deleting entries, checking whether the financial totals and charts updated, and refreshing the dashboard to make sure the saved records were still available.

## What I Learned

Honestly, one of the toughest parts of my CS50 journey was debugging, especially during the Finance problem. I spent more than 13 hours trying to figure out what was wrong with my code. There were moments when I felt completely frustrated and demotivated, especially when I fixed one error only to run into another. At times, I genuinely wondered if I would be able to get through it. But I kept coming back, trying different solutions and figuring things out one step at a time. Finally getting it to work felt like a huge relief. That experience taught me that programming isn't just about knowing how to write code; it's also about having the patience to struggle with a problem without giving up. Building FinSight gave me another chance to put that lesson into practice, and it made me appreciate how much I can learn by sticking with something even when it gets difficult.

## Demonstration Video

**Demonstration video:** https://youtu.be/LHo2RDJqHdY

## Acknowledgements

This project was developed as part of CS50x 2026. Any external resources and AI assistance used during development will be acknowledged in accordance with the course's academic honesty requirements.
