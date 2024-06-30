from flask import Flask
from flask_cors import CORS

from app.views import *
from app.database import *

app = Flask(__name__)

# Cors
CORS(app)

# Rutas de API-Rest
app.route('/api/tasks/get_all', methods=['GET'])(get_all)

# CRUD
app.route('/api/tasks/create/', methods=['POST'])(create_task)

create_table_tareas()

# Conexión a BDD
init_app(app)




if __name__ == '__main__':
    app.run(debug=True)