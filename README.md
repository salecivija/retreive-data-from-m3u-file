# M3U Parser

This code parses an M3U file and retrieves the names and URLs of the channels listed in the file. The resulting data is written to a file as a JSON array.

## Requirements

- Python 3
- json (included in the Python standard library)

## Usage

1. Save the M3U file as `file.m3u` in the same directory as the script.
2. Run the script: `python m3u_parser.py`
3. The data will be written to a file named `data.json`.

## Example Output

```json
[
  ["Channel 1", "http://example.com/channel1"],
  ["Channel 2", "http://example.com/channel2"],
  ...
]
