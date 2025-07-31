**Descripción**

Esta es una aplicación estilo blog centrada en el mundo del cine. Permite gestionar una base de datos de películas, directores y actores, además de ofrecer una funcionalidad de búsqueda. 

**Estructura MVT**

Models (`models.py`): Define las clases `Pelicula`, `Director` y `Actor`.
Views (`views.py`): Lógica para crear objetos, listar películas, y buscar.
Templates (`templates/peliculas/`): HTML con herencia, formularios y presentación de datos.
URLs (`urls.py`): Rutas de acceso a cada vista.

**Funcionalidades disponibles**

**Crear Película** => Formulario que permite cargar una nueva película con título, año y género.
**Crear Director** => Formulario para registrar directores con nombre y nacionalidad.
**Crear Actor** => Formulario para agregar actores, incluyendo nombre y edad.
**Buscar Película** => Formulario que permite buscar películas por título. Muestra coincidencias si existen.
**Listar Películas** => Muestra todas las películas guardadas en la base de datos de manera ordenada.
**Página de Inicio** => Desde la raíz (`/`), se muestran todos los actores y directores registrados hasta el momento.

**Navegación recomendada**

1. Desde la raíz (`/`) verás los actores y directores ya cargados.
2. Usá el menú para ir a:
    Cargar nuevas películas, directores y actores
    Buscar una película
    Ver la lista completa de películas

**No hay un orden para utilizar las funciones ya que puede usarse de distintas maneras, pero por logica, diria de crear peliculas primero, y decidir si queres ver la lista de las mismas o buscar una en especifico. Y de querer cargar directores o actores, utilizar sus respectivas funcionalidades. Pero como dije, no tiene un orden.**