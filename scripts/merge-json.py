import json
import os
import requests

# Path to the JSON file containing the list of external URLs
external_urls_file = "port-lists-external/external.json"

# Directory containing the JSON files to be merged
port_lists_dir = "port-lists"

# Output file
output_file = "merged_network_port_prefix.json"

# Load the list of external URLs from the JSON file
with open(external_urls_file, 'r') as f:
    external_urls = json.load(f)

# Initialize merged data and sets to track used network names and ports
merged_data = {}
used_ports = set()
used_networks = set()

# Function to merge data from a JSON source
def merge_data(source_data):
    for network, port in source_data.items():
        network_lower = network.lower()
        if network_lower not in used_networks and port not in used_ports:
            merged_data[network_lower] = port
            used_networks.add(network_lower)
            used_ports.add(port)

# Fetch and merge external JSON data
for url in external_urls:
    response = requests.get(url)
    data = response.json()
    merge_data(data)

# Merge JSON files from the port-lists directory
for filename in os.listdir(port_lists_dir):
    if filename.endswith(".json"):
        with open(os.path.join(port_lists_dir, filename), 'r') as f:
            data = json.load(f)
            merge_data(data)

# Save the merged data to the output file
with open(output_file, 'w') as f:
    json.dump(merged_data, f, indent=4)

print(f"Merged JSON data saved to {output_file}")
