Proyecto Final Rosas Sandillú, Julián Curso Python Coderhouse

ProyectoFinal es una aplicación web desarrollada en Django que permite a los usuarios registrarse y crear, ver, editar y eliminar videojuegos favoritos, permite a su vez reseñarlos y ordenarlos.
Ademas incluye un foro de discusión entre usuarios registrados, mensajes entre usuarios registrados y una busqueda de videojuegos según ciertas pautas. 
El sistema de autenticación y autorización restringe el acceso a ciertas funciones a usuarios no registrados. 
Incluye también un sistema de edición de perfil y manejo de los avatars, como también un apartado de admin donde se puede manejar toda la pagina.

Funcionalidades:

A continuación se detallan las funcionalidades de ProyectoFinal:

Registro y autenticación:

    Los usuarios pueden registrarse haciendo click en "CREAR USUARIO".
    Los usuarios pueden iniciar sesión en "LOGIN".
    Los usuarios pueden cerrar sesión en la aplicación en cualquier momento en "LOGOUT".

Lista de videojuegos:
    Los usuarios pueden agregar sus videojuegos favoritos haciendo click en "agregar videojuego", una vez agregado lo pueden "editar" y "eliminar".
    Los usuarios pueden agregar reseñas sobre sus videojuegos favoritos haciendo click en "agregar reseña", una vez agregada la pueden "editar" y "eliminar".
    Los usuarios pueden ordenar los videojuegos favoritos por "fecha de lanzamiento" y "valoración".
    
Búsqueda de videojuegos:
    Los usuarios pueden buscar videojuegos guardados en base a su "nombre", "género", "empresa" y "valoración" haciendo click en sus respectivos botones.
    
Foro:
    Los usuarios pueden ver una lista de todos los temas de discusión existentes en el foro.
    Los usuarios pueden ver detalles de un tema de discusión específico haciendo click en el tema.
    Los usuarios pueden crear un nuevo tema de discusión haciendo click en "crear nuevo tema".
    Los usuarios pueden editar un tema de discusión existente haciendo click en "editar".
    Los usuarios pueden eliminar un tema de discusión existente haciendo click en "eliminar".
    Los usuarios pueden comentar un tema de discusión existente haciendo click en el tema y después "agregar".

Mensajes:
    Los usuarios pueden ver una lista de todos las conversaciones haciendo click en "Mensajes" arriba o bajando en la parte del chat, cada usuario tiene su propia mensajería privada con los mensajes que mandó a cada usuario.
    Los usuarios pueden crear una nueva conversación con un mensaje hacia un usuario haciendo click en "CREAR NUEVA CONVERSACIÓN".
    Los usuarios pueden dejar un comentario respondiendo el mensaje que otro usuario les mandó haciendo click en "VER CONVERSACIÓN" y luego "ENVIAR MENSAJE", luego se podrá ver la conversación actualizada en "Mensajes".
    
Perfil:
    Los usuarios pueden editar su perfil haciendo click en "Perfil" y luego "Editar perfil".
    Los usuarios pueden agregar un avatar para su perfil haciendo click en "Perfil" y luego "Agregar Avatar".
    Los usuarios pueden ver los avatares que tiene haciendo click en "Perfil" y luego "Ver los avatares".
    
Administración:
    Los usuarios con permisos de administrador pueden ver, editar, eliminar y agregar todo.

AboutMe
    Cualquiera que entre a la página puede ver el AboutMe sobre el creador de la página.
    
Requerimientos:
Antes de poder utilizar ProyectoFinal, debe tener instalado lo siguiente:
    Python 3.8 o superior
    Django 3.2 o superior

Instalación
Para instalar ProyectoFinal, siga estos pasos:

    Clonar el repositorio de ProyectoFinal en su máquina local utilizando el siguiente comando: git clone https://github.com/your_username/ProyectoFinal.git
    Navegue hasta el directorio ProyectoFinal utilizando el comando cd ProyectoFinal.
    Cree un entorno virtual utilizando el comando python3 -m venv venv.
    Active el entorno virtual utilizando el comando source venv/bin/activate.
    Instale los paquetes necesarios utilizando el comando pip install -r requirements.txt.
    Configure la base de datos utilizando el comando python manage.py migrate.
    Ejecute la aplicación utilizando el comando python manage.py runserver.

Conclusion

¡Eso es todo! Espero que esta descripción te haya gustado, saludos, Julián!
