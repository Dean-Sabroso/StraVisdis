import pandas as pd
import matplotlib.pyplot as plt
import circlify
import warnings

# Hide pandas formatting warnings
warnings.filterwarnings('ignore', category=UserWarning, module='pandas')

print("Loading Strava activities data...")
df = pd.read_csv(r"C:\StravaPy\strava_py\activities\activities.csv")

# Dynamically find the Date, Distance, and Type columns
date_col = [col for col in df.columns if 'Date' in col][0]
dist_col = [col for col in df.columns if 'Distance' in col][0]
type_col = [col for col in df.columns if 'Type' in col][0]

# Clean up data
df[date_col] = pd.to_datetime(df[date_col])
df['Year'] = df[date_col].dt.year
df = df[df[dist_col] > 0]  # Remove activities with 0 distance

print("Calculating circle sizes...")
agg_df = df.groupby([type_col, 'Year'])[dist_col].sum().reset_index()

# Define some beautiful, distinct colors for different activities
activity_colors = {
    'Run': '#fc4c02',  # Strava Orange
    'Ride': '#1e90ff',  # Dodger Blue
    'Walk': '#2ecc71',  # Emerald Green
    'Workout': '#9b59b6',  # Amethyst Purple
    'Swim': '#00ced1',  # Turquoise
    'Hike': '#e67e22',  # Earthy Orange
    'Yoga': '#e84393'  # Pink
}
default_color = '#7f8c8d'  # Gray for anything else

# Format the data for 'circlify' and pass the parent activity name to the children
hierarchy_data = []
for act_type in agg_df[type_col].unique():
    type_data = agg_df[agg_df[type_col] == act_type]
    children = []
    for _, row in type_data.iterrows():
        # Inner circles: Year and Distance. We also save 'parent_id' so we know what color to make it!
        children.append({
            'id': str(row['Year']),
            'datum': row[dist_col],
            'parent_id': act_type
        })
    # Outer circles: Activity Type and Total Distance
    hierarchy_data.append({'id': act_type, 'datum': type_data[dist_col].sum(), 'children': children})

# Compute the layout for the packed circles
circles = circlify.circlify(hierarchy_data, show_enclosure=False, target_enclosure=circlify.Circle(x=0, y=0, r=1))

print("Drawing Enhanced Packed Circles plot...")
fig, ax = plt.subplots(figsize=(14, 14), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')
ax.axis('off')

# Set the limits of the plot based on the generated circles
lim = max(max(abs(circle.x) + circle.r, abs(circle.y) + circle.r) for circle in circles)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

# Draw the circles
for circle in circles:
    if circle.level == 1:
        # --- OUTER CIRCLES (Activity Types) ---
        act_type = circle.ex["id"]
        base_color = activity_colors.get(act_type, default_color)

        # Draw a light background circle with a colored border
        circle_patch = plt.Circle((circle.x, circle.y), circle.r, alpha=0.1, color=base_color)
        border_patch = plt.Circle((circle.x, circle.y), circle.r, fill=False, edgecolor=base_color, linewidth=2,
                                  alpha=0.5)
        ax.add_patch(circle_patch)
        ax.add_patch(border_patch)

        # Label the Activity Type (Only if the circle is large enough)
        if circle.r > 0.15:
            plt.text(circle.x, circle.y + circle.r - 0.06, act_type.upper(),
                     ha='center', va='top', fontsize=16, fontweight='black', color=base_color, alpha=0.8)

    elif circle.level == 2:
        # --- INNER CIRCLES (Years & Distances) ---
        act_type = circle.ex.get("parent_id", "Unknown")
        base_color = activity_colors.get(act_type, default_color)

        # Draw the solid inner circle
        circle_patch = plt.Circle((circle.x, circle.y), circle.r, alpha=0.85, edgecolor="white", linewidth=1.5,
                                  color=base_color)
        ax.add_patch(circle_patch)

        # Smart Text Labels: Only draw text if the circle is big enough to fit it!
        if circle.r > 0.08:
            year_text = circle.ex["id"]
            dist_val = int(circle.ex["datum"])

            # Dynamically scale font size based on circle radius
            font_size = max(9, min(14, int(circle.r * 60)))

            # Print Year
            plt.text(circle.x, circle.y + 0.02, year_text,
                     ha='center', va='bottom', fontsize=font_size, color="white", fontweight='bold')
            # Print Distance
            plt.text(circle.x, circle.y - 0.02, f"{dist_val:,} km",
                     ha='center', va='top', fontsize=font_size - 2, color="white", fontweight='medium')

# Add a much cleaner, professional title
plt.suptitle("Strava Activity Footprint", fontsize=26, fontweight='black', color='#2c3e50', y=0.95)
plt.title("Total distance grouped by Activity Type and Year", fontsize=16, color='#7f8c8d', pad=20)

# Save the image
output_path = r'C:\StravaPy\packed_circles_enhanced.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()

print(f"Success! Your Enhanced Packed Circles chart has been saved to {output_path}")