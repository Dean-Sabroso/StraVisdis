import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# This hides that annoying "Could not infer format" datetime warning
warnings.filterwarnings('ignore', category=UserWarning, module='pandas')

print("Loading Strava activities data...")

# 1. Load your CSV file
df = pd.read_csv(r"C:\StravaPy\strava_py\activities\activities.csv")

# 2. Convert the 'Activity Date' column to actual datetime formats
date_col = [col for col in df.columns if 'Date' in col][0]
df[date_col] = pd.to_datetime(df[date_col])

# 3. Extract the Year, Month, and Week into their own columns
df['Year'] = df[date_col].dt.year
# Get the month abbreviation (Jan, Feb, etc.) and sort them
df['Month'] = df[date_col].dt.strftime('%b')
months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)
# Get the week of the year (1-52)
df['Week'] = df[date_col].dt.isocalendar().week

# Set the visual style for the charts
sns.set_theme(style="whitegrid")

print("Drawing Activities by Year...")
# --- PLOT 1: ACTIVITIES BY YEAR ---
plt.figure(figsize=(10, 6))
# FIXED: Added 'hue' and 'legend=False' to satisfy Seaborn's new rules
sns.countplot(data=df, x='Year', hue='Year', palette='viridis', legend=False)
plt.title('Total Activities by Year', fontsize=16)
plt.ylabel('Number of Activities')
plt.savefig(r'C:\StravaPy\activities_by_year.png', dpi=300, bbox_inches='tight')
plt.close()

print("Drawing Activities by Month...")
# --- PLOT 2: ACTIVITIES BY MONTH ---
plt.figure(figsize=(12, 6))
# FIXED: Added 'hue' and 'legend=False'
sns.countplot(data=df, x='Month', hue='Month', palette='magma', legend=False)
plt.title('Total Activities by Month (All Years)', fontsize=16)
plt.ylabel('Number of Activities')
plt.savefig(r'C:\StravaPy\activities_by_month.png', dpi=300, bbox_inches='tight')
plt.close()

print("Drawing Activities by Week...")
# --- PLOT 3: ACTIVITIES BY WEEK ---
plt.figure(figsize=(15, 6))
# FIXED: Added 'hue' and 'legend=False'
sns.countplot(data=df, x='Week', hue='Week', palette='crest', legend=False)
plt.title('Total Activities by Week of the Year', fontsize=16)
plt.xlabel('Week Number (1-52)')
plt.ylabel('Number of Activities')
plt.savefig(r'C:\StravaPy\activities_by_week.png', dpi=300, bbox_inches='tight')
plt.close()

# FIXED: Added the 'r' before the string to tell Python to ignore the \ backslashes!
print(r"Success! Your Year, Month, and Week charts have been saved to C:\StravaPy\strava_py\activities")