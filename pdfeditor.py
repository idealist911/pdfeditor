# NAME: 
#     pdfeditor.py
# USAGE: 
#     python3 pdfeditor.py -u filename1.pdf filename2.pdf ...
# REFERENCES:
# [*] https://pypdf2.readthedocs.io/en/3.x/user/merging-pdfs.html
# [*] https://stackoverflow.com/questions/3444645/merge-pdf-files
# TODO:
# [+] Add argparse

import argparse
import PyPDF2
import sys
import textwrap

class PdfEditor():
    def __init__(self, args):
        self.args = args

    def run(self):
        if self.args.merge:
            self.merge()
        elif self.args.split:
            self.split()
        elif self.args.remove:
            self.remove()

    def merge(self):
        merger = PyPDF2.PdfWriter()

        if self.args.file:
            merged_filename = self.args.file
        else:
            merged_filename = "merged.pdf"
    
        # Append contents in each pdf into PdfWriter
        for filename in self.args.merge:
            with open(filename, "rb") as f:
                merger.append(f)
    
        # Store merged contents into a file
        with open(merged_filename, "wb") as output:
            merger.write(output)
    
        merger.close()

    def remove(self):
        # Exit if file not provided
        try: 
            assert self.args.file 
        except AssertionError as e:
            print("Error: Please provide a file to split.")
            sys.exit()

        writer = PyPDF2.PdfWriter() 

        filename = self.args.file
        remove_list = []

        for page in self.args.remove:
            if '-' in page:
                splitted = page.split('-')
                for split in range(int(splitted[0]), int(splitted[1])+1):
                    # remove all pages within range
                    remove_list.append(split)
            else:
                remove_list.append(int(page))

        f = open(filename, "rb")
        reader = PyPDF2.PdfReader(f)

        for index in range(len(reader.pages)):
            page = index + 1
            if page not in remove_list:
                writer.add_page(reader.pages[index])

        with open(f"{filename[:-4]}_removed.pdf","wb") as output:
            writer.write(output)
    
        f.close()
        writer.close()

    def split(self):
        # Exit if file not provided
        try: 
            assert self.args.file 
        except AssertionError as e:
            print("Error: Please provide a file to split.")
            sys.exit()

        filename = self.args.file

        # Save starting page of each split file into a list
        pages = []
        for page in self.args.split:
            pages.append(int(page))

        read_file = open(filename, "rb")
        pdf_reader = PyPDF2.PdfReader(read_file)
        
        last_page = len(pdf_reader.pages)
        if last_page not in pages:
            pages.append(last_page)
        
        index = 1 # included in split file names
        start_page = 1
        for page_number in pages:
            pdf_writer = PyPDF2.PdfWriter()

            try:
                # (note: range is inclusive of first but not last page)
                assert page_number < (last_page + 1)

                # if last page, save from previous page_number to last page
                # (note: shift left by 1 due to zero indexing)
                if page_number == last_page:
                    for page in range(start_page-1,page_number):
                        pdf_writer.add_page(pdf_reader.pages[page])
                else:
                    # save from previous page_number to (current page_number - 1)
                    for page in range(start_page-1,page_number-1):
                        pdf_writer.add_page(pdf_reader.pages[page])
         
                with open(f"{filename[:-4]}_part_{index}.pdf", 'wb') as file:
                    pdf_writer.write(file)  

                start_page = page_number
                index += 1
        
            except AssertionError as e:
                print("Error: The PDF you are cutting has less pages than you want to cut!")
    
        read_file.close()
        pdf_writer.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="PDF Editor",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''
                Example:
                pdfeditor.py -f merged_file.pdf -m file1.pdf file2.pdf file3.pdf # merge these files to merged_file.pdf
                pdfeditor.py -f file.pdf -r 1 5-8 10 # remove pages 1, 5 to 8, and 10 from file.pdf and save file as file_removed.pdf
                pdfeditor.py -f file.pdf -s 5 8 # split file into pages 1-4, 5-7, 8-last and save files as file_part_1.pdf, file_part_2.pdf, etc
            '''))
    parser.add_argument('-f', '--file', help='file')
    parser.add_argument('-m', '--merge', nargs='+', help='merge files') 
    parser.add_argument('-r', '--remove', nargs='+', help='remove files')
    parser.add_argument('-s', '--split', nargs='+', help='split file')

    args = parser.parse_args()

    editor = PdfEditor(args)
    editor.run()

