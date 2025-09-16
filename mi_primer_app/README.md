Video explicativo 
https://github.com/CandeArra/mi_primera_app/releases/tag/v1     

 **Cine - Aplicación Web Estilo Blog sobre Cine**

**Descripción:**

Esta una aplicación web que permite gestionar una base de datos de películas, directores y actores, así como interactuar con otros usuarios a través de mensajes. Los usuarios pueden registrar películas, directores y actores, buscar información sobre ellos, y administrar su perfil.

**Estructura MVT**

Models (models.py): Define las clases Pelicula, Director, Actor, y Profile para gestionar las entidades y sus relaciones en la base de datos.

Views (views.py): Contiene la lógica para crear, listar, y buscar películas, directores, actores, así como la gestión del perfil de usuario.

Templates (templates/peliculas/): Archivos HTML con herencia, formularios para agregar nuevos registros y presentar datos de manera dinámica.

URLs (urls.py): Define las rutas que permiten acceder a cada vista de la aplicación.

**Funcionalidades disponibles**
1. Inicio (Página de inicio)
Al acceder a la página principal, verás:
- Lista de actores registrados.
- Lista de directores registrados.
- Lista de películas cargadas en la base de datos.

Esta página se encuentra disponible para todos los usuarios, ya estén logueados o no, pero no permite realizar acciones como borrar, agregar o editar elementos.

2. About Me
Esta sección muestra mi información personal.
Se presenta en la página de inicio, para que los usuarios puedan conocer más sobre el proyecto y sobre mi.

3. Registro y Login
Registro de Usuario (Signup): Permite a los usuarios crear una cuenta para acceder a todas las funcionalidades (pide usuario, email, contraseña y que repita la contraseña).
Login (Iniciar sesión): Una vez registrado, el usuario puede iniciar sesión y acceder a las funcionalidades exclusivas.

**Funcionalidades para usuarios autenticados**
Una vez que un usuario ha iniciado sesión, se añaden las siguientes opciones de navegación:

1. Crear Nueva Película
Permite a los usuarios registrados agregar nuevas películas a la base de datos.
Los datos requeridos son:

- Título de la película
- Año de estreno
- Género

2. Crear Nuevo Director
Permite agregar nuevos directores a la base de datos con los siguientes datos:

- Nombre del director
- Nacionalidad

3. Crear Nuevo Actor
Permite agregar nuevos actores con la siguiente información:

- Nombre del actor
- Edad

4. Listar Películas
Muestra todas las películas registradas en la base de datos, ordenadas de manera cronológica.

5. Mi Perfil
Permite ver los detalles del perfil del usuario.

El usuario puede:
- Ver su perfil: Nombre de usuario, correo electrónico, biografía, fecha de nacimiento y enlace.
- Editar perfil: Cambiar la biografía, la fecha de nacimiento o el enlace de su perfil.
- Cambiar contraseña: Opción separada para cambiar la contraseña de la cuenta.

6. Mensajes
- Los usuarios pueden enviar mensajes a otros usuarios registrados. 

7. Logout
- Permite cerrar la sesión del usuario y volver a la página de inicio.

**Flujo recomendado**
1. Página de Inicio
2. About me
3. Registro
4. Login
Una vez logueado podras direccionar vos mismo el flujo que quieras seguir:
- Crear película, director y actor: Agregar nuevos registros.
- Listar películas: Ver todas las películas registradas.
- Mi perfil: Ver y editar tus datos personales, cambiar la contraseña.
- Mensajes: Enviar mensajes a otros usuarios.
