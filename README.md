# PlayPeliculas-Django-Backbone
PlayPeliculas un proyecto creado en Python/Django y JavaScript/Backbone
### Instalacion:
- Crea un entorno virtual con virtualenv.
- Clona el repositorio 
``` sh
$ git clone https://github.com/moises1234/PlayPeliculas-Django-Backbone.git 
 ```
- Instalar dependencias
```sh
$ cd PlayPeliculas-Django-Backbone/
$ pip install -r requirements.txt
```
- En caso que sea necesario realiza las migraciones
``` sh
$ python3 manage.py makemigrations pelicula
$ python3 manage.py migrate
```
- Crea un superUsuario
``` sh
$ python3 manage.py createsuperuser
```
- Ejecuta el proyecto
``` sh
$ python3 manage.py runserver
```
### Listo!!
