# Create a Python script that will read a list of phone numbers and write them into a CSV file.

import csv

PHONE_NUMBER_FILE = 'phone_numbers.txt'
CSV_FILE = 'phone_numbers.csv'

# Read phone numbers from text file
with open(PHONE_NUMBER_FILE, 'r') as f:
    phone_numbers = f.read().splitlines()

# Write phone numbers to CSV file
with open(CSV_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Phone Number'])
    for phone_number in phone_numbers:
        writer.writerow([phone_number])


# To use this script, create a text file called
#  `phone_numbers.txt` in the same directory as 
# the script and add one phone number per line. 
# Then, run the script and it will create a new file called 
# `phone_numbers.csv`with the same phone numbers in CSV format.







