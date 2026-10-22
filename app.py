import streamlit as st
import mi_negocio
import calculos
import pdf_presupuesto

st.title(mi_negocio.NOMBRE_NEGOCIO)
st.write(f"Rubro: {mi_negocio.RUBRO}")

cliente = st.text_input("Nombre del cliente")

RENGLONES = 3
nombres = []
cantidades = []
precios_unitarios = []

for i in range(RENGLONES):
    producto = st.selectbox(f"Producto {i + 1}", mi_negocio.productos, key=f"p_{i}")
    cantidad = st.number_input(f"Cantidad {i + 1}", min_value=0, step=1, key=f"c_{i}")
    if cantidad > 0:
        pos = calculos.buscar_posicion(mi_negocio.productos, producto)
        nombres.append(producto)
        cantidades.append(cantidad)
        precios_unitarios.append(mi_negocio.precios[pos])

forma_pago = st.radio("Forma de pago", [calculos.EFECTIVO, calculos.TRANSFERENCIA])

subtotal = calculos.calcular_subtotal(cantidades, precios_unitarios)
descuento = calculos.calcular_descuento(subtotal, forma_pago)
monto_descontado = subtotal - descuento
iva = calculos.calcular_iva(monto_descontado)
total = calculos.calcular_total(subtotal, descuento, iva)

st.subheader("Resumen")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Subtotal", f"${subtotal}")
col2.metric("Descuento", f"${descuento}")
col3.metric("IVA 21%", f"${iva}")
col4.metric("TOTAL", f"${total}")

if len(nombres) == 0:
    st.warning("Elegí al menos un producto con cantidad mayor a 0.")
elif cliente == "":
    st.warning("Falta el nombre del cliente.")
else:
    pdf_bytes = pdf_presupuesto.generar_pdf(
        mi_negocio.NOMBRE_NEGOCIO,
        cliente,
        nombres,
        cantidades,
        precios_unitarios,
        subtotal,
        descuento,
        iva,
        total
    )
    st.download_button("Descargar PDF", data=pdf_bytes, file_name="presupuesto.pdf", mime="application/pdf")