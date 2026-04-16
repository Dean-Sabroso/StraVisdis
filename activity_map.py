import os
import gzip
import gpxpy
import folium
import warnings

warnings.filterwarnings('ignore')

# Your GPX activities folder
activities_dir = r"C:\StravaPy\strava_py\activities\activities"
output_path = r'C:\StravaPy\strava_interactive_map.html'

print("Scanning for GPX files and building interactive map...")

try:
    route_files = [f for f in os.listdir(activities_dir) if f.lower().endswith('.gpx') or f.lower().endswith('.gpx.gz')]
except FileNotFoundError:
    print(f"\n[!] Error: Could not find folder {activities_dir}")
    exit()

# Create the base map (Using a clean, light-themed map background)
m = folium.Map(location=[20.0, 0.0], zoom_start=2, tiles="CartoDB positron")

plotted_count = 0

for filename in route_files:
    filepath = os.path.join(activities_dir, filename)
    try:
        # Decompress on the fly if needed
        if filename.lower().endswith('.gz'):
            with gzip.open(filepath, 'rt', encoding='utf-8') as f:
                gpx = gpxpy.parse(f)
        else:
            with open(filepath, 'r', encoding='utf-8') as f:
                gpx = gpxpy.parse(f)

        # Extract coordinates (Folium needs them as Latitude, Longitude)
        route_coordinates = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    route_coordinates.append((point.latitude, point.longitude))

        # Plot the route on the map
        if route_coordinates:
            folium.PolyLine(
                route_coordinates,
                color='#ff4b00',  # Strava Orange
                weight=2.5,
                opacity=0.8
            ).add_to(m)
            plotted_count += 1
            print('.', end='', flush=True)

    except Exception as e:
        pass

if plotted_count > 0:
    # Save as an interactive HTML file
    m.save(output_path)
    print(f"\n\nSuccess! Interactive map created with {plotted_count} tracks.")
    print(f"Go to your folder and double-click to open: {output_path}")
else:
    print("\n\nFailed. No valid tracks were found to plot.")