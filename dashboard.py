import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sample_users.csv")

# CTR Plot
ctr_summary = df.groupby("group")["clicked"].mean()
ctr_summary.plot(kind="bar", title="Click-Through Rate (CTR)", rot=0)
plt.ylabel("CTR")
plt.savefig("results/ctr_comparison.png")
plt.close()

# Retention Plot
ret_summary = df.groupby("group")["retained"].mean()
ret_summary.plot(kind="bar", title="Retention Rate", rot=0)
plt.ylabel("Retention")
plt.savefig("results/retention_comparison.png")
plt.close()

print("✅ Dashboard charts saved in results/")
