from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sqlite3
from pathlib import Path
from datetime import date

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-only-change-me")

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "finsight.db"

CATEGORIES = [
    "Food", "Transport", "Education", "Shopping",
    "Bills", "Entertainment", "Health", "Other"
]


def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount > 0),
                category TEXT NOT NULL,
                transaction_date TEXT NOT NULL,
                type TEXT NOT NULL CHECK(type IN ('income', 'expense'))
            )
        """)


@app.route("/")
def index():
    with get_db() as db:
        transactions = db.execute("""
            SELECT * FROM transactions
            ORDER BY transaction_date DESC, id DESC
        """).fetchall()

        income = db.execute("""
            SELECT COALESCE(SUM(amount), 0)
            FROM transactions
            WHERE type = 'income'
        """).fetchone()[0]

        expenses = db.execute("""
            SELECT COALESCE(SUM(amount), 0)
            FROM transactions
            WHERE type = 'expense'
        """).fetchone()[0]

        category_rows = db.execute("""
            SELECT category, SUM(amount) AS total
            FROM transactions
            WHERE type = 'expense'
            GROUP BY category
            ORDER BY total DESC
        """).fetchall()

        monthly_rows = db.execute("""
            SELECT
                substr(transaction_date, 1, 7) AS month,
                SUM(
                    CASE WHEN type = 'income'
                    THEN amount ELSE 0 END
                ) AS income,
                SUM(
                    CASE WHEN type = 'expense'
                    THEN amount ELSE 0 END
                ) AS expenses
            FROM transactions
            WHERE transaction_date IS NOT NULL
              AND transaction_date != ''
            GROUP BY substr(transaction_date, 1, 7)
            ORDER BY month
        """).fetchall()

    return render_template(
        "index.html",
        transactions=transactions,
        income=income,
        expenses=expenses,
        balance=income - expenses,
        categories=CATEGORIES,
        category_data=[dict(row) for row in category_rows],
        monthly_data=[dict(row) for row in monthly_rows],
        today=date.today().isoformat()
    )


@app.route("/add", methods=["POST"])
def add_transaction():
    title = request.form.get("title", "").strip()
    amount_text = request.form.get("amount", "").strip()
    category = request.form.get("category", "")
    transaction_date = request.form.get("transaction_date", "")
    transaction_type = request.form.get("type", "")

    try:
        amount = float(amount_text)
        valid_date = date.fromisoformat(transaction_date)
    except (ValueError, TypeError):
        flash("Enter a valid amount and date.", "error")
        return redirect(url_for("index"))

    if (
        not title
        or len(title) > 100
        or amount <= 0
        or amount > 1_000_000_000
        or category not in CATEGORIES
        or transaction_type not in ("income", "expense")
        or valid_date.isoformat() != transaction_date
    ):
        flash(
            "Invalid transaction details. Please check your entries.",
            "error"
        )
        return redirect(url_for("index"))

    with get_db() as db:
        db.execute("""
            INSERT INTO transactions
                (title, amount, category, transaction_date, type)
            VALUES (?, ?, ?, ?, ?)
        """, (
            title,
            amount,
            category,
            transaction_date,
            transaction_type
        ))

    flash("Transaction added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete_transaction(transaction_id):
    with get_db() as db:
        db.execute(
            "DELETE FROM transactions WHERE id = ?",
            (transaction_id,)
        )

    flash("Transaction deleted.", "success")
    return redirect(url_for("index"))


init_db()

if __name__ == "__main__":
    app.run(debug=False)
