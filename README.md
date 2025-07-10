#  Proyecto Python – Gestión de Torneos de Tenis

Este proyecto es una aplicación web construida con Django siguiendo el patrón **MVT** (Modelo–Vista–Template). Permite registrar, buscar y listar jugadores, torneos y partidos de tenis.

---

## Funcionalidades principales

- Alta de jugadores, torneos y partidos mediante formularios.
- Búsqueda de jugadores por nombre.
- Listado de jugadores, torneos y partidos registrados.
- Navegación basada en herencia de templates (base.html).
- Panel de administración para gestionar todos los modelos.

---

## Modelos utilizados

- `Jugador`: nombre, edad y ranking.
- `Torneo`: nombre, sede, fecha de inicio.
- `Partido`: jugador1, jugador2, torneo, resultado y fecha.

---

## Orden sugerido para probar el sistema

1. Ingresar a [http://127.0.0.1:8000/jugadores/nuevo/](http://127.0.0.1:8000/jugadores/nuevo/) para cargar un jugador.
2. Registrar torneos en [http://127.0.0.1:8000/torneos/nuevo/](http://127.0.0.1:8000/torneos/nuevo/)
3. Cargar partidos: [http://127.0.0.1:8000/partidos/nuevo/](http://127.0.0.1:8000/partidos/nuevo/)
4. Consultar:
   - Jugadores: `/jugadores/`
   - Torneos: `/torneos/`
   - Partidos: `/partidos/`
5. Buscar jugador por nombre: `/jugadores/buscar/`
6. Acceder al panel de admin: `/admin/` (tras crear superusuario)

---

## ¿Cómo correr el proyecto localmente?

1. Clonar o descargar el repositorio
2. Crear y activar un entorno virtual:

```bash
python -m venv env
.\env\Scripts\activate  # En Windows

3. Instalar Django:

```bash
pip install django

4. Aplicar migraciones:

python manage.py makemigrations
python manage.py migrate

5. Crear superusuario (opcional)

python manage.py createsuperuser

6. Ejecutar el servidor:

python manage.py runserver

7. Acceder desde el navegador:

http://127.0.0.1:8000/

## Estructura del proyecto

TORNEO_TENIS/
├── .venv/
├── env/
├── gestion/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── gestion/
│           ├── base.html
│           ├── buscar_jugador.html
│           ├── jugador_form.html
│           ├── jugador_list.html
│           ├── partido_form.html
│           ├── partido_list.html
│           ├── torneo_form.html
│           └── torneo_list.html
│
├── torneo_tenis/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── .gitattributes