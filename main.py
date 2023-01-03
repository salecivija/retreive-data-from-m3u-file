#!/usr/bin/env python

# Import the required libraries
import re
import json

# Open the M3U file in read mode
with open('file.m3u', 'r') as f:
  # Read the contents of the file into a list
  lines = f.readlines()

# Initialize an empty list for the data
data = []

# Iterate through the lines in the file
for line in lines:
  # Check if the line starts with '#EXTINF:'
  if line.startswith('#EXTINF:'):
    # Split the line by ',' and get the name of the channel
    name = line.split(',')[1]
    # Get the next line, which is the URL of the channel
    url = next(f).strip()
    # Add the name and URL to the data list
    data.append((name, url))

# Serialize the data list as a JSON array
json_data = json.dumps(data)

# Open a file for writing
with open('data.json', 'w') as f:
  # Write the JSON array to the file
  f.write(json_data)