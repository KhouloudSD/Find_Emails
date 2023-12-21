# Copy and paste the provided code

import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails

# Take input text from the user
input_text = input("Enter a piece of text: ")

# Extract and print the emails from the input text
emails = extract_emails(input_text)
print("Extracted emails:", emails)
