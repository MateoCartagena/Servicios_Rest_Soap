# 🌦️ ClimaSeguro - API REST + Cliente SOAP

Este proyecto es una API REST desarrollada con Flask que permite registrar zonas agrícolas y consultar temperaturas convertidas mediante un servicio SOAP externo. Es ideal para prácticas de integración de servicios REST y SOAP en un contexto agrícola.

## 📁 Estructura del proyecto

```text
clima_seguro_api/
├── api/
│   ├── __init__.py
│   ├── routes.py
│   └── temperature.py
├── app.py
├── config.py
├── requirements.txt
└── README.md
```


## 🚀 Instrucciones de ejecución

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/tu_usuario/climaseguro.git
   cd climaseguro

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt

3. **Ejecutar el servidor**
   ```bash
   python main.py

## 🌐 Acceder a la documentación Swagger

[http://localhost:5000/apidocs](http://localhost:5000/apidocs)

# 🔁 Pruebas con CURL

1. ✅ Registrar zona
   ```bash
   curl -X POST http://localhost:5000/zonas \
     -H "Content-Type: application/json" \
     -d "{\"nombre\":\"Zona Andina\",\"cultivo_principal\":\"Papa\",\"hectareas\":120,\"coordenadas\":{\"latitud\":-2.15,\"longitud\":-78.5}}"

   ![POST](https://github.com/user-attachments/assets/7f02e2d0-ea1b-42d1-be1e-aa7a7a26ddce)


2. 📋 Listar todas las zonas
   ```bash
   curl http://localhost:5000/zonas

   ![GET Zonas](https://github.com/user-attachments/assets/daf69499-19b9-4823-8ca1-b8a969c3878d)

3. 🔍 Obtener zona por ID
   ```bash
   curl http://localhost:5000/zonas/1

   ![GET Zonas ID](https://github.com/user-attachments/assets/5d7e507d-001d-48a3-a32c-2608c6a605d6)


4. ❌ Eliminar zona
   ```bash
   curl -X DELETE http://localhost:5000/zonas/1

   ![DELETE](https://github.com/user-attachments/assets/e43de11a-faba-4483-b0a4-85dec1ae9519)


5. 🌡️ Convertir temperatura (SOAP)
   ```bash
   curl "http://localhost:5000/temperatura/convertir?valor=35"

   ![SOAP](https://github.com/user-attachments/assets/ab3732c8-ebfe-453c-ac03-92db15a541e4)


