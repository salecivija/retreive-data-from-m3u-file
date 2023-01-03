#!/usr/bin/env python

import re
import json
import tkinter as tk
from tkinter import filedialog
import subprocess

def parse_m3u():
  # Open the M3U file in read mode
  f = open(file_path.get(), 'r', encoding='utf-8')

  # Read the contents of the file into a list
  lines = f.readlines()

  # Close the file
  f.close()

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

  # Open a temporary file for writing
  with open('temp.json', 'w') as f:
    # Write the JSON array to the file
    f.write(json_data)

  # Open the file in Notepad
  subprocess.run(['notepad.exe', 'temp.json'])

# Create the GUI window
root = tk.Tk()
root.title('M3U Parser')
root.geometry('320x240')

# Create a label
label = tk.Label(root, text='Select an M3U file:')
label.pack()

# Create a text entry field
# Create a text entry field to store the file path
file_path = tk.StringVar()
entry = tk.Entry(root, textvariable=file_path)
entry.pack()

# Create a button to open the file selection dialog
button = tk.Button(root, text='Browse', command=lambda: file_path.set(filedialog.askopenfilename()))
button.pack()

# Create a button to parse the M3U file
parse_button = tk.Button(root, text='Parse M3U', command=parse_m3u)
parse_button.pack()

# Run the GUI loop
root.mainloop()
