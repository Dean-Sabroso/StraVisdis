import pandas as pd
import matplotlib.pyplot as plt
import circlify
import warnings
import math
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# Hide warnings for clean console output
warnings.filterwarnings('ignore')

print("Loading Strava activities data...")
# 1. Load your CSV file
df = pd.read_csv(r"C:\StravaPy\strava_py\activities\activities.csv")

# 2. Find the necessary columns safely
date_col = next((col for col in df.columns if 'Date' in col), 'Activity Date')
dist_col = next((col for col in df.columns if 'Distance' in col), 'Distance')
time_col = next((col for col in df.columns if 'Moving Time' in col or 'Time' in col), 'Moving Time')
type_col = next((col for col in df.columns if 'Type' in col), 'Activity Type')

# Convert Dates and Extract Year
df[date_col] = pd.to_datetime(df[date_col])
df['Year'] = df[date_col].dt.year

# 3. Filter data: We only want Runs with valid distance and time
df = df[df[type_col].astype(str).str.contains('Run', case=False, na=False)]
df = df[(df[dist_col] > 0) & (df[time_col] > 0)]

print("Calculating speeds and filtering data...")
# 4. Standardize Distance (km) and Calculate Speed (km/h)
if df[dist_col].mean() > 100:
    df['Distance_km'] = df[dist_col] / 1000
else:
    df['Distance_km'] = df[dist_col]

df['Speed_kmh'] = df['Distance_km'] / (df[time_col] / 3600)

# Filter out glitchy GPS data
df = df[(df['Speed_kmh'] > 2) & (df['Speed_kmh'] < 25)]

print("Packing circles for each year (this might take a few seconds)...")

# 5. Set up the visual grid
years = sorted(df['Year'].unique())
num_years = len(years)

cols = min(3, num_years)
rows = math.ceil(num_years / cols)

# ENHANCEMENT: Slightly larger figure with a clean, premium off-white background
fig, axes = plt.subplots(rows, cols, figsize=(cols * 5, rows * 5), facecolor='#f8f9fa')

if num_years > 1:
    axes = axes.flatten()
else:
    axes = [axes]

# 6. Set up the Colormap
cmap = plt.cm.plasma
norm = Normalize(vmin=df['Speed_kmh'].min(), vmax=df['Speed_kmh'].max())

# 7. Draw the clusters year by year
for i, year in enumerate(years):
    ax = axes[i]
    ax.set_facecolor('#f8f9fa')  # Match background
    year_data = df[df['Year'] == year]

    data = [{'id': str(idx), 'datum': row['Distance_km'], 'speed': row['Speed_kmh']}
            for idx, row in year_data.iterrows()]

    circles = circlify.circlify(data, show_enclosure=False)

    ax.axis('off')
    if not circles:
        continue

    # Scale axes with a little extra padding so labels fit beautifully
    lim = max(max(abs(c.x) + c.r, abs(c.y) + c.r) for c in circles)
    ax.set_xlim(-lim * 1.05, lim * 1.05)
    ax.set_ylim(-lim * 1.15, lim * 1.05)

    # Draw each individual run
    for circle in circles:
        speed = circle.ex['speed']
        color = cmap(norm(speed))

        # ENHANCEMENT: Crisp white borders instead of hard black lines
        circle_patch = plt.Circle((circle.x, circle.y), circle.r, color=color,
                                  edgecolor='white', linewidth=1.2, alpha=0.95)
        ax.add_patch(circle_patch)

    # ENHANCEMENT: Stylish Year label drawn directly on the axis coordinates
    ax.text(0, -lim * 1.1, str(year), fontsize=22, fontweight='bold', color='#2c3e50', ha='center')

for j in range(i + 1, len(axes)):
    axes[j].axis('off')

# 8. Add the Enhanced Speed Colorbar
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=axes, shrink=0.5, aspect=15, pad=0.05)
cbar.set_label('Average Speed (km/h)', fontsize=14, fontweight='bold', color='#2c3e50', labelpad=15)
cbar.outline.set_visible(False)
cbar.ax.tick_params(labelsize=12, colors='#2c3e50', length=0)  # Clean, tickless look

# 9. ENHANCEMENT: Premium Typography & Layout for Main Titles
fig.text(0.05, 1.05, "Strava Runs: Distance & Speed", fontsize=28, fontweight='black', color='#111111', ha='left')
fig.text(0.05, 1.00, "Circle area represents total distance. Color gradient represents average speed.", fontsize=14,
         color='#555555', ha='left')

# Save and finish
output_path = r'C:\StravaPy\packed_circles_advanced_enhanced.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()

print(f"Success! Your Enhanced Advanced Packed Circles chart has been saved to {output_path}")