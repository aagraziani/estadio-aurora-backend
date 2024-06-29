from app.database import get_db

class Task:
    def __init__(self, id_task=None, nombre=None, fecha=None, foto=None, genero=None):
        self.id_task = id_task
        self.nombre = nombre
        self.fecha = fecha
        self.foto = foto
        self.genero = genero

    @staticmethod
    def __get_tasks_by_query(query):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        tasks = []
        for row in rows:
            tasks.append(
                Task(
                    id_task = row[0],
                    nombre = row[1],
                    fecha = row[2],
                    foto = row[3],
                    genero= row[4]
                )
            )
        cursor.close()
        return tasks
    
    @staticmethod
    def get_by_id(id_task):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Tareas WHERE id = %s", (id_task,))

        row = cursor.fetchone()
        cursor.close()

        if row:
            return Task(
                id_task = row[0],
                nombre = row[1],
                fecha = row[2],
                foto = row[3],
                genero= row[4]
            )
        return None
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_task: # Actualizar Tarea existente
            cursor.execute(
                """
                UPDATE tareas
                SET nombre = %s, fecha = %s, foto = %s
                WHERE id = %s
                """,
                (self.nombre, self.fecha, self.foto, self.genero, self.id_task))
        else: # Crear Tarea nueva
            cursor.execute(
                """
                INSERT INTO tareas
                (nombre, fecha,, foto, genero)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (self.nombre, self.fecha, self.foto, self.genero))
            self.id_task = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE tareas SET activa = false WHERE id = %s", (self.id_task,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id': self.id_task,
            'nombre': self.nombre,
            'fecha': self.fecha,
            'foto': self.foto,
            'genero': self.genero
        }
