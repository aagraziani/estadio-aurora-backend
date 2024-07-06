from app.database import get_db


class Banda:
    def __init__(self, id_band=None, nombre=None, genero=None, fecha=None, foto=None):
        self.id_band = id_band
        self.nombre = nombre
        self.genero = genero
        self.fecha = fecha
        self.foto = foto

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Bandas")
        rows = cursor.fetchall()

        bands = []
        for row in rows:
            bands.append(
                Banda(
                    id_band=row[0],
                    nombre=row[1],
                    genero=row[2],
                    fecha=row[3],
                    foto=row[4],
                )
            )
        cursor.close()
        return bands

    @staticmethod
    def get_by_id(id_band):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM bandas WHERE id = %s", (id_band,))

        row = cursor.fetchone()
        cursor.close()

        if row:
            return Banda(
                id_band=row[0],
                nombre=row[1],
                genero=row[2],
                fecha=row[3],
                foto=row[4],
            )
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""DELETE FROM bandas WHERE id = %s""", (self.id_band,))
        db.commit()
        cursor.close()

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_band:  # Actualizar Tarea existente
            cursor.execute(
                """
                UPDATE Bandas
                SET nombre = %s, genero = %s, fecha = %s, foto = %s,
                WHERE id = %s
                """,
                (self.nombre, self.genero, self.fecha, self.foto, self.id_band),
            )
        else:  # Crear Tarea nueva
            cursor.execute(
                """
                INSERT INTO Bandas
                (nombre, genero, fecha, foto)
                VALUES (%s, %s, %s, %s)
                """,
                (self.nombre, self.genero, self.fecha, self.foto),
            )
            self.id_band = cursor.lastrowid
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            "id": self.id_band,
            "nombre": self.nombre,
            "genero": self.genero,
            "fecha": self.fecha,
            "foto": self.foto,
        }
