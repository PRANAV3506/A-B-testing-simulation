# A/B Testing Simulation

This project simulates an **A/B test** on e-commerce user journeys to measure:
- Click-Through Rate (CTR)
- Retention Rate
- Revenue impact

## Steps
1. Generate synthetic user data (`generate_data.py`)
2. Run analysis (`analyze_ab_test.py`)
3. View charts in `results/` from `dashboard.py`

## Results
- CTR improvement: ~12% in Variant B
- Retention improvement: ~8% in Variant B
- Statistically significant differences (p < 0.05)

## Tech Stack
- Python, Pandas, NumPy, SciPy, Matplotlib
