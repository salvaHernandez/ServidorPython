from Constantes import *
import conexionOO
import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api



################################### Probando conexión ####################################
conex = conexionOO.Conexion('root','','desafiopython')

app = Flask(__name__)
api = Api(app)

#------------------------------------------------------------------------------
@app.route('/')
def hello():
    return 'Hola holita'

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
@app.route("/usuario/<name>", methods=['GET']) #aquí especificamos la ruta para el endpoint.
def getPersona(name): #aquí declaramos una función que se llamará cuando se realice una request a esa url
    persona = conex.buscarUsuario(name)
    print(jsonify(persona))
    if (len(persona) != 0):
        resp = jsonify(persona)
        resp.status_code = 200
    else:
        respuesta = {'message': 'No se han extraido datos.'}
        resp = jsonify(respuesta)
        resp.status_code = 400
    print(resp)
    return resp


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
@app.route("/encuesta/<nombreEncuesta>", methods=['GET']) #aquí especificamos la ruta para el endpoint.
def getEstadoEnc(nombreEncuesta): #aquí declaramos una función que se llamará cuando se realice una request a esa url
    enc = conex.estadoEncuesta(nombreEncuesta)
    print(jsonify(enc))
    if (len(enc) != 0):
        resp = jsonify(enc)
        resp.status_code = 200
    else:
        respuesta = {'message': 'No se han extraido datos.'}
        resp = jsonify(respuesta)
        resp.status_code = 400
    print(resp)
    return resp


@app.route("/listaUsuarios", methods=['GET']) #aquí especificamos la ruta para el endpoint.
def getUsuarios(): #aquí declaramos una función que se llamará cuando se realice una request a esa url
    listaUsuarios = conex.listaUsuarios()
    if (len(listaUsuarios) != 0):
        resp = jsonify(listaUsuarios)
        resp.status_code = 200
    else:
        respuesta = {'message': 'No se han extraido datos.'}
        resp = jsonify(respuesta)
        resp.status_code = 400

    return resp


@app.route("/listaEncuestas", methods=['GET']) #aquí especificamos la ruta para el endpoint.
def getEncuestas(): #aquí declaramos una función que se llamará cuando se realice una request a esa url
    listaEnc = conex.listaEncuesta()
    if (len(listaEnc) != 0):
        resp = jsonify(listaEnc)
        resp.status_code = 200
    else:
        respuesta = {'message': 'No se han extraido datos.'}
        resp = jsonify(respuesta)
        resp.status_code = 400

    return resp


@app.route('/addEncuesta', methods=["POST"])
def encuestaRellenada():
    data = request.json
    if (conex.rellenarEncuesta(data[SERIE_O_PELI], data[SAGA_PREFERIDA], data[GENERO_FAV],
                              data[NUM_PELICULAS], data[ANIME], data[VALORACION_ENCUESTA], data[NOMRE_USU])):
        respuesta = {'message': 'OK.'}
        resp = jsonify(respuesta)
        resp.status_code = 200
    else:
        respuesta = {'message': 'Error.'}
        resp = jsonify(respuesta)
        resp.status_code = 400
    return resp



@app.route('/addUser', methods=["POST"])
def aniadirUsuario():
    data = request.json
    if (conex.registrarUsuario(data[NOMBRE_USUARIO], data[ID_ROL], data[PASS_USUARIO]) > 0):
        respuesta = {'message': 'OK.'}
        resp = jsonify(respuesta)
        resp.status_code = 200
    else:
        respuesta = {'message': 'El usuario ya existe.'}
        resp = jsonify(respuesta)
        resp.status_code = 400
    return resp



@app.route("/reiniciarEncuesta", methods=["DELETE"])
def delEncuesta():
    if conex.borrarRegistrosEncuesta() > 0:
        respuesta = {'message': 'Ok.'}
        resp = jsonify(respuesta)
        resp.status_code = 200
    else:
        respuesta = {'message': 'No se ha podido reiniciar la encuesta'}
        resp = jsonify(respuesta)
        resp.status_code = 400
    return resp


@app.route("/activarDesactivarEnc", methods=["PUT"])
def modAula():
    data = request.json
    print(data)
    if (conex.modificarEstadoEnc(data[NOMBRE_ENC], data[ENC_ACTIVADA]) > 0):
        respuesta = {'message': 'Ok.'}
        resp = jsonify(respuesta)
        resp.status_code = 200
    else:
        respuesta = {'message': 'Error al modificar.'}
        resp = jsonify(respuesta)
        resp.status_code = 400
    return resp



#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
@app.route("/user/<string:nombre>/<string:passs>")
def getUser(nombre,passs):
    persona = conex.buscarUsuario(nombre,passs)
    print(jsonify(persona))
    if (len(persona) != 0):
        resp = jsonify(persona)
        resp.status_code = 200
    else:
        respuesta = {'message': 'No se han extraido datos.'}
        resp = jsonify(respuesta)
        resp.status_code = 400
    print(resp)
    return resp



# Para montarlo en http normaleras.
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host= '0.0.0.0') #Esto sería para poder usar el móvil. No arrancaría el servicio en localhost sino en esa ip. También 0.0.0.0

