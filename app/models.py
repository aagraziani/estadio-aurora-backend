from app.database import get_db


class Task:
    def __init__(self, id_task=None, nombre=None, genero=None, fecha=None, foto=None):
        self.id_task = id_task
        self.nombre = nombre
        self.genero = genero
        self.fecha = fecha
        self.foto = foto

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
                    id_task=row[0],
                    nombre=row[1],
                    genero=row[2],
                    fecha=row[3],
                    foto=row[4],
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
                id_task=row[0],
                nombre=row[1],
                genero=row[2],
                fecha=row[3],
                foto=row[4],
            )
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_task:  # Actualizar Tarea existente
            cursor.execute(
                """
                UPDATE tareas
                SET nombre = %s, genero = %s, fecha = %s, foto = %s,
                WHERE id = %s
                """,
                (self.nombre, self.genero, self.fecha, self.foto, self.id_task),
            )
        else:  # Crear Tarea nueva
            cursor.execute(
                """
                INSERT INTO tareas
                (nombre, genero, fecha, foto)
                VALUES (%s, %s, %s, %s)
                """,
                (self.nombre, self.genero, self.fecha, self.foto),
            )
            self.id_task = cursor.lastrowid
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            "id": self.id_task,
            "nombre": self.nombre,
            "genero": self.genero,
            "fecha": self.fecha,
            "foto": self.foto
        }
