
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

rows = result.fetchall()

for row in rows:
    print(row[0], ":", row[1])



# Display the result
row = result.fetchone()
print("Total claims:", row[0])

# Close the connection
connection.close()
