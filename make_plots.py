# Import the necessary functions from the stravavis package
from stravavis.process_data import process_data
from stravavis.process_activities import process_activities
from stravavis.plot_calendar import plot_calendar
from stravavis.plot_dumbbell import plot_dumbbell
from stravavis.plot_map import plot_map

# THIS IS THE CRUCIAL FIX FOR WINDOWS:
if __name__ == '__main__':
    print("Loading data... this might take a minute.")

    # 1. Load the GPS data
    df = process_data(r"C:\StravaPy\strava_py\activities\activities")

    # 2. Load the CSV metadata
    activities = process_activities(r"C:\StravaPy\strava_py\activities\activities.csv")

    print("Data loaded! Drawing plots...")

    # 3. Create the plots!
    plot_map(df, alpha=0.3, linewidth=0.3, output_file="custom_map.png")

    plot_calendar(activities, year_min=2020, year_max=2024, max_dist=50, fig_height=9, fig_width=15,
                  output_file="custom_calendar.png")

    plot_dumbbell(activities, year_min=2020, year_max=2024, local_timezone='Europe/Helsinki', fig_height=34,
                  fig_width=34, output_file="custom_dumbbell.png")

    print("Done! Check your folder for the new images.")