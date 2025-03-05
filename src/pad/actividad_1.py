import json
import requests
import sys
import os

class Actividad_1():
    def __init__(self):
        self.ruta_static="src/pad/static/"
        self.ruta_json="src/pad/static/json"
        directorio = os.path.dirname(self.ruta_json)
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        sys.stdout.reconfigure(encoding='utf-8')

    def leer_api(self, url):
        # El get()método envía una solicitud de GET a la url especificada.
        response = requests.get(url)
        return response.json()
    
    
    def escribir_json(self,nombre_archivo="",datos=None): # "" '' """ """
        if nombre_archivo=="":
            nombre_archivo="datos.json"
        if datos is None:
            datos = "No hay datos"
        ruta_json = "{}json/{}".format(self.ruta_static,nombre_archivo)
        try:
            with open(ruta_json, 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)
                #f.write(str(datos))
                #ajuste
        except Exception as e:
            print("Error:",e)

        return True # booleano True (1) False (0)

    

# Se crea una intancia de la clase
ingestion = Actividad_1()


datos_json = ingestion.leer_api("https://api-colombia.com/api/v1/Region")
print("datos json:",datos_json)

print("****************************************************") 


if ingestion.escribir_json(nombre_archivo="entrega_actividad_1.json",datos=datos_json):
    print("Se creo el archivo json exitosamente.")





    