# Analizador Léxico en Python

Este proyecto es un **analizador léxico** simple implementado en Python utilizando expresiones regulares. 

Procesa un archivo de entrada (`entrada.txt`) y reconoce diferentes tipos de tokens como:

- Palabras reservadas
- Identificadores
- Números enteros y decimales
- Operadores aritméticos y lógicos
- Delimitadores y signos de puntuación

### 📌 Tabla de símbolos

El programa construye una tabla de símbolos que incluye:

- Identificadores encontrados
- Palabras reservadas utilizadas

### ▶️ Cómo usar

1. Escribe el código fuente en `entrada.txt`.
2. Ejecuta el analizador:

```bash
python analizador_lexico.py
```

3. Se imprimen los tokens detectados por línea y la tabla de símbolos final.

### 📄 Requisitos

- Python 3.x
- Conocimientos básicos de expresiones regulares y análisis léxico.
