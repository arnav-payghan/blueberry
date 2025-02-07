import re

def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+youtube'
    # Use re.search() to find the match in command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name, ELSE retun none
    return match.group(1) if match else None

def remove_words(input_string, words_to_remove):
    # Split the string into words
    words = input_string.split()
    # Remove unwated words from the list
    filtered_words = [words for words in words if words.lower() not in words_to_remove]
    # Join the filtered words back into a string
    result_string = ' '.join(filtered_words)

    return result_string