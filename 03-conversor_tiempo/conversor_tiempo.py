# Programa que convierte segundos a días, horas, minutos y segundos

def cabecera():

    """
    Función que muestra la cabecera del programa
    """

    print("\nℂ𝕠𝕟𝕧𝕖𝕣𝕤𝕠𝕣 𝕕𝕖 𝕋𝕚𝕖𝕞𝕡𝕠")


def convertir_tiempo():

    """
    Función que pide al usuario el tiempo a convertir y realiza las respectivas operaciones.
    """

    print("\nNota: Recuerda que dependiendo de la cantidad de segundos que ingreses, se mostrarán hasta días, horas, minutos o segundos. ")
    segundos = int(input("Ingresa los segundos que quieres convertir: "))

    if segundos >= 86400:
        dias = segundos // 86400
        seg_restan = segundos % 86400

        horas = seg_restan // 3600
        seg_restan2 = seg_restan % 3600

        minutos = seg_restan2 // 60
        seg = seg_restan2 % 60

        print(f"\n{segundos} segundos son: {dias} d {horas} h {minutos} min {seg} s")

    elif segundos >= 3600:
        horas = segundos // 3600
        seg_restan = segundos % 3600
        
        minutos = seg_restan // 60
        seg = seg_restan % 60

        print(f"\n{segundos} segundos son: {horas} h {minutos} min {seg} s")

    elif segundos < 3600 and segundos >= 60:
        minutos = segundos // 60
        seg = segundos % 60
        
        print(f"\n{segundos} segundos son: {minutos} min {seg} s")

    elif segundos < 60 and segundos > 0:
        print(f"\n{segundos} segundos son: {segundos} s") 

    elif segundos <= 0:
        print("\nError: los segundos no pueden ser cantidades negativas ni iguales a 0.") 


# Programa

cabecera()
convertir_tiempo()

