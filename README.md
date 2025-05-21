# pdfeditor
A python program to edit PDF documents. Currently only able to merge several PDF files into a single PDF file, remove specified pages from a single PDF file, or split a PDF file into several PDF files.

## Examples of usage:
python pdfeditor.py -h # to show help message
python pdfeditor.py -f merged_file.pdf -m file1.pdf file2.pdf file3.pdf # merge these files to merged_file.pdf
python pdfeditor.py -f file.pdf -r 1 5-8 10 # remove pages 1, 5 to 8, and 10 from file.pdf and save file as file_removed.pdf
python pdfeditor.py -f file.pdf -s 5 8 # split file into pages 1-4, 5-7, 8-last and save files as file_part_1.pdf, file_part_2.pdf, etc

Depending on machine, sometimes you need to replace python with python3, i.e.
python3 pdfeditor.py -h

## Dependencies
Python libraries used:
1. argparse
2. PyPDF2
3. sys
4. textwrap

## Acknowledgements:
A lot of searches were conducted on the internet in order to create this program.
A few notable ones are below:
1. https://stackoverflow.com/questions/3444645/merge-pdf-files -- This got me started on which libraries enable the editing of PDFs
2. https://pypdf2.readthedocs.io/en/3.x/user/merging-pdfs.html -- This is the documentation of PyPDF2
3. Seitz, J. and Arnold, T. (2021). Black Hat Python : Python programming for hackers and pentesters. San Francisco: No Starch Press. -- This teaches me how to use argparse for a better command line interface e.g. to show a help message whenever I forget how to use the program
