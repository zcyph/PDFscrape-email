PDFscrape-email: a script to extract emails from PDF. If you're having trouble manually copying a number of email addresess out of a PDF, give this a try. I hope it helps!

## Requirements

**Python**

This is a Python script, so of course you need to have Python installed to run it. The command may vary depending on your system configuration. You can skip this step if you already know Python is installed.

Debian-based distributions: `sudo apt-get install python`

Arch-based distributions: `sudo pacman -S install python`

Next, make sure you have the required packages:

**pdfminer.six**

`pip install pdfminer.six`

**xerox**

`pip install xerox`

**xclip**

Debian-based distributions: `sudo apt-get install xclip`

Arch-based distributions: `sudo pacman -S xclip`

## Usage

Give the script executable permissions:

`chmod +x PDFscrape-email.py`

Then run it with your PDF filename as a command-line argument:

`./PDFscrape-email.py yourPDFfile.pdf`

Or run it without executable permissions:

`python PDFscrape-email.py yourPDFfile.pdf`

If the file does not reside in the same folder as the script, enter the full absolute path including file name and extension. You can also omit the filename argument and enter the filename when prompted after running the script instead:

![](https://github.com/zcyph/PDFscrape-email/blob/main/screenshot.png)

The script will give you the option of copying the list of emails to clipboard, where you can directly paste it into your email or other applications - and it will also ask you if you'd like to save the list to a text file.
