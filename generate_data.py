import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of users
n_users = 10000

# Simulate user IDs
user_ids = np.arange(1, n_users + 1)

# Assign groups (A or B)
groups = np.random.choice(['A', 'B'], size=n_users, p=[0.5, 0.5])

# Simulate Click-Through Rate (CTR)
# Assume variant B performs ~12% better
ctr_A = np.random.binomial(1, 0.25, size=n_users)  # 25% CTR baseline
ctr_B = np.random.binomial(1, 0.28, size=n_users)  # 28% CTR

ctr = [ctr_A[i] if groups[i] == 'A' else ctr_B[i] for i in range(n_users)]

# Simulate Retention (7-day)
# Assume variant B retains ~8% more
ret_A = np.random.binomial(1, 0.45, size=n_users)  # 45%
ret_B = np.random.binomial(1, 0.49, size=n_users)  # 49%

retention = [ret_A[i] if groups[i] == 'A' else ret_B[i] for i in range(n_users)]

# Combine into dataframe
df = pd.DataFrame({
    "user_id": user_ids,
    "group": groups,
    "clicked": ctr,
    "retained": retention
})

# Save CSV
df.to_csv("sample_users.csv", index=False)

print("✅ Synthetic data generated: sample_users.csv")
