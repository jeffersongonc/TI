# Funções para fazer 
# Abrir em tela cheia (Consegui abrir no tamanho da janela)
# Ajustar visualização do documento
# Virar página def rotate_page
# Imprimir def print_file
# Juntar def join_pdf
# Converter Word def convert_doc
# Converter Excel def convert_xls
# Converter PowerPoint def convert_ppt
# Converter Imagem def convert_img
# Converter HTML def convert_html
# Converter PDF Pesquisável
# Converter PDF/A
# Comprimir
# Enviar arquivo por e-mail def send_mail
# Editar o PDF
# Assinar Eletrônicamente
# Marca d'agua
# Desproteger
# Proteger


#https://www.thepythoncode.com/article/make-pdf-viewer-with-tktinter-in-python
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import os
from miner import PDFMiner
import win32api


# creating a class called PDFViewer
class PDFViewer:
    # initializing the __init__ / special method
    def __init__(self, master):
        # Tamanho da janela
        winHeigth = win32api.GetSystemMetrics(1)
        winWidth = win32api.GetSystemMetrics(0)
        # path for the pdf doc
        self.path = None
        # state of the pdf doc, open or closed
        self.fileisopen = None
        # author of the pdf doc
        self.author = None
        # name for the pdf doc
        self.name = None
        # the current page for the pdf
        self.current_page = 0
        # total number of pages for the pdf doc
        self.numPages = None    
        # creating the window
        self.master = master
        # gives title to the main window
        self.master.title('PDF Viewer')
        # gives dimensions to main window
        self.master.geometry(str(int(winWidth*0.5)) + 'x' + str(winHeigth))#('580x520+440+180')
        # this disables the minimize/maximize button on the main window
        #self.master.resizable(width = 0, height = 0)
        # loads the icon and adds it to the main window
        self.master.iconbitmap(self.master, 'pdf_file_icon.ico')
        # creating the menu
        self.menu = Menu(self.master)
        # adding it to the main window
        self.master.config(menu=self.menu)
        # creating a sub menu
        self.filemenu = Menu(self.menu)
        self.editmenu = Menu(self.menu)
        self.viewmenu = Menu(self.menu)
        self.signmenu = Menu(self.menu)
        self.helpmenu = Menu(self.menu)
        # giving the sub menu a label
        self.menu.add_cascade(label="Arquivo", menu=self.filemenu)
        self.menu.add_cascade(label="Editar", menu=self.editmenu)
        self.menu.add_cascade(label="Visualizar", menu=self.viewmenu)
        self.menu.add_cascade(label="Assinar", menu=self.signmenu)
        self.menu.add_cascade(label="Ajuda", menu=self.helpmenu)
        # adding a two buttons to the sub menus
        # Menu Arquivo
        self.filemenu.add_command(label="Abrir", command=self.open_file)
        self.filemenu.add_command(label="Imprimir", command=self.print_file)
        self.filemenu.add_command(label="Juntar PDFs", command=self.join_pdf)
        self.filemenu.add_command(label="Sair", command=self.master.destroy)
        # Menu Editar
        self.editmenu.add_command(label="Localizar", command=self.find_text)
        self.editmenu.add_command(label="Enviar por E-mail", command=self.send_mail)
        # Menu Visualizar
        self.viewmenu.add_command(label="Converter para Word", command=self.convert_doc)
        self.viewmenu.add_command(label="Converter para Excel", command=self.convert_xls)
        self.viewmenu.add_command(label="Converter para PowerPoint", command=self.convert_ppt)
        self.viewmenu.add_command(label="Converter para Imagem", command=self.convert_img)
        self.viewmenu.add_command(label="Converter para HTML", command=self.convert_html)
        self.viewmenu.add_command(label="Girar a Página ->", command=self.rotate_page_right)
        self.viewmenu.add_command(label="Girar a Página <-", command=self.rotate_page_left)
        # creating the top frame
        self.top_frame = ttk.Frame(self.master, width=int(winWidth*0.5), height=int(winHeigth*0.8))#width=580, height=460)
        # placing the frame using inside main window using grid()
        self.top_frame.grid(row=0, column=0)
        # the frame will not propagate
        self.top_frame.grid_propagate(False)
        # creating the bottom frame
        self.bottom_frame = ttk.Frame(self.master, width=int(winWidth*0.5), height=50)
        # placing the frame using inside main window using grid()
        self.bottom_frame.grid(row=1, column=0)
        # the frame will not propagate
        self.bottom_frame.grid_propagate(False)
        # creating a vertical scrollbar
        self.scrolly = Scrollbar(self.top_frame, orient=VERTICAL)
        # adding the scrollbar
        self.scrolly.grid(row=0, column=1, sticky=(N,S))
        # creating a horizontal scrollbar
        self.scrollx = Scrollbar(self.top_frame, orient=HORIZONTAL)
        # adding the scrollbar
        self.scrollx.grid(row=1, column=0, sticky=(W, E))
        # creating the canvas for display the PDF pages
        self.output = Canvas(self.top_frame, bg='#ECE8F3', width=int(winWidth*0.48), height=int(winHeigth*0.75))
        # inserting both vertical and horizontal scrollbars to the canvas
        self.output.configure(yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set)
        # adding the canvas
        self.output.grid(row=0, column=0)
        # configuring the horizontal scrollbar to the canvas
        self.scrolly.configure(command=self.output.yview)
        # configuring the vertical scrollbar to the canvas
        self.scrollx.configure(command=self.output.xview)
        # loading the button icons
        self.uparrow_icon = PhotoImage(file='uparrow.png')
        self.downarrow_icon = PhotoImage(file='downarrow.png')
        # resizing the icons to fit on buttons
        self.uparrow = self.uparrow_icon.subsample(3, 3)
        self.downarrow = self.downarrow_icon.subsample(3, 3)
        # creating an up button with an icon
        self.upbutton = ttk.Button(self.bottom_frame, image=self.uparrow, command=self.previous_page)
        # adding the button
        self.upbutton.grid(row=0, column=1, padx=(270, 5), pady=8)
        # creating a down button with an icon
        self.downbutton = ttk.Button(self.bottom_frame, image=self.downarrow, command=self.next_page)
        # adding the button
        self.downbutton.grid(row=0, column=3, pady=8)
        # label for displaying page numbers
        self.page_label = ttk.Label(self.bottom_frame, text='page')
        # adding the label
        self.page_label.grid(row=0, column=4, padx=5)
        
    # function for opening pdf files
    def open_file(self):
        # open the file dialog
        global filepath
        filepath = fd.askopenfilename(title='Select a PDF file', initialdir=os.getcwd(), filetypes=(('PDF', '*.pdf'), ))
        # checking if the file exists
        if filepath:
            # declaring the path
            self.path = filepath
            # extracting the pdf file from the path
            filename = os.path.basename(self.path)
            # passing the path to PDFMiner 
            self.miner = PDFMiner(self.path)
            # getting data and numPages
            data, numPages = self.miner.get_metadata()
            # setting the current page to 0
            self.current_page = 0
            # checking if numPages exists
            if numPages:
                # getting the title
                self.name = data.get('title', filename[:-4])
                # getting the author
                self.author = data.get('author', None)
                self.numPages = numPages
                # setting fileopen to True
                self.fileisopen = True
                # calling the display_page() function
                self.display_page()
                # replacing the window title with the PDF document name
                self.master.title(self.name)
    
    # Impressão
    def print_file(self):
        win32api.ShellExecute(0, "print", filepath, None, ".", 0)

    # the function to display the page  
    def display_page(self):
        # checking if numPages is less than current_page and if current_page is less than
        # or equal to 0
        if 0 <= self.current_page < self.numPages:
            # getting the page using get_page() function from miner
            self.img_file = self.miner.get_page(self.current_page)
            # inserting the page image inside the Canvas
            self.output.create_image(0, 0, anchor='nw', image=self.img_file)
            # the variable to be stringified
            self.stringified_current_page = self.current_page + 1
            # updating the page label with number of pages 
            self.page_label['text'] = str(self.stringified_current_page) + ' of ' + str(self.numPages)
            # creating a region for inserting the page inside the Canvas
            region = self.output.bbox(ALL)
            # making the region to be scrollable
            self.output.configure(scrollregion=region)         

    # function for displaying next page
    def next_page(self):
        # checking if file is open
        if self.fileisopen:
            # checking if current_page is less than or equal to numPages-1
            if self.current_page <= self.numPages - 1:
                # updating the page with value 1
                self.current_page += 1
                # displaying the new page
                self.display_page()
                            
    # function for displaying the previous page        
    def previous_page(self):
        # checking if fileisopen
        if self.fileisopen:
            # checking if current_page is greater than 0
            if self.current_page > 0:
                # decrementing the current_page by 1
                self.current_page -= 1
                # displaying the previous page
                self.display_page()
    # Join files
    def join_pdf(self):
        pass
    # Function for find text the page
    def find_text(self):
        pass
    # Function for send file for mail
    def send_mail(self):
        pass
    # Converter Word 
    def convert_doc(self):
        pass
    # Converter Excel 
    def convert_xls(self):
        pass
    # Converter PowerPoint 
    def convert_ppt(self):
        pass
    # Converter Imagem 
    def convert_img(self):
        pass
    # Converter HTML 
    def convert_html(self):
        pass
    # Function for rotate the page
    def rotate_page_right(self):
        rotation_angle = 90
        
        pass

    def rotate_page_left(self):
        rotation_angle = -90
        pass

# creating the root winding using Tk() class
root = Tk()
# instantiating/creating object app for class PDFViewer
app = PDFViewer(root)
# calling the mainloop to run the app infinitely until user closes it
root.mainloop()