import os

activities_dir = r"C:\StravaPy\strava_py\activities"
print("Checking exactly what files are in this folder...")

try:
    files = os.listdir(activities_dir)
    # Filter out our python scripts and the main CSV file
    activity_files = [f for f in files if not f.endswith('.py') and not f.endswith('.csv')]

    print(f"\nTotal activity files found: {len(activity_files)}")
    print("Here are the first 10 files so we can see the exact format:")
    print("-" * 40)
    for f in activity_files[:10]:
        print(f)
    print("-" * 40)
except Exception as e:
    print(f"Error reading folder: {e}")