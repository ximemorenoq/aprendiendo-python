# ======================================
# CALCULADORA DE FITNESS Y SALUD PERSONAL
# ======================================

def calcular_imc(peso_kg, altura_m):
    """
    Calcula el índice de masa corporal (IMC)

    Fórmula: IMC = peso / (altura^2)

    Parámetros:
    peso_kg (float): Peso en kilogramos
    altura_m (float): Altura en metros

    Retorna:
    float: el IMC calculado
    """

    imc = peso_kg / (altura_m ** 2)
    return imc


def es_peso_saludable(imc):
    """
    Determina si el IMC está en rango (18.5 - 24.9)

    Parámetros:
    imc (float): índice de Masa Corporal

    Retorna:
    bool: True si está en rango saludable, False si no lo esta

    """

    # Operadores de comparación y lógicos

    es_saludable = imc >= 18.5 and imc <= 24.9
    return es_saludable


def tiene_sobrepeso(imc):
    """
    Determina si esta en sobrepeso ( Mayor que 24.9)
    
    Parámetros:
    imc (float): índice de Masa Corporal
    
    Retorna:
    bool: True si está en sobrepeso, False si no lo esta
    
    """

    return imc >= 25


def tiene_bajo_peso(imc):
    """
    Determina si esta de bajo peso (Menor que 18.5)
    
    Parámetros:
    imc (float): índice de Masa Corporal
    
    Retorna:
    bool: True si está en bajo peso, False si no lo esta
    
    """

    return imc < 18.5


def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):
    """
    Calcula las calorias diarias
    
    Parámetros:
    peso_kg (float): peso en kilogramos
    altura_cm (float): altura en centimetros
    edad (int): edad en años
    es_hombre (bool): true si es hombre o false si es mujer
    
    Retorna:
    float: las calorias diarias calculadas según el sexo
    
    """

    calorias_hombre = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)
    calorias_mujer = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)

    return es_hombre * calorias_hombre + (1 - es_hombre) * calorias_mujer


def calcular_agua_diaria(peso_kg):
    """
    Calcula los litros de agua recomendados al dia
        
    Parámetros:
    peso_kg (float): peso en kilogramos
    
    Retorna:
    float: los litros de agua recomendados
    """

    ml_agua = peso_kg * 35
    litros_agua = ml_agua / 1000

    return litros_agua


def calcular_ritmo_cardiaco_maximo(edad):
    """
    Calcula el ritmo cardiaco máximo recomendado en el ejercicio
            
    Parámetros:
    edad (int): edad en años
        
    Retorna:
    int: pulsasiones máximas recomendadas por minuto
    """

    return 220 - edad


def generar_reporte_completo(nombre, peso, altura, edad, es_hombre):
    """
    Genera un reporte completo de salud y fitness
    """

    print("\n="*60)
    print(f"📊 REPORTE DE FITNESS Y SALUD - {nombre}")
    print("="*60)

    # Calculos

    imc = calcular_imc(peso, altura)
    calorias = calcular_calorias_diarias(peso, altura*100, edad, es_hombre)
    agua = calcular_agua_diaria(peso)
    fc_max = calcular_ritmo_cardiaco_maximo(edad)

    # Informaciòn bàsica
    print(f"\n👤 Datos Personales: ")
    print(f"    Peso: {peso} kg ")
    print(f"    Altura: {altura} m")
    print(f"    Edad: {edad}")
    print(f"    ¿Hombre?: {es_hombre}")

    # IMC y evaluacion
    print("\n🦾 Indice de Masa Corporal (IMC):")
    print(f"    Tu IMC: {round(imc, 2)}")
    print(f"    ¿Peso saludable? {es_peso_saludable(imc)}")
    print(f"    ¿Sobrepeso? {tiene_sobrepeso(imc)}")
    print(f"    ¿Bajo peso? {tiene_bajo_peso(imc)}")

    # Calorias
    print(f"\n🍽️ Nutricion: ")
    print(f"    Calorias diarias recomendadas: {round(calorias, 0)} kcal")
    print(f"    Agua diaria recomendada: {round(agua, 2)} litros")


    # Cardio
    print(f"\n❤️ Zona Cardiaca: ") 
    print("     Frecuencia cardiaca maxima {fc_max}")
    print(f"    Zona cardio optima: {round(fc_max*0.6, 0)} - {round(fc_max * 0.8, 0)} bpn")

    print("\n " + "="*60)



# ==============================
 # PROGRAMA PRINCIPAL 
# ==============================

cabecera = """
=============================================

𝙲𝚊𝚕𝚌𝚞𝚕𝚊𝚍𝚘𝚛𝚊 𝚍𝚎 F𝚒𝚝𝚗𝚎𝚜𝚜 𝚢 S𝚊𝚕𝚞𝚍 P𝚎𝚛𝚜𝚘𝚗𝚊𝚕

¡Descubre tus metricas de salud optimas!

=============================================
"""
print(cabecera)

# Solicitar datos
nombre = input("\n👤 ¿Cual es tu nombre? ")
peso = float(input("⚖️ ¿Cuanto pesas? (kg): "))
altura = float(input("📏 ¿Cuanto mides? (m): "))
edad = int(input("🎂 ¿Cuantos años tienes? "))
sexo = input("🗣️ ¿Eres hombre o mujer? (H/M): ")

# Convertir sexo a booleano
es_hombre = sexo == "H" or sexo == "h" or sexo == "hombre"

# Generar el reporte
generar_reporte_completo(nombre, peso, altura, edad, es_hombre)

print("\n No olvides cuidar tu salud💫 \n")