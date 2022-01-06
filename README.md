# Concurso-de-preguntas-y-respuestas
Desarrollo del reto "Concurso de preguntas y respuestas" usando Python.

En el desarrollo del reto se utilizaron librerias de Python como tkinter para la interfaz y pymongo para la conexión con la base de datos.

Para correr el programa solo se necesitan tener las librerias mencionadas instaladas y ejecutar el programa, en donde se mostrara una interfaz con las preguntas y las respuestas
para cada una de las rondas.

En el caso de la persistencia de los datos (el historico del jugador) se utilizo una base de datos No-relacional MongoDB, mas espceficicamente la base de datos online MongoAtlas,
para la cual si el programa tiene problemas con la conexión, intentar utilizar la siguiente URL para la conexión (esta ya viene integrada en el sistema pero por algun motivo no
carga o aparece por favor utilizarla):

CONNECTION_STRING = "mongodb+srv://Wizz:Gato123@wizzdatabase.8e9zq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

