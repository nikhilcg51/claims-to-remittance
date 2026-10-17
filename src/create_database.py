
import csv
import sqlite3
from pathlib import Path

# Find the main project folder
project_folder = Path(__file__).resolve().parent.parent

# Set the locations of the CSV file and database
csv_file = project_folder / "data" / "claims.csv"
database_file = project_folder / "claims.db"

# Connect to the database (creates it if it doesn't exist)
connection = sqlite3.connect(database_file)

# Create a table to store the claims
connection.execute("""
CREATE TABLE IF NOT EXISTS claims (
    claim_id TEXT,
    patient_id TEXT,
    claim_amount REAL,
    claim_status TEXT
)
""")
connection.execute("DELETE FROM claims")

# Read the CSV and load the claims into the table
with open(csv_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            amount = float(row["claim_amount"])

            if amount < 0:
                amount = None

        except (ValueError, TypeError):
            amount = None

        connection.execute(
            """
            INSERT INTO claims
            (claim_id, patient_id, claim_amount, claim_status)
            VALUES (?, ?, ?, ?)
            """,
            (
                row["claim_id"],
                row["patient_id"],
                amount,
                row["claim_status"]
            )
        )

# Save the changes and close the database
connection.commit()
connection.close()

print("Claims database created successfully!")
