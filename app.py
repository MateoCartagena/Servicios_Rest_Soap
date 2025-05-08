from flask import Flask
from flasgger import Swagger
from api.routes import api_blueprint

app = Flask(__name__)

# Inicializar Swagger con configuración básica
swagger = Swagger(app)

# Registrar las rutas de la API
app.register_blueprint(api_blueprint)

# Ruta raíz informativa
@app.route('/')
def home():
    return "Bienvenido a la API Clima Seguro. Accede a /apidocs para ver la documentación."

if __name__ == '__main__':
    app.run(debug=True)
