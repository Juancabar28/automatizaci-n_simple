from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def obtener_precio_accion(driver, consulta):
    #Limpieza
    palabras_ruido = ["precio", "accion", "valor", "de", "la", "las", "del"]
    busqueda = " ".join([p for p in consulta.split() if p not in palabras_ruido]).strip()

    #búsqueda de Yahoo
    driver.get(f"https://finance.yahoo.com/lookup?s={busqueda}")
    
    try:
        #Esperar a que la tabla de resultados aparezca
        wait = WebDriverWait(driver, 10)
        #Esperamos a que el primer símbolo sea visible
        fila_uno = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr")))

        #Extraemos datos de las columnas de la tabla
        #Columna 1: Símbolo (Ticker)
        ticker = fila_uno.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text
        
        #Columna 2: Nombre de la empresa
        nombre = fila_uno.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
        
        #Columna 3: Último precio (Last Price)
        precio = fila_uno.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text

        return f"Encontrado: {nombre} [{ticker}]. Precio: ${precio} USD (Yahoo Finance)."

    except Exception as e:
        # Si algo falla, tomamos foto para ver si la tabla cambió
        driver.save_screenshot("error_yahoo_tabla.png")
        return f"No pude extraer los datos de la tabla para '{busqueda}'. Intenta con el ticker directamente (ej: AAPL)."