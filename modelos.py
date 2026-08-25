class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def to_dict(self):
        """Convierte el objeto a diccionario, necesario para guardarlo en JSON."""
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "disponible": self.disponible,
        }

    @staticmethod
    def from_dict(datos):
        """Reconstruye un objeto Libro a partir de un diccionario leído del JSON."""
        return Libro(datos["titulo"], datos["autor"], datos["isbn"], datos["disponible"])

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} — {self.autor} (ISBN: {self.isbn}) [{estado}]"