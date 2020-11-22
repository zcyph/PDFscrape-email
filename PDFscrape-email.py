#!/usr/bin/python
# PDFscrape-email: A script to extract email addresses from PDF files
# Requires pdfminer.six, xerox and xclip

import re, sys, xerox
from pdfminer.high_level import extract_text
from os import system, name

# Clear screen for tidy start
system('clear')

# While loop with try & except to keep asking for file name until a valid one is provided
while True:
    try:
        # If the filename was not passed as a commandline argument, ask user for filename
        if '.pdf' not in str(sys.argv):
            SelectedFile = input("Please enter filename including extension (case sensitive): ")
        # Use the specified commandline argument as filename
        else:
            SelectedFile = str(sys.argv[1])
            print(f"You selected: {SelectedFile}. \n\nSearching...\n")

        # Pass "SelectedFile" into pdfminer's "extract_text" to get its entire contents
        StoredContents = extract_text(SelectedFile)

        # A regex findall to grab email addresses from from the file
        emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", StoredContents)

        # Remove duplicates by passing it through a dictionary
        emails = list(dict.fromkeys(emails))

        # Show how many and what email addresses were found
        print(f'\n{len(emails)} emails found: \n')
        for email in emails:
            print(email)

        # Ask user if they want contents copied to clipboard
        CopyToClipboard = input("\nCopy to clipboard? (y/n) ")

        # Use Xerox to copy to clipboard (convert to string first using .join)
        if CopyToClipboard.lower() == 'y' or 'yes' in CopyToClipboard.lower() or 'yup' in CopyToClipboard.lower():
            clippy = '\n'.join(emails)
            xerox.copy(clippy)
            print("List of emails copied to clipboard.\n")
        else:
            pass

        # Ask user if they would like to save results to file
        SaveToFile = input("Save list to a text file? (y/n) ")

        # If the user chose 'y', write to file
        if SaveToFile.lower() == 'y' or 'yes' in SaveToFile.lower() or 'yup' in SaveToFile.lower():
            TextFile = open('PDFscraped.txt','w')
            for email in emails:
                TextFile.write(email)
                TextFile.write('\n')
            TextFile.close()
            print("List of emails saved to PDFscraped.txt")
        else:
            break
        break

    except:
        system('clear')
        print("That didn't seem to be a valid PDF file, please try again.\n")
        continue
    else:
        break
