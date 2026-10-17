
# Claims-to-Remittance Reconciliation Platform

## Project Overview
This project processes healthcare claims data from a CSV file using Python. It calculates the total number of claims, sums valid claim amounts, and identifies records with invalid amounts.

## Problem Statement
Data can contain missing, incorrectly formatted, or negative claim amounts. These records need to be identified so that inaccurate data does not affect reporting.

## Technologies Used
- Python
- CSV
- Git
- GitHub

## Current Features
- Reads claims from a CSV file.
- Counts the total number of claims.
- Calculates the total of valid claim amounts.
- Identifies invalid and negative claim amounts.

## Project Structure
- `data/` — Input claims data.
- `src/` — Python processing script.
- `sql/` — SQL development.
- `tests/` — Future automated tests.

## How to Run
1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

   `python src/main.py`

## Data Quality Rules
- Claim amounts must be numeric.
- Claim amounts must not be negative.
- Invalid amounts are reported and excluded from the total.

## Future Improvements
- Add automated tests.
- Store processed data in a SQL database.
- Build data transformation workflows.
- Add pipeline orchestration and reporting.
