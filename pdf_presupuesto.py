from fpdf import FPDF

def generar_pdf(nombre_negocio, cliente, nombres, cantidades, precios_unitarios, subtotal, descuento, iva, total):
    pdf = FPDF()
    pdf.add_page()
    
    # Encabezado
    pdf.image("logo.png", 10, 8, 25)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, nombre_negocio, ln=True, align="C")
    pdf.ln(10)
    
    # Cliente
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Cliente: {cliente}", ln=True)
    pdf.ln(5)
    
    # Tabla
    pdf.set_font("Arial", "B", 10)
    pdf.cell(80, 8, "Producto", border=1)
    pdf.cell(25, 8, "Cantidad", border=1)
    pdf.cell(35, 8, "Precio U.", border=1)
    pdf.cell(40, 8, "Importe", border=1)
    pdf.ln()
    
    pdf.set_font("Arial", "", 10)
    for i in range(len(nombres)):
        importe = cantidades[i] * precios_unitarios[i]
        pdf.cell(80, 8, str(nombres[i]), border=1)
        pdf.cell(25, 8, str(cantidades[i]), border=1)
        pdf.cell(35, 8, f"${precios_unitarios[i]}", border=1)
        pdf.cell(40, 8, f"${importe}", border=1)
        pdf.ln()
    
    pdf.ln(5)
    
    # Totales
    pdf.set_font("Arial", "", 11)
    pdf.cell(140, 6, "Subtotal:", align="R")
    pdf.cell(40, 6, f"${subtotal}", ln=True)
    
    pdf.cell(140, 6, "Descuento:", align="R")
    pdf.cell(40, 6, f"${descuento}", ln=True)
    
    pdf.cell(140, 6, "IVA (21%):", align="R")
    pdf.cell(40, 6, f"${iva}", ln=True)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(140, 8, "TOTAL:", align="R")
    pdf.cell(40, 8, f"${total}", ln=True)
    
    return bytes(pdf.output())