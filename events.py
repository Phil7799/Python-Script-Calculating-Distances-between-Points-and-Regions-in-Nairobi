import pandas as pd
import geopy.distance

# Step 1: Read the Excel data with region polygons and their latitude and longitude columns
excel_file = 'nairobi_jan.xlsx'
excel_data = pd.read_excel(excel_file)

# Step 2: Define the four different points with their longitude and latitude
points = [
    {'latitude': -1.278967, 'longitude': 36.770486}, #-1.278967,36.770486 #2000
    {'latitude': -1.278967, 'longitude': 36.770486}, #-1.278967,36.770486 #2000
    {'latitude': -1.278967, 'longitude': 36.770486}, #-1.278967,36.770486 #2000
    {'latitude': -1.278967, 'longitude': 36.770486}, #-1.278967,36.770486 #2000
    {'latitude': -1.278967, 'longitude': 36.770486}, #-1.278967,36.770486 #2000
    
]

# Step 3: Calculate distances using Haversine formula for each point
for i, point in enumerate(points):
    def calculate_distance(row):
        coords_1 = (row['latitude'], row['longitude'])  # Updated to use 'latitude' and 'longitude'
        if pd.notna(coords_1[0]) and pd.notna(coords_1[1]):
            coords_2 = (point['latitude'], point['longitude'])
            distance_km = geopy.distance.geodesic(coords_1, coords_2).kilometers
            return distance_km * 1000  # Convert kilometers to meters
        else:
            return None

    column_name = f'distance_point_{i+1}'
    excel_data[column_name] = excel_data.apply(calculate_distance, axis=1)

# Step 4: Export the updated Excel data
output_excel_file = 'nairobi_1.xlsx'
excel_data.to_excel(output_excel_file, index=False)