import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ---------------------------
# 1. Generate synthetic data
# ---------------------------
# Example: Support efficiency analysis
# Categories = Support Channels, Value = Resolution Time (in minutes)
np.random.seed(42)

data = {
    "Channel": np.repeat(
        ["Email", "Phone", "Chat", "Self-Service", "On-Site"], 100
    ),
    "ResolutionTime": np.concatenate([
        np.random.normal(60, 10, 100),   # Email
        np.random.normal(30, 5, 100),    # Phone
        np.random.normal(20, 4, 100),    # Chat
        np.random.normal(10, 3, 100),    # Self-Service
        np.random.normal(90, 15, 100),   # On-Site
    ])
}

df = pd.DataFrame(data)

# ---------------------------
# 2. Seaborn Styling
# ---------------------------
sns.set_style("whitegrid")          # professional appearance
sns.set_context("talk")             # larger text for presentation
palette = sns.color_palette("Set2") # clean business-friendly palette

# ---------------------------
# 3. Create Violin Plot
# ---------------------------
plt.figure(figsize=(8, 8))  # 8x8 inches → 512x512 px at dpi=64
sns.violinplot(
    x="Channel",
    y="ResolutionTime",
    data=df,
    palette=palette,
    inner="quartile"
)

# ---------------------------
# 4. Titles and Labels
# ---------------------------
plt.title("Support Efficiency Analysis by Channel", fontsize=16, weight="bold")
plt.xlabel("Support Channel", fontsize=14)
plt.ylabel("Resolution Time (minutes)", fontsize=14)
plt.xticks(rotation=20)

# ---------------------------
# 5. Save Chart
# ---------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")  # exactly 512x512
plt.close()
