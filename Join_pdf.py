import PyPDF2

# ABRIR LOS ARCHIVOS
pdf1_path = 'archivo1.pdf'
pdf2_path = 'archivo2.pdf'

# INSTANCIAMOS DE LA CLASE DE PDF
pdf_writer = PyPDF2.PdfFileWriter()

# AGREGAMOS UNA FUNCION PARA UNIR A LOS PDF
def agregar_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_path, 'rb'))
    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)

# AGREGAMOS LAS PAGINAS DE LOS PDF
agregar_pdf(pdf1_path)
agregar_pdf(pdf2_path)

# FINALMENTE CREAMOS UN NUEVO PDF FINAL
with open('resultado.pdf', 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

print('Archivos PDF unidos con éxito.')
