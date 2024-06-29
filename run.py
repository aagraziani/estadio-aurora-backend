from flask import Flask
from app.views import *
from app.database import test_connection, init_app, create_table_tareas

app = Flask(__name__)

# Rutas de API-Rest
app.route("/", methods=["GET"])(index)

# Conexión con la base de datos
init_app(app)

create_table_tareas()

if __name__ == "__main__":
    app.run(debug=True)