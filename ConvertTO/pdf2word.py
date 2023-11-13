from pdf2docx import Converter

pdf_file = 'teste.pdf'
docx_file = 'teste.docx'

# Convert PDF to DOCX
file = pdf2docx.Converter(pdf_file)
file.convert(docx_file)
file.close()