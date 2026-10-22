import calculos as cl
import streamlit as st
import mi_negocio as mn
import pdf_presupuesto as ppdf

st.title(mn.NOMBRE_NEGOCIO)

cliente = st.text_input("Nombre del cliente")

producto = st.selectbox("Producto", mn.productos)

cantidad = st.number_input("Cantidad", min_value=0, step=1)

pos = cl.buscar_posicion(mn.productos, producto)
precio = mn.precios[pos]
subtotal = cantidad * precio

pago = st.radio("Ingrese su método de pago:", [cl.EFECTIVO, cl.TRANSFERENCIA])


monto_desc = cl.aplicar_descuento(subtotal, pago)
iva = cl.calcular_iva(monto_desc)
total = round(monto_desc + iva, 2)

st.write("El precio individual es: $", precio)
st.write("El subtotal es: $", subtotal)
st.write("Monto con descuento: $", monto_desc)
st.write("IVA (21%): $", iva)
st.write("El total es: $", total)

numero = st.text_input("Ingresa el numero de compra")
fecha = st.date_input("Fecha de hoy: ")

if numero:
    archivo_pdf = ppdf.armar_pdf(
        numero=numero, 
        fecha=fecha, 
        cliente=cliente, 
        producto=producto, 
        cantidad=cantidad, 
        precio=precio, 
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