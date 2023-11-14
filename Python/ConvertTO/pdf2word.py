from pdf2docx import Converter

pdf_file = r"C:\Projetos\Github\TI\python\convertto\teste.pdf"
docx_file = r"C:\Projetos\Github\TI\python\convertto\teste.docx"

# Convert PDF to DOCX
try:
    file = Converter(pdf_file)
    file.convert(docx_file)
    file.close()
except:
    print('Falha ao tentar converter o arquivo')