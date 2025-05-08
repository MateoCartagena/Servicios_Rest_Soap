import zeep
from config import WSDL_URL

# Crear un cliente SOAP para el servicio de conversión de temperatura
client = zeep.Client(wsdl=WSDL_URL)

def convertir_temperatura(celsius):
    return client.service.CelsiusToFahrenheit(celsius)
