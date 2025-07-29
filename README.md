#  - 📌 Proyecto Python – Gestión de Torneos de Tenis

Este proyecto es una aplicación web construida con Django siguiendo el patrón **MVT** (Modelo–Vista–Template). Permite registrar, buscar y listar jugadores, torneos y partidos de tenis. La carga de información solo está habilitada para usuarios autenticados; quienes no estén registrados podrán únicamente visualizar información.


---

## - 🧩 Funcionalidades principales

- Alta de jugadores, torneos y partidos mediante formularios protegidos
- Búsqueda de jugadores por nombre.
- Listado de jugadores, torneos y partidos registrados.
- Navegación basada en herencia de templates (base.html) para mantener coherencia visual.
- Panel de administración para gestionar todos los modelos.

---

## - 👤 Registro, inicio de sesión y perfil personalizado

- Los usuarios pueden registrarse desde /registro/ y loguearse en /login/.
- Tras iniciar sesión, acceden a una pantalla de bienvenida personalizada.
- Cada usuario tiene un perfil propio accesible en /perfil/ donde puede:
      - Visualizar sus datos
      - Subir o modificar su foto de perfil
      - Editar su información
      - Cambiar contraseña en /cambiar_password/
      - La foto de perfil se muestra en el vértice superior derecho de la app, generando una experiencia visual más humana y profesional.
- Los formularios de carga y modificación están protegidos: solo usuarios autenticados pueden acceder.

---

## 🎾 Modelos utilizados

- `Jugador`: nombre, apellido, fecha de nacimiento, nacionalidad y ranking.
- `Torneo`: nombre, sede, pais, fecha de inicio y fecha de finalización del torneo.
- `Partido`: Modalidad (single o doble), jugador1, jugador2, jugador 3 y jugador 4, ganador, torneo, fecha y resultado.

---

## - 🛠️ Orden sugerido para probar el sistema

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

## - ⚙️ ¿Cómo correr el proyecto localmente?

1. Clonar o descargar el repositorio
2. Crear y activar un entorno virtual:

python -m venv env
.\env\Scripts\activate  # En Windows

3. Instalar Django:

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

---

## - 🎨 Estética y experiencia visual

- Paleta cálida y deportiva: naranja polvo de ladrillo, negro elegante y blanco.
- Efectos hover suaves en botones y enlaces.
- Barra de navegación personalizada con colores e identidad visual.
- Formularios unificados con headers y botones personalizados.

---

## 📁 Estructura del proyecto

TORNEO_TENIS
   gestion
      templates
         about.html
         base.html
         bienvenida.html
         buscar_jugador.html
         cambiar_password.html
         editar_perfil.html
         inicio.html
         jugador_form.html
         jugador_list.html
         login.html
         partido_form.html
         ppartido_list.html
         perfil.html
         registro.html
         subir_foto.html
         torneo_form.html
         torneo_list.html
      admin.py
      apps.py
      forms.py
      models.py
      urls.py
      views.py
   media
      avatars
   torneo_tenis
      asgi.py
      settings.py
      urls.py
      wsgi.py
   manage.py
      

