import pandas as pd
import matplotlib.pyplot as plt
import joypy

print("Loading Strava activities data...")

# 1. Load your CSV file
df = pd.read_csv(r"C:\StravaPy\strava_py\activities\activities.csv")

# 2. Convert the 'Activity Date' column to actual datetime formats
date_col = [col for col in df.columns if 'Date' in col][0]
df[date_col] = pd.to_datetime(df[date_col])

# 3. Extract the Year and the Day of the Year (1-365)
df['Year'] = df[date_col].dt.year
df['DayOfYear'] = df[date_col].dt.dayofyear

# 4. Filter out years with too few activities (optional, prevents flat lines)
# Only keep years where you had at least 5 activities
activity_counts = df['Year'].value_counts()
valid_years = activity_counts[activity_counts >= 5].index
df = df[df['Year'].isin(valid_years)]

print("Drawing Ridgeline Plot...")

# 5. Create the Ridgeline plot!
# 'by="Year"' creates a new mountain ridge for each year
# 'column="DayOfYear"' distributes the mountains across the 365 days of the year
fig, axes = joypy.joyplot(
    data=df,
    by="Year",
    column="DayOfYear",
    colormap=plt.cm.viridis, # Color theme (you can also try 'plasma' or 'magma')
    figsize=(12, 8),
    title="Strava Activities by Year",
    alpha=0.85, # How transparent the mountains are
    linewidth=1,
    overlap=1.5 # How much the mountains overlap each other
)

# 6. Save the image
output_path = r'C:\StravaPy\activities_by_year_ridges.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print(f"Success! Your Ridgeline plot has been saved to {output_path}")