# -----------------------------
# Clase Contacto
# -----------------------------
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre  # Se guarda el nombre original
        self.nombre_key = nombre.lower()  # Usado para búsquedas sin importar mayúsculas
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

# -----------------------------
# Árbol Binario de Búsqueda
# -----------------------------


class NodoArbol:
    def __init__(self, contacto):
        self.contacto = contacto
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, contacto):
        def _insertar(nodo, contacto):
            if nodo is None:
                return NodoArbol(contacto)
            if contacto.nombre_key < nodo.contacto.nombre_key:
                nodo.izquierda = _insertar(nodo.izquierda, contacto)
            elif contacto.nombre_key > nodo.contacto.nombre_key:
                nodo.derecha = _insertar(nodo.derecha, contacto)
            return nodo
        self.raiz = _insertar(self.raiz, contacto)

    def buscar(self, nombre):
        nombre_key = nombre.lower()

        def _buscar(nodo, nombre_key):
            if nodo is None:
                return None
            if nombre_key == nodo.contacto.nombre_key:
                return nodo.contacto
            elif nombre_key < nodo.contacto.nombre_key:
                return _buscar(nodo.izquierda, nombre_key)
            else:
                return _buscar(nodo.derecha, nombre_key)
        return _buscar(self.raiz, nombre_key)

# -----------------------------
# Tabla Hash
# -----------------------------


class TablaHash:
    def __init__(self, tamaño=100):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]

    def _hash(self, clave):
        clave = clave.lower()
        hash_total = 0
        for caracter in clave:
            hash_total += ord(caracter)
        return hash_total % self.tamaño

    def insertar(self, contacto):
        indice = self._hash(contacto.nombre_key)
        for i, c in enumerate(self.tabla[indice]):
            if c.nombre_key == contacto.nombre_key:
                self.tabla[indice][i] = contacto
                return
        self.tabla[indice].append(contacto)

    def buscar(self, nombre):
        nombre_key = nombre.lower()
        indice = self._hash(nombre_key)
        for contacto in self.tabla[indice]:
            if contacto.nombre_key == nombre_key:
                return contacto
        return None

    def eliminar(self, nombre):
        nombre_key = nombre.lower()
        indice = self._hash(nombre_key)
        for i, contacto in enumerate(self.tabla[indice]):
            if contacto.nombre_key == nombre_key:
                del self.tabla[indice][i]
                return True
        return False

    def obtener_todos(self):
        contactos = []
        for sublista in self.tabla:
            for contacto in sublista:
                contactos.append(contacto)
        return contactos

# -----------------------------
# Interfaz de Usuario
# -----------------------------


def menu():
    arbol = ArbolBinario()
    hash_tabla = TablaHash()

    while True:
        print("\n--- AGENDA DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Actualizar contacto")
        print("5. Ver todos los contactos")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            contacto = Contacto(nombre, telefono, email)
            arbol.insertar(contacto)
            hash_tabla.insertar(contacto)
            print("✅ Contacto agregado exitosamente.")

        elif opcion == "2":
            nombre = input("Nombre del contacto a buscar: ")
            contacto = hash_tabla.buscar(nombre)
            if contacto:
                print("📇 Contacto encontrado:\n", contacto)
            else:
                print("⚠️ Contacto no encontrado.")

        elif opcion == "3":
            nombre = input("Nombre del contacto a eliminar: ")
            eliminado = hash_tabla.eliminar(nombre)
            if eliminado:
                print("✅ Contacto eliminado.")
            else:
                print("⚠️ Contacto no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del contacto a actualizar: ")
            contacto = hash_tabla.buscar(nombre)
            if contacto:
                print("📇 Contacto actual:", contacto)
                nuevo_telefono = input("Nuevo teléfono: ")
                nuevo_email = input("Nuevo email: ")
                nuevo_contacto = Contacto(
                    contacto.nombre, nuevo_telefono, nuevo_email)
                arbol.insertar(nuevo_contacto)
                hash_tabla.insertar(nuevo_contacto)
                print("✅ Contacto actualizado.")
            else:
                print("⚠️ Contacto no encontrado.")

        elif opcion == "5":
            ver_todos_contactos(hash_tabla)

        elif opcion == "6":
            print("👋 Saliendo de la agenda...")
            break
        else:
            print("❌ Opción inválida, intenta de nuevo.")

# -----------------------------
# Ver todos los contactos ordenados
# -----------------------------


def ver_todos_contactos(tabla_hash):
    contactos = tabla_hash.obtener_todos()

    # Ordenamiento burbuja manual por nombre_key
    n = len(contactos)
    for i in range(n):
        for j in range(0, n-i-1):
            if contactos[j].nombre_key > contactos[j+1].nombre_key:
                contactos[j], contactos[j+1] = contactos[j+1], contactos[j]

    print("\n📋 Lista de contactos ordenada alfabéticamente:")
    if not contactos:
        print("No hay contactos guardados.")
    else:
        for contacto in contactos:
            print(contacto)


# -----------------------------
# Ejecutar la agenda
# -----------------------------
if __name__ == "__main__":
    menu()
