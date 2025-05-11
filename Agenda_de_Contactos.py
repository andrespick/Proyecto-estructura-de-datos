# -----------------------------
# Clase Contacto
# -----------------------------
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.nombre_key = nombre.lower()
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"📇 Nombre: {self.nombre}\n   📞 Teléfono: {self.telefono}\n   📧 Email: {self.email}"

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
        return sum(ord(c) for c in clave) % self.tamaño

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
            contactos.extend(sublista)
        return contactos

# -----------------------------
# Interfaz de Usuario
# -----------------------------


def menu():
    arbol = ArbolBinario()
    hash_tabla = TablaHash()

    while True:
        print("\n" + "═" * 50)
        print("📒 AGENDA DE CONTACTOS INTELIGENTE 📒".center(50))
        print("═" * 50)
        print("1️⃣  Agregar contacto")
        print("2️⃣  Buscar contacto")
        print("3️⃣  Eliminar contacto")
        print("4️⃣  Actualizar contacto")
        print("5️⃣  Ver todos los contactos")
        print("6️⃣  Salir")
        print("─" * 50)
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            print("\n📥 INGRESAR NUEVO CONTACTO")
            nombre = input("📝 Nombre: ")
            telefono = input("📞 Teléfono: ")
            email = input("📧 Email: ")
            contacto = Contacto(nombre, telefono, email)
            arbol.insertar(contacto)
            hash_tabla.insertar(contacto)
            print("✅ Contacto agregado exitosamente.")

        elif opcion == "2":
            print("\n🔍 BUSCAR CONTACTO")
            nombre = input("🔎 Nombre a buscar: ")
            contacto = hash_tabla.buscar(nombre)
            if contacto:
                print("\n✅ Contacto encontrado:\n")
                print(contacto)
            else:
                print("❌ Contacto no encontrado.")

        elif opcion == "3":
            print("\n🗑️ ELIMINAR CONTACTO")
            nombre = input("🗑️ Nombre del contacto a eliminar: ")
            if hash_tabla.eliminar(nombre):
                print("✅ Contacto eliminado.")
            else:
                print("❌ Contacto no encontrado.")

        elif opcion == "4":
            print("\n✏️ ACTUALIZAR CONTACTO")
            nombre = input("🛠️ Nombre del contacto a actualizar: ")
            contacto = hash_tabla.buscar(nombre)
            if contacto:
                print("\n📇 Contacto actual:")
                print(contacto)
                nuevo_telefono = input("📞 Nuevo teléfono: ")
                nuevo_email = input("📧 Nuevo email: ")
                nuevo_contacto = Contacto(
                    contacto.nombre, nuevo_telefono, nuevo_email)
                arbol.insertar(nuevo_contacto)
                hash_tabla.insertar(nuevo_contacto)
                print("✅ Contacto actualizado.")
            else:
                print("❌ Contacto no encontrado.")

        elif opcion == "5":
            ver_todos_contactos(hash_tabla)

        elif opcion == "6":
            print("\n👋 ¡Gracias por usar la Agenda de Contactos!\n")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

# -----------------------------
# Ver todos los contactos ordenados
# -----------------------------


def ver_todos_contactos(tabla_hash):
    print("\n📋 LISTA DE TODOS LOS CONTACTOS:")
    contactos = tabla_hash.obtener_todos()

    # Ordenamiento burbuja
    n = len(contactos)
    for i in range(n):
        for j in range(0, n-i-1):
            if contactos[j].nombre_key > contactos[j+1].nombre_key:
                contactos[j], contactos[j+1] = contactos[j+1], contactos[j]

    if not contactos:
        print("⚠️ No hay contactos guardados.")
    else:
        for i, contacto in enumerate(contactos, 1):
            print(f"\n🟢 Contacto {i}:")
            print(contacto)


# -----------------------------
# Ejecutar la agenda
# -----------------------------
if __name__ == "__main__":
    menu()
