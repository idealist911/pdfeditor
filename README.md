# pdfeditor
A python program to edit PDF documents. Currently only able to merge several PDF files into a single PDF file, remove specified pages from a single PDF file, or split a PDF file into several PDF files.

Python libraries used:
1. argparse
2. PyPDF2
3. sys
4. textwrap

Acknowledgements:
A lot of searches were conducted on the internet in order to create this program.
A few notable ones are below:
1. https://stackoverflow.com/questions/3444645/merge-pdf-files -- This got me started on which libraries enable the editing of PDFs
2. https://pypdf2.readthedocs.io/en/3.x/user/merging-pdfs.html -- This is the documentation of PyPDF2
3. Seitz, J. and Arnold, T. (2021). Black hat Python : Python programming for hackers and pentesters. San Francisco: No Starch Press. -- This teaches me how to use argparse for a better command line interface e.g. to show a help message whenever I forget how to use the program
