# Programa que calcula las notas definitivas de una materia y te dice cuanto necesitas para pasar

def cabecera():
    print("\nＳｉｓｔｅｍａ　ｄｅ　Ｃáｌｃｕｌｏ　ｄｅ　Ｎｏｔａｓ")

def mostrar_menu():
    """
    Función creada para que el usuario elija una opción del menú.
    """

    print("""
    \nMenú:
1. Cálculo de nota definitiva
2. Cálculo de última nota
    """)

    opcion = input("\nIngresa tu opción: ")

    return opcion


def pedir_nota(mensaje):
    """
    Función creada para pedirle una nota al usuario hasta que sea un número entre 0.0 y 5.0.
    """
    
    while True:
        try:
                
            nota = float(input(mensaje))
            while nota < 0 or nota > 5:
                print("Nota inválida, debe estar entre 0.0 y 5.0")
                nota = float(input(mensaje))
    
            break
    
        except ValueError: 
            print("Escribe solo números.")     
                
    return nota


# ---------------- FUNCIONALIDADES MODO 1 -----------------
def pedir_notas1():
    """
    Función creada para pedir al usuario su nombre y sus notas.
    """

    nombre = input("\nIngresa tu nombre: ")
    nota1 = pedir_nota("Ingresa la nota 1: ")
    nota2 = pedir_nota("Ingresa la nota 2: ")
    nota3 = pedir_nota("Ingresa la nota 3: ")
    print("Notas recibidas!!")

    return nota1, nota2, nota3, nombre


def calcular_definitiva(nota1, nota2, nota3, nombre):
    """
    Función creada para calcular la nota definitiva del estudiante.
    """

    nota_definitiva = nota1 * 0.3 + nota2 * 0.3 + nota3 * 0.4

    print(f"\n{nombre} tu nota definitiva es: {nota_definitiva:.2f}")

    return nota_definitiva


def mostrar_estado(nota_definitiva):
    """
    Función creada para mostrar al estudiante el estado de su nota, si se encuentra bien, aprobada o reprobada.
    """

    if nota_definitiva >= 4.5:
        print("El estado de tu materia es excelente!")
    elif nota_definitiva >= 3.0:
        print("Tu materia esta aprobada.")
    else:
        print("Tu materia esta reprobada.")



# ---------------- FUNCIONALIDADES MODO 2 --------------------
def pedir_notas2():
    """
    Función creada para pedir al usuario su nombre y sus notas
    """

    nombre = input("\nIngresa tu nombre: ")
    nota1 = pedir_nota("Ingresa la nota 1: ")
    nota2 = pedir_nota("Ingresa la nota 2: ")
    print("Notas recibidas!!")
    
    return nota1, nota2, nombre



def nota_faltante(nota1, nota2):
    """
    Función creada para calcular la nota faltante que necesita el estudiante para aprobar
    """
    nota_actual = nota1 * 0.3 + nota2 * 0.3
    faltante = 3.0 - nota_actual
    nota_final = faltante / 0.4

    return nota_final


def mostrar_resultado(nota_final, nombre):
    """
    Función creada para mostrar el resultado según sea el caso:
        Si necesita más de 5 → ya no alcanza a pasar, aunque saque 5.
        Si necesita 0 o menos → ya pasó, sin importar cuánto saque en la nota 3.
        En cualquier otro caso → cuánto necesita, con dos decimales.
    """

    if nota_final > 5.0:
        print(f"{nombre} necesitas {nota_final:.2f}, ya no alcanzas a aprobar la materia.")

    elif nota_final <= 0:
        print(f"{nombre} ya aprobaste la materia, felicitaciones.")

    else:
        print(f"{nombre} necesitas {nota_final:.2f} para aprobar la materia, aún estás a tiempo.")




# ------------- PROGRAMA PRINCIPAL ----------------



def main():
    cabecera()
    opcion = mostrar_menu()


    if opcion == "1":
        nota1, nota2, nota3, nombre = pedir_notas1()
        nota_definitiva = calcular_definitiva(nota1, nota2, nota3, nombre)
        mostrar_estado(nota_definitiva)

    elif opcion == "2": 
        nota1, nota2, nombre = pedir_notas2()
        nota_final = nota_faltante(nota1, nota2)
        mostrar_resultado(nota_final, nombre)

    else:
        print("Opción incorrecta.")


if __name__ == "__main__":
    main()
