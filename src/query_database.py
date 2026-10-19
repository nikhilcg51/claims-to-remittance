
import sqlite3
from pathlib import Path

# Find the main project folder
project_folder = Path(__file__).resolve().parent.parent
database_file = project_folder / "claims.db"

# Connect to the database
connection = sqlite3.connect(database_file)

# Run our first SQL query


result = connection.execute("""
SELECT claim_status, COUNT(*) AS total_claims
FROM claims
GROUP BY claim_status;
""")
missing_amounts = connection.execute("""
SELECT claim_id, patient_id, claim_amount
FROM claims
WHERE claim_amount IS NULL;
""")

missing_rows = missing_amounts.fetchall()

print("\nClaims with missing amounts:")

for row in missing_rows:
    print(row)
    negative_amounts = connection.execute("""
SELECT claim_id, patient_id, claim_amount
FROM claims
WHERE claim_amount < 0;
""")

negative_rows = negative_amounts.fetchall()

print("\nClaims with negative amounts:")

for row in negative_rows:
    print(row)
rows = result.fetchall()

for row in rows:
    print(row[0], ":", row[1])



# Display the result
row = result.fetchone()
print("Total claims:", row[0])

# Close the connection
connection.close()
