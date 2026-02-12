import requests

def obtener_clima(driver, consulta):
    #Limpieza de la consulta
    palabras_ruido = ["clima", "temperatura", "tiempo", "en", "de", "la", "el", "dime", "cual", "es"]
    ciudad = " ".join([p for p in consulta.split() if p not in palabras_ruido]).strip()

    if not ciudad:
        return "Por favor, dime una ciudad."

    #Configuración de la API (OpenStreetMap para geolocalización y Open-Meteo para el clima)
    #APIs son gratuitas y NO requieren registro/llave (API Key)
    try:
        # Obtiene las coordenadas de la ciudad (Latitud y Longitud)
        geo_url = f"https://nominatim.openstreetmap.org/search?city={ciudad}&format=json&limit=1"
        headers = {'User-Agent': 'AsistenteVirtualPython/1.0'}
        
        geo_resp = requests.get(geo_url, headers=headers).json()
        
        if not geo_resp:
            return f"No pude encontrar la ubicación de '{ciudad}'."

        lat = geo_resp[0]['lat']
        lon = geo_resp[0]['lon']
        nombre_completo = geo_resp[0]['display_name'].split(",")[0]

        #Obtiene el clima real con las coordenadas
        clima_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        clima_resp = requests.get(clima_url).json()
        
        temp = clima_resp['current_weather']['temperature']
        viento = clima_resp['current_weather']['windspeed']

        return f"En {nombre_completo}, la temperatura actual es de {temp}°C con vientos de {viento} km/h."

    except Exception as e:
        return f"Error al conectar con el servicio de clima: {str(e)}"