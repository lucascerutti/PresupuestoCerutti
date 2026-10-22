EFECTIVO = "Efectivo"
TRANSFERENCIA = "Transferencia"

def buscar_posicion(lista_productos, producto_buscado):
    for i in range(len(lista_productos)):
        if lista_productos[i] == producto_buscado:
            return i
    return -1

def calcular_subtotal(cantidades, precios_unitarios):
    subtotal = 0
    for i in range(len(cantidades)):
        subtotal = subtotal + (cantidades[i] * precios_unitarios[i])
    return subtotal

def calcular_descuento(subtotal, forma_pago):
    if forma_pago == EFECTIVO:
        return subtotal * 0.10
    else:
        return 0

def calcular_iva(monto_descontado):
    return monto_descontado * 0.21

def calcular_total(subtotal, descuento, iva):
    total = subtotal - descuento + iva
    return round(total, 2)