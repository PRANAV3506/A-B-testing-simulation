import pandas as pd
import scipy.stats as stats

# Load dataset
df = pd.read_csv("sample_users.csv")

# Summary CTR
ctr_summary = df.groupby("group")["clicked"].mean()
ret_summary = df.groupby("group")["retained"].mean()

print("CTR Summary:")
print(ctr_summary)
print("\nRetention Summary:")
print(ret_summary)

# Hypothesis Testing (Chi-square test)
ctr_table = pd.crosstab(df["group"], df["clicked"])
ret_table = pd.crosstab(df["group"], df["retained"])

chi2_ctr, p_ctr, _, _ = stats.chi2_contingency(ctr_table)
chi2_ret, p_ret, _, _ = stats.chi2_contingency(ret_table)

print("\nHypothesis Testing:")
print(f"CTR Difference p-value: {p_ctr:.4f}")
print(f"Retention Difference p-value: {p_ret:.4f}")

# Save results
with open("results/summary_report.md", "w") as f:
    f.write("## A/B Testing Results\n\n")
    f.write(f"CTR A: {ctr_summary['A']:.3f}, CTR B: {ctr_summary['B']:.3f}\n")
    f.write(f"Retention A: {ret_summary['A']:.3f}, Retention B: {ret_summary['B']:.3f}\n\n")
    f.write(f"CTR p-value: {p_ctr:.4f}\n")
    f.write(f"Retention p-value: {p_ret:.4f}\n")

print("✅ Analysis complete. Results saved in results/summary_report.md")
