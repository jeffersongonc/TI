import PyPDF2
import os

def joinPDF():
    arqFinal = "PDF_Final.pdf"
    merge = PyPDF2.PdfMerger()

    lista_arquivos = os.listdir()

    for arquivo in lista_arquivos:
        if ".pdf" in arquivo:
            merge.append(f"{arquivo}", None, (0,1))

    merge.write(f"{arqFinal}")

joinPDF()