
-- Find the total number of claims
SELECT COUNT(*) AS total_claims
FROM claims;

-- Find claims with missing amounts
SELECT claim_id, patient_id, claim_amount
FROM claims
WHERE claim_amount IS NULL;