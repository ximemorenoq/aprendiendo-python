# Programa que simula la caja registradora de una tienda

def cabecera():
    print("\n 🛒 C͟a͟j͟a͟ R͟e͟g͟i͟s͟t͟r͟a͟d͟o͟r͟a͟")


def calcular_subtotal():
    """
    Función creada para pedir los datos del producto al usuario y calcular el subtotal de la compra.
    """

    print("\nRecuerda que las cantidades deben ser mayores a 0.")
    producto = input("Ingresa el nombre del producto: ")
    precio_unidad = float(input("Ingresa el precio unitario del producto: "))
    cantidad = int(input("Ingresa la cantidad de productos: "))

    subtotal = precio_unidad * cantidad
    print(f"Producto: {producto}")
    print(f"Subtotal: {subtotal:,.2f}")

    return subtotal



def calcular_descuento(subtotal):
    """
    Función creada para calcular el descuento de la compra.
    """

    if subtotal >= 200000:
        descuento = subtotal * 10 / 100
        print(f"Descuento (10%): {descuento:,.2f}")
    
    elif subtotal >= 100000:
        descuento = subtotal * 5 / 100
        print(f"Descuento (5%): {descuento:,.2f}")

    else:
        descuento = 0
        print("No se aplica descuento, el valor es menor a 100.000$.")

    return descuento


def calcular_total(subtotal, descuento):
    """
    Función creada para calcular el total de la compra.
    """

    base = subtotal - descuento
    iva = base * 0.19
    total = base + iva

    print(f"IVA (19%): {iva:,.2f}")
    print(f"Total: {total:,.2f}")

    return total


def recibir_pago(total):
    """
    Función creada para recibir el pago, saber si alcanza o no.
    """

    con_cuanto_paga = float(input("¿Con cuánto paga?: "))

    cambio = 0
    faltan = 0

    if con_cuanto_paga > total:
        cambio = con_cuanto_paga - total
        print(f"Cambio: {cambio:,.2f}")

    elif con_cuanto_paga == total:
        cambio = 0
        print(f"Cambio: {cambio:,.2f}")

    else:
        faltan = total - con_cuanto_paga
        print(f"Falta: {faltan:,.2f}")

    return cambio, faltan


def dar_cambio(cambio):
    """
    Función creada para recibir el cambio y decir cuantos billetes entregar de cada uno
    """

    queda = int(cambio)

    cincuenta = queda // 50000
    queda = queda % 50000

    veinte = queda // 20000 
    queda = queda % 20000

    diez = queda // 10000
    queda = queda % 10000

    cinco = queda // 5000
    queda = queda % 5000

    dos = queda // 2000
    queda = queda % 2000

    print("\nEntregar:")
    print(f"  {cincuenta} billete(s) de 50,000")
    print(f"  {veinte} billete(s) de 20,000")
    print(f"  {diez} billete(s) de 10,000")
    print(f"  {cinco} billete(s) de 5,000")
    print(f"  {dos} billete(s) de 2,000")
    print(f"  {queda} en monedas")



# Programa 
cabecera()
subtotal = calcular_subtotal()
descuento = calcular_descuento(subtotal)
total = calcular_total(subtotal, descuento)
cambio, faltan = recibir_pago(total)

if faltan == 0:
    dar_cambio(cambio)

    





