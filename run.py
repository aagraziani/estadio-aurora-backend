from flask import Flask
from flask_cors import CORS

from app.views import *
from app.database import *

app = Flask(__name__)

# Cors
CORS(app)

# Rutas de API-Rest
app.route('/api/bands/get_all', methods=['GET'])(get_all)

# CRUD
app.route('/api/bands/create/', methods=['POST'])(create_band)
app.route('/api/bands/delete/<int:id_band>', methods=['DELETE'])(delete_band)

create_table_tareas()

# Conexión a BDD
init_app(app)




if __name__ == '__main__':
    app.run(debug=True)