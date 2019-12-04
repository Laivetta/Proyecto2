from flask import Flask, render_template, request, redirect, url_for
from calculoscuotas import calculo_cuota


"""
request me va  permitir tomar los datos que vinen de los formularios html por post o get
"""

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Cliente

# Connect to Database and create database session
engine = create_engine('sqlite:///proyecto.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



@app.route('/')
@app.route("/clientes", methods=["GET", "POST"])
def inicio():
    """ se crea la variable cleente en donde se guarda la consulta a la base de datos
        despues en el return se crea la variable clientes y se le da el mismo valor que cliente
        y clientes es pasado a la pagina inicio.html para poder ser trabajado ahi
        en el query Cliente es el nombre de la clase, y dentro de la clase esta el nombre
        de la tabla cliente y dentro de la tabla cada una de las columnas
    """
    cliente = session.query(Cliente).all()
    return render_template("inicio.html", clientes=cliente)


@app.route("/nuevocliente", methods=['GET', 'POST'])
def nuevocliente():
        if request.form:
            nuevocliente = Cliente(nombres=request.form.get("nombres"), 
                       apellidos=request.form.get("apellidos"),
                       dni=request.form.get("dni"),
                       #aca estoy poniendo un valor no proveniente del formulario
                       #sino que calculado por mi y despues le agregue el valor del campo
                       cuota=calculo_cuota(15000, 0.09, 33))

            session.add(nuevocliente)
            session.commit()
            return redirect (url_for('inicio'))
        return render_template("nuevocliente.html")
       

@app.route ("/clientes/<int:cliente_id>/borrarcliente", methods=['GET', 'POST'])
def borrarcliente(cliente_id):
    resultadoconsulta = session.query(Cliente).filter_by(id=cliente_id).one()
    #aca estoy filtrando por <int:cliente_id>/ en la consulta 
    nombre = resultadoconsulta.nombres
    apellido = resultadoconsulta.apellidos
    #aca estoy individualizando a quien voy a borrar, lo voy a mostrar antes de borrar
    if request.method == 'POST':
       session.delete(resultadoconsulta)
       session.commit()
       return redirect (url_for('inicio', cliente=resultadoconsulta))
    return render_template("borrarcliente.html", cliente_id=cliente_id, nombre=nombre, apellido=apellido)
# Cliente es la clase, cliente_id es el campo del decorador
#clienteparaborrar es la recuperacion de la consulta sql
# 

@app.route("/clientes/<int:cliente_id>/actualizarcliente", methods=['GET', 'POST'])
def actualizarcliente(cliente_id):
    #aca estoy filtrando por <int:cliente_id>/ en la consulta 
    resultadoconsulta = session.query(Cliente).filter_by(id=cliente_id).one()
    
    
    #creo las variables con los datos de las consultas
    a= resultadoconsulta.nombres
    apellidos_consulta= resultadoconsulta.apellidos
    dni_consulta= resultadoconsulta.dni
    
    

    #aca estoy pidiendo nuevamente los datos del formulario para actualizar la base de datos
    #con esto accedo a lo enviado por el formulario y accedo a los campos nombre, apellidos, etc
    
    if request.form:
            #obtengo los datos del formulario
            nombres=request.form.get("nombres")
            apellidos=request.form.get("apellidos")
            dni=request.form.get("dni")
            
            #asigno los datos del formulario a los campos de la base de datos
            resultadoconsulta.nombres=nombres
            resultadoconsulta.apellidos=apellidos
            resultadoconsulta.dni=dni
            
            #grabo en la base de datos
            session.commit()
            return redirect (url_for('inicio'))
    return render_template("actualizarcliente.html", cliente_id=cliente_id, nombres_consulta=a, apellidos_consulta=apellidos_consulta, dni_consulta=dni_consulta)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)