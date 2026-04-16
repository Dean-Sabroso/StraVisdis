import os
import gpxpy
import gpxpy.geo
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import contextily as ctx
import numpy as np
import warnings

# Hide unnecessary warnings
warnings.filterwarnings("ignore")

# Define where your GPX files are, and where the images should be saved
activities_dir = r"C:\StravaPy\strava_py\activities\activities"
output_dir = r"C:\StravaPy\Pace_Maps"

# Create the output folder if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

try:
    route_files = [f for f in os.listdir(activities_dir) if f.lower().endswith('.gpx')]
    print(f"Found {len(route_files)} GPX files. Generating custom pace maps...\n")
except FileNotFoundError:
    print(f"Error: Could not find folder {activities_dir}")
    exit()

success_count = 0

# Loop through every GPX file
for filename in route_files:
    gpx_path = os.path.join(activities_dir, filename)
    output_image_path = os.path.join(output_dir, filename.replace('.gpx', '_pace.png'))

    print(f"Processing {filename}...")

    try:
        # 1. Open and parse the GPX data
        with open(gpx_path, 'r', encoding='utf-8') as f:
            gpx = gpxpy.parse(f)

        points = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    # We need time data to calculate speed/pace!
                    if point.time:
                        points.append((point.longitude, point.latitude, point.time))

        if len(points) < 2:
            print(f"  [!] Skipped {filename}: Not enough time data.")
            continue

        segments = []
        paces = []

        # 2. Calculate the Pace for every tiny segment of the route
        for i in range(1, len(points)):
            p1 = points[i - 1]
            p2 = points[i]

            # Calculate distance (meters) and time difference (seconds)
            dist = gpxpy.geo.haversine_distance(p1[1], p1[0], p2[1], p2[0])
            time_diff = (p2[2] - p1[2]).total_seconds()

            if time_diff > 0 and dist > 0:
                speed_m_s = dist / time_diff
                pace_min_km = (1000 / speed_m_s) / 60

                # Filter out crazy GPS glitches (faster than 2 min/km or slower than 15 min/km)
                if 2 < pace_min_km < 15:
                    segments.append([(p1[0], p1[1]), (p2[0], p2[1])])
                    paces.append(pace_min_km)

        if not segments:
            print(f"  [!] Skipped {filename}: Could not calculate valid pace segments.")
            continue

        # 3. Draw the Map
        fig, ax = plt.subplots(figsize=(10, 10))

        # LineCollection maps a color array directly to the line segments
        # 'turbo' is the color gradient: red->yellow->green->blue
        lc = LineCollection(segments, cmap='turbo', linewidth=4, alpha=0.8)
        lc.set_array(np.array(paces))
        ax.add_collection(lc)

        # Set the map borders to fit the activity perfectly
        lons = [p[0] for p in points]
        lats = [p[1] for p in points]
        ax.set_xlim(min(lons), max(lons))
        ax.set_ylim(min(lats), max(lats))

        # 4. Add the Map Background (Streets/Geography)
        ctx.add_basemap(ax, crs="EPSG:4326", source=ctx.providers.CartoDB.Positron)

        # 5. Add Polish to the image
        cbar = fig.colorbar(lc, ax=ax, fraction=0.036, pad=0.04)
        cbar.set_label('Pace (min/km)', fontsize=12)

        ax.set_title(f"Activity Pace - {filename}", fontsize=14)
        ax.axis('off')

        # Save and close memory
        plt.savefig(output_image_path, dpi=300, bbox_inches='tight')
        plt.close(fig)

        success_count += 1
        print(f"  -> Saved {filename.replace('.gpx', '_pace.png')}")

    except Exception as e:
        print(f"  [!] Error processing {filename}: {e}")

print(f"\nFinished! Successfully created {success_count} pace maps.")
print(f"Check the folder: {output_dir}")