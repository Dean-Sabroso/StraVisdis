# Import the necessary functions from the stravavis package
from stravavis.process_data import process_data
from stravavis.process_activities import process_activities
from stravavis.plot_calendar import plot_calendar
from stravavis.plot_dumbbell import plot_dumbbell
from stravavis.plot_map import plot_map

print("Loading data... this might take a minute.")

# 1. Load the GPS data (For Maps, Elevations, Landscapes, Facets)
# Notice the 'r' before the quotes—this tells Python to read the Windows folder path exactly as written!
df = process_data(r"C:\StravaPy\strava_py\activities\activities")

# 2. Load the CSV metadata (For Calendar and Dumbbell plots)
activities = process_activities(r"C:\StravaPy\strava_py\activities\activities.csv")

print("Data loaded! Drawing plots...")

# 3. Create the plots!
# You can change the years, timezone, and output file names here.

# Make a map
plot_map(df, alpha=0.3, linewidth=0.3, output_file="custom_map.png")

# Make a Calendar plot
plot_calendar(activities, year_min=2020, year_max=2024, max_dist=50, fig_height=9, fig_width=15, output_file="custom_calendar.png")

# Make a Dumbbell plot (Change the timezone to your local timezone!)
plot_dumbbell(activities, year_min=2020, year_max=2024, local_timezone='Europe/Helsinki', fig_height=34, fig_width=34, output_file="custom_dumbbell.png")

print("Done! Check your folder for the new images.")