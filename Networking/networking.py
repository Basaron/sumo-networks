import xml.etree.ElementTree as ET
import folium
import random

osm_file = 'C:/Users/basti\Desktop/3Sem/StudieCourse/Networking/map.osm'  # Replace with your file path

# Function to parse the OSM file and extract street lamps
def extract_street_lamps(osm_file):
    tree = ET.parse(osm_file)
    root = tree.getroot()
    street_lamps = []

    for node in root.findall('node'):
        for tag in node.findall('tag'):
            if tag.get('k') == 'highway' and tag.get('v') == 'street_lamp':
                lat = float(node.get('lat'))
                lon = float(node.get('lon'))
                street_lamps.append((lat, lon))

    return street_lamps

street_lamps = extract_street_lamps(osm_file)
#print(street_lamps)


# Function to calculate the center of the street lamps
def calculate_center(street_lamps):
    if not street_lamps:
        return None, None

    sum_lat = sum(lamp[0] for lamp in street_lamps)
    sum_lon = sum(lamp[1] for lamp in street_lamps)
    num_lamps = len(street_lamps)

    return sum_lat / num_lamps, sum_lon / num_lamps

center_lat, center_lon = calculate_center(street_lamps)
print(f"Center Latitude: {center_lat}, Center Longitude: {center_lon}")


# Create a map object
m = folium.Map(location=[center_lat, center_lon], zoom_start=15)  # Replace latitude, longitude with your map's central point

# Add street lamps to the map
for lamp in street_lamps:
    folium.Marker([float(lamp[0]), float(lamp[1])], popup='Street Lamp').add_to(m)

# Save the map to an HTML file
m.save('C:/Users/basti/Desktop/3Sem/StudieCourse/Networking/street_lamps_map.html')

# Update Folium marker code to include on/off status
for lamp in street_lamps:
    status = 'On' if random.choice([True, False]) else 'Off'
    icon_color = 'green' if status == 'On' else 'red'
    folium.Marker(
        [float(lamp[0]), float(lamp[1])], 
        popup=f'Street Lamp: {status}',
        icon=folium.Icon(color=icon_color)
    ).add_to(m)

m.save('C:/Users/basti/Desktop/3Sem/StudieCourse/Networking/street_lamps_map_with_status.html')




