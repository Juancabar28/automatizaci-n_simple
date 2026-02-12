import unicodedata
import re

def sanitizar(text):
    # 1. Convertir a minúsculas
    text = text.lower()
    
    # 2. Eliminar tildes, eñes y diéresis
    # NFD descompone caracteres (ej. 'á' -> 'a' + '´') y filtratamos las marcas de acento
    text = unicodedata.normalize('NFD', text)
    text = "".join(c for c in text if unicodedata.category(c) != 'Mn')
    
    # 3. Eliminar caracteres especiales (mantener solo letras, números y espacios)
    # ^a-z0-9\s significa: busca todo lo que NO sea letra, número o espacio
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    # 4. Eliminar espacios extra a los lados
    return text.strip()