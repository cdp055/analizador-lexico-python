import re  # Importamos el módulo de expresiones regulares (I,N,o)

# Conjunto de palabras reservadas (no pueden ser usadas como identificadores, nombres de variables o funciones)
palabras_reservadas = {
    'if', 'else', 'while', 'for', 'return',
    'int', 'float', 'bool', 'true', 'false',
    'break', 'continue', 'void', 'main'
}

# Diccionario con expresiones regulares para cada tipo de token
regex_patterns = {
    'PALABRA_RESERVADA': r'\b(?:' + '|'.join(palabras_reservadas) + r')\b',  # Palabras clave
    'IDENTIFICADOR': r'\b[a-zA-Z][a-zA-Z0-9_]*[a-zA-Z]\b'  # Variables o nombres válidos
    'NUMERO_DECIMAL': r'\b\d+\.\d+\b',  # Ej: 3.14
    'NUMERO_ENTERO': r'\b\d+\b',  # Ej: 42
    'ASIGNACION': r'=',
    'COMPARADOR_IGUAL': r'==',
    'COMPARADOR_DIFERENTE': r'!=',
    'COMPARADOR_MAYOR_IGUAL': r'>=',
    'COMPARADOR_MENOR_IGUAL': r'<=',
    'COMPARADOR_MAYOR': r'>',
    'COMPARADOR_MENOR': r'<',
    'LOGICO_AND': r'&&',
    'LOGICO_OR': r'\|\|',
    'NEGACION': r'!',
    'SUMA': r'\+',
    'RESTA': r'-',
    'MULTIPLICACION': r'\*',
    'DIVISION': r'/',
    'PARENTESIS_IZQ': r'\(',
    'PARENTESIS_DER': r'\)',
    'LLAVE_IZQ': r'\{',
    'LLAVE_DER': r'\}',
    'PUNTO_Y_COMA': r';',
}

# Tabla de símbolos: aquí se almacenarán los identificadores y palabras reservadas encontradas
tabla_simbolos = set()

# Combinamos todas las expresiones regulares en una sola para buscar cualquier tipo de token
token_regex = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in regex_patterns.items())

# Función para analizar una línea de código y extraer los tokens
def analizar_linea(linea):
    tokens = []
    # Iteramos sobre todos los tokens encontrados usando la expresión regular
    for match in re.finditer(token_regex, linea):
        tipo = match.lastgroup  # Tipo de token (clave del diccionario)
        valor = match.group()   # Valor del token (texto encontrado)

        # Si es identificador o palabra reservada, lo agregamos a la tabla de símbolos
        if tipo in {'IDENTIFICADOR', 'PALABRA_RESERVADA'}:
            tabla_simbolos.add(valor)

        tokens.append((valor, tipo))  # Añadimos el token a la lista de salida
    return tokens

# Función para abrir y procesar un archivo línea por línea
def procesar_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            for num_linea, linea in enumerate(archivo, 1):
                print(f"\n🔹 Línea {num_linea}: {linea.strip()}")
                tokens = analizar_linea(linea)
                for valor, tipo in tokens:
                    print(f"  Token: {valor:15} Tipo: {tipo}")
    except FileNotFoundError:
        print("❌ No se encontró la ruta del archivo .")

    # Al final del análisis mostramos la tabla de símbolos encontrada
    print("\n📌 Tabla de símbolos:")
    for simbolo in sorted(tabla_simbolos):
        print(f"  ➤ {simbolo}")

# Llamada principal a la función
procesar_archivo("entrada.txt")
