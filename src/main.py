import csv

total_claims = 0
total_amount = 0
invalid_claims = 0

with open("data/claims.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_claims = total_claims + 1

        try:
            claim_amount = float(row["claim_amount"])

            if claim_amount < 0:
                print("Invalid amount:", row["claim_id"])
                invalid_claims = invalid_claims + 1
            else:
                total_amount = total_amount + claim_amount

        except ValueError:
            print("Invalid amount:", row["claim_id"])
            invalid_claims = invalid_claims + 1

print("Total claims:", total_claims)
print("Total billed amount:", total_amount)
print("Invalid claims:", invalid_claims)

