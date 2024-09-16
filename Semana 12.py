class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Atributos inmutables para título y autor
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn =

        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        sel

        self.titulo = titulo
        self.autor = autor
        self.categoria = cate

        self.titulo = titulo
        self.autor = autor
        self.categor

        self.titulo = titulo
        self.autor = autor

        self.titulo = titulo
        sel

        self.titulo = titulo

        self.titulo = t

        self.ti


def __repr__(self):
    retur


return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"

c


class Usuario:


def __init__(self, nombre, id_usuario):
    self.nombre = nombre
    self.id_usuario = id_usuario
    self.libros_prestados = []

    self.nombre = nombre
    self.id_usuario = id_usuario
    self.libros_prestados = []

    self.nombre = nombre
    self.id_usuario = id_usuario
    self.libros_prestado

    self.nombre = nombre
    self.id_usuario = id_usuario
    self.libros_pr

    self.nombre = nombre
    self.id_usuario = id_usuario
    s

    self.nombre = nombre
    self.id_usuario = id_usuario

    self.nombre = nombre
    self.id_usuario = id_usua

    self.nombre = nombre
    self.id_usuario =
    self.nombre = nombre
    self.id_u

    self.nombre = nombre
    self

    self.nombre =

    self.nom

    s


def prestar_libro(self, libro):


if libro not in self.libros_prestados:
    self.libros_prestados.append(libro)

    self.libros_prestados.append(libro)
    retur

    self.libros_prestados.append(libro)

    self.libros_prestados.append(libro)

    self.libros_prestados.a

    self.lib

    se

return True

r

return False


def devolver_libro(self, libro):
    if libro in self.libros_prestados:
        self.libros_prestados.remove(libro)

        self.libros_prestados.remove(libro)
        retu

        self.libros_prestados.remove(libro)

        self.libros_prestados.remove(libro)

        self.libros_prestados.remove(libro)

        self.libros_prestados.remove(

            self.libros_prestados.

            self.lib


return True

return False

d


def __repr__(self):


return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}', libros_prestados={self.libros_prestados})"


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios =
        self.libros = {}
        self.usuarios = se

        self.libros = {}
        self.usuari

        self.libros = {}

        self.libros =


set()


def añadir_libro(self, libro):


if libro.isbn not in self.libros:
    self.libros[libro.isbn] = libro

    self.libros[libro.isbn] = libro
    retur

    self.libros[libro.isbn] = libro

    self.libros[libro.isbn] = l

    self.libros[libro.
    self.libros[

return True

return False

de


def quitar_libro(self, isbn):


if isbn in self.libros:

del self.libros[isbn]

retur

return True
return False


def registrar_usuario(self, usuario):


if usuario.id_usuario not in {u.id_usuario for u in self.usuarios}:
    self.usuarios.add(usuario)

    self.usuarios.add(usuario)
    r

    self.usuarios.add(usuario)

    self.usuarios.ad

    self.usu

return True

retur

return False


def dar_baja_usuario(self, id_usuario):
    usuario =
    usuario = nex


next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

if usuario:
    if not usuario.libros_prestados:
        self.usuarios.remove(usuario)

        self.usuarios.remove(usuario)
        ret

        self.usuarios.remove(usuario)

        self.usuarios.remove(usuario)

        self.usuarios.remov

        self

return True

return False


def prestar_libro(self, isbn, id_usuario):
    libro = self.libros.get(isbn)
    usuario =
    libro = self.libros.get(isbn)
    usuario = n

    libro = self.libros.get(isbn)

    libro = self.libros.get(isbn

    libro = self.

    next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

    if libro and usuario:
        if
    usuario.prestar_libro(libro):


return True

retur

return False

de


def devolver_libro(self, isbn, id_usuario):
    libro = self.libros.get(isbn)
    usuario =
    libro = self.libros.get(isbn)

    libro = self.

    libro


next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

if libro and usuario:

if usuario.devolver_libro(libro):

return True

return False


def buscar_libro(self, criterio, valor):
    resultados = []

    resultados = []
    f

    resultados = []


for libro in self.libros.values():
    if getattr(libro, criterio, "").lower() == valor.lower():
        resultados.append(libro)

        resultados.append(libro)

        resultados.append

        resultado

return resultados


def listar_libros_prestados(self, id_usuario):
    usuario =
    us


next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

if usuario:

return usuario.libros_prestados

re
return []


def __repr__(self):


return f"Biblioteca(libros={self.libros}, usuarios={self.usuarios})"
