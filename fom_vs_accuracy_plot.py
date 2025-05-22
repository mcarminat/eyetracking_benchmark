import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename, color):
    df = pd.read_csv(filename, sep='\t')
    print(df)
    df['Color'] = color
    return df

# Load both datasets with their respective colors
df_commercial = load_data("commercial_fom_data.csv","#3776ab")
df_literature = load_data("literature_fom_data.csv", "orange")

# Combine
df = pd.concat([df_commercial, df_literature], ignore_index=True)

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_yscale('log')

# Scatter and annotate
for _, row in df.iterrows():
    ax.scatter(row['Accuracy'], row['FoM'], color=row['Color'])
    ax.text(row['Accuracy'], row['FoM'], row['Model'], fontsize=8)

# Labels and grid
ax.set_xlabel("Accuracy [°]")
ax.set_ylabel("FoM")
ax.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.savefig("plot.png", dpi=200)
