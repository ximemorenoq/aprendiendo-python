# Juego

def cabecera():
    """Muestra la cabecera de la aplicación"""

    titulo = r"""
 ███   ███  █   █ █████ ████  █████  ███   ███   ████ 
█     █   █ ██ ██ █     █   █   █   █   █ █     █     
█  ██ █████ █ █ █ ████  ████    █   █████ █  ██  ███  
█   █ █   █ █   █ █     █  █    █   █   █ █   █     █ 
 ███  █   █ █   █ █████ █   █   █   █   █  ███  ████  

    🎮¡Crea tu identidad gamer!🎮
 """
    print(titulo)



def crear_tag_basico(nombre):
    """
    Crea un gamertag básico usando las primeras 4 letras.
    
    Parámetro:
    nombre (str): El nombre del usuario

    Retorna: 
    str: Gamertag básico
    """

    tag = nombre[:4]
    return tag



def crear_tag_invertido(nombre):
    """
        Crea un gamertag usando el nombre completo.
        
        Parámetro:
        nombre (str): El nombre del usuario
    
        Retorna: 
        str: Nombre invertido
        """

    tag = nombre[::-1]
    return tag



def crear_tag_intercalado(nombre, apellido):
    """
        Crea un gamertag usando el nombre completo y apellido.
            
        Parámetros:
        nombre (str): El nombre del usuario
        apellido (str): El apellido del usuario
        
        Retorna: 
        str: Nombre y apellido intercalado
        """
    print("3. Tag intercalado: ",nombre[0],  apellido[0],  nombre[1:], apellido[1:], sep="")
    return 



def crear_tag_elite(nombre):
    """
        Crea un gamertag usando las 2 primeras y las 2 ultimas letras del nombre.
                
        Parámetro:
        nombre (str): El nombre del usuario
            
        Retorna: 
        str: Nombre elite
        """
    print("4. Tag élite: ", nombre[:2], nombre[-2:], sep="")
    return



def crear_tag_con_numero(nombre, numero):
    """
        Crea un gamertag usando las 5 primeras letras del nombre con su numero favorito.
        
        Parámetros:
        nombre (str): El nombre del usuario
        numero favorito (int): El número favoritio del usuario
          
        Retorna: 
        str: Nombre elite
        """
    print("5. Tag con número: ", nombre[:5], numero, sep="")



def mostrar_estadisticas(nombre):
    """
    Muestra estadísticas del nombre proporcionado.
    
    Parámetro:
    nombre (str): El nombre a analizar
    
    Retorna:
    None (imprime directamente)
    """

    longitud_nombre = len(nombre)

    print("\n📊ESTADÍSTICAS DE TU NOMBRE:")
    print("Nombre completo:", nombre)
    print("Longitud del nombre:", longitud_nombre)
    print("Primera letra:", nombre[0])
    print("Última letra:", nombre[-1])



def  generar_todas_opciones(nombre, apellido, numero):
    """
    Genera y muestra todas las opciones del gamertags.

    Parámetros:
    nombre (str): El nombre del usuario
    apeliido (str): El apellido del usuario
    numero favorito (int): El número favoritio del usuario

    Retorna:
    None (imprime directamente)
    """

    print("\n-----------------------------")
    print("🎯TUS OPCIONES DE GAMERTAG:")
    print("-----------------------------")

    print("\n1. Tag básico: ", crear_tag_basico(nombre))
    print("2. Tag invertido: ", crear_tag_invertido(nombre))
    crear_tag_intercalado(nombre, apellido)
    crear_tag_elite(nombre)
    crear_tag_con_numero(nombre, numero)

    print("\n-----------------------------")



# =================================
# APLICACIÓN PRINCIPAL
# =================================

# Mostrar cabecera
cabecera()

# Solicitar datos al usuario
nombre = input("👤\nIntroduce tu nombre: ")   
apellido = input("📜Introduce tu apellido: ")
numero = input("🔢Introduce tu número favorito: ")

# Mostrar las estadísticas
mostrar_estadisticas(nombre)

# Generar y mostrar las opciones del GamerTags

generar_todas_opciones(nombre, apellido, numero)
print("\n¡Elige tu favorito y conquista el mundo gamer! \n")