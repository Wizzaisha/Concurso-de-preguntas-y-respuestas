# Concurso-de-preguntas-y-respuestas
Desarrollo del reto "Concurso de preguntas y respuestas" usando Python.

En el desarrollo del reto se utilizaron librerias de Python como tkinter para la interfaz, pymongo para la conexión con la base de datos junto a dnspython para poder leer la URL y requests para la petición http (get) a la API. También se utilizo una API para la obtención de preguntas y respuestas, la cual se llama OPEN TRIVIA DATABASE, en donde se realizo una petición a la API siguiendo las caracteristicas deseadas (25 preguntas de diferente dificultad y de opción multiple).

Nota:
Los modulos de python que se deben tener para ejecutar el programa son:
1. dnspython : Este se puede instalar usando el comando ----> $ python -m pip install dnspython
2. pymongo: Este se puede instalar usando el comando -----> $ python -m pip install pymongo
3. requests: Este se puede instalar usando el comando -----> $ python -m pip install requests

Para correr el programa solo se necesitan tener las librerias mencionadas instaladas y ejecutar el programa, en donde se mostrara una interfaz con las preguntas y las respuestas
para cada una de las rondas. Y se debe ejecutar o correr el main.py para dar inicio.

En el caso de la persistencia de los datos (el historico del jugador) se utilizo una base de datos No-relacional MongoDB, mas espceficicamente la base de datos online MongoAtlas,
para la cual si el programa tiene problemas con la conexión, intentar utilizar la URL para la conexión que se encuentra en el archivo de texto "urls.txt" (esta ya viene integrada en el sistema pero por algun motivo nocarga o aparece por favor utilizarla)
