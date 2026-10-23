import calculos as cl
import streamlit as st
import mi_negocio as mn
import pdf_presupuesto as ppdf

st.title(mn.NOMBRE_NEGOCIO)

cliente = st.text_input("Nombre del cliente")

# Manejo de los 3 renglones
RENGLONES = 3
nombres = []
cantidades = []
precios_unitarios = []

for i in range(RENGLONES):
    producto = st.selectbox(f"Producto {i + 1}", mn.productos)
    cantidad = st.number_input(f"Cantidad {i + 1}", min_value=0, step=1)
    
    if cantidad > 0:
        pos = cl.buscar_posicion(mn.productos, producto)
        nombres.append(producto)
        cantidades.append(cantidad)
        precios_unitarios.append(mn.precios[pos])

pago = st.radio("Ingrese su método de pago:", [cl.EFECTIVO, cl.TRANSFERENCIA])

subtotal = cl.calcular_subtotal(cantidades, precios_unitarios)
monto_desc = cl.aplicar_descuento(subtotal, pago)
iva = cl.calcular_iva(monto_desc)
total = round(monto_desc + iva, 2)

st.write("El subtotal es: $", subtotal)
st.write("Monto con descuento: $", monto_desc)
st.write("IVA (21%): $", iva)
st.write("El total es: $", total)

numero = st.text_input("Ingresa el numero de compra")
fecha = st.date_input("Fecha de hoy: ")

if len(nombres) == 0:
    st.warning("Seleccioná al menos un producto con cantidad mayor a 0.")
elif numero:
    archivo_pdf = ppdf.armar_pdf(
        numero=numero, 
        fecha=fecha, 
        cliente=cliente, 
        nombres=nombres, 
        cantidades=cantidades, 
        precios=precios_unitarios, 
        subtotal=subtotal, 
        descuento=monto_desc, 
        iva=iva, 
        total=total
    )

    st.download_button(
        label="Descargar presupuesto (PDF)", 
        data=archivo_pdf, 
        file_name=f"presupuesto_{numero}.pdf", 
        mime="application/pdf"
    )