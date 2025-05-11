
# 📒 Agenda de Contactos - Proyecto en Python

Esta es una aplicación de terminal para la gestión de contactos personales o profesionales. Permite **agregar, buscar, actualizar, eliminar y visualizar contactos ordenados alfabéticamente**, utilizando estructuras de datos como **árboles binarios de búsqueda** y **tablas hash** implementadas manualmente.

## 🎯 Objetivo

El proyecto busca optimizar la forma en que se almacenan y gestionan los contactos, sin el uso de bases de datos ni librerías externas, haciendo énfasis en la eficiencia de búsqueda y ordenamiento usando estructuras clásicas de datos.

---

## ⚙️ Características

- 📥 Agregar nuevos contactos
- 🔍 Buscar contactos (sin distinguir mayúsculas/minúsculas)
- 🗑️ Eliminar contactos
- ✏️ Actualizar contactos existentes
- 📋 Ver todos los contactos ordenados alfabéticamente
- 🌲 Árbol binario para búsquedas eficientes
- #️⃣ Tabla hash con manejo manual de colisiones
- 💻 Interfaz totalmente por consola
- 🎨 Estética agradable en terminal con emojis y separadores

---

## 📦 Requisitos

- Python 3.x
- Terminal compatible con codificación UTF-8 (emojis)

> ⚠️ No se requiere conexión a internet ni instalación de paquetes adicionales.

---

## ▶️ Cómo ejecutar

1. Clona el repositorio:

```bash
git clone [https://github.com/tu_usuario/agenda-contactos-python.git](https://github.com/andrespick/Proyecto-estructura-de-datos.git)
cd agenda-contactos-python
```

2. Ejecuta el archivo principal:

```bash
python agenda_contactos.py
```

---

## 🧠 Estructuras de datos usadas

| Estructura           | Función                                                      |
|----------------------|--------------------------------------------------------------|
| Árbol Binario        | Inserción y búsqueda eficiente de contactos por nombre       |
| Tabla Hash           | Almacenamiento y acceso directo de contactos                 |
| Lista con burbuja    | Ordenamiento manual de todos los contactos alfabéticamente   |

---

## 🛠️ Funciones clave

- `Contacto`: clase para representar cada entrada de la agenda.
- `ArbolBinario`: estructura que optimiza inserción y búsqueda.
- `TablaHash`: almacenamiento eficiente con búsqueda directa.
- `ver_todos_contactos()`: muestra todos los contactos ordenados por nombre.
- `menu()`: interfaz de usuario por consola.

---

## 📚 Justificación académica

Este proyecto fue desarrollado como parte de un trabajo académico para aplicar y demostrar el uso práctico de estructuras de datos, sin depender de bases de datos ni librerías externas. Representa un ejemplo funcional de cómo organizar información eficientemente en aplicaciones pequeñas o educativas.

---

## ✍️ Autores

- Erika Andrea Erazo Rodríguez  
- Diógenes Bermeo Sánchez  
- Andrés Felipe Vela Flórez  
- Jeison Elian Benítez Hernández  

**Docente:** Mabel Liliana Navarrete Rodríguez  
**Institución:** Institución Universitaria Antonio José Camacho  
**Programa:** Tecnología en Sistemas de Información  
**Año:** 2025

---

## 📄 Licencia

Este proyecto es de uso académico y libre bajo la licencia MIT. Puedes modificarlo, distribuirlo o usarlo para tus propios fines educativos.
