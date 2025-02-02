import re

def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+youtube'
    # Use re.search() to find the match in command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name, ELSE retun none
    return match.group(1) if match else None