import PyPDF2
import sys

# create parameter of pdf to be merged
inputs = sys.argv[1:]

def pdfcombiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('new_pdf_name.pdf')

pdfcombiner(inputs)

