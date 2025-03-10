from flask import Flask, jsonify, request
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

cnx = mysql.connector.connect(host= os.getenv("MYSQL_ADDON_HOST"),
                              user=os.getenv("MYSQL_ADDON_USER"),
                              password=os.getenv("MYSQL_ADDON_PASSWORD"),
                              database=os.getenv("MYSQL_ADDON_DB"),
                              port = int(os.getenv("MYSQL_ADDON_PORT")),
                              )

app = Flask(__name__)

@app.route("/autos")
def show():
    
    with cnx.cursor() as cursor:
        query = ("SELECT * FROM autos")
        cursor.execute(query)
        resp = [i for i in cursor.fetchall()]
        
    return jsonify({"Resp":resp}) 

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    with cnx.cursor() as cursor:
        nombre = data["nombre"]
        marca = data["marca"]
        cursor.execute("INSERT INTO autos (nombre, marca) VALUES (%s,%s)",(nombre, marca))
        cnx.commit()
        return jsonify({"msg":"Auto añadido correctamente"})
    
@app.route("/edit/<string:id>", methods=["PUT"])
def editar(id):
    with cnx.cursor() as cursor:
        
        data = request.get_json()
        nombre = data["nombre"]
        marca = data["marca"]
        if nombre and marca:
            cursor.execute("UPDATE autos SET nombre=%s, marca=%s WHERE id = %s",(nombre, marca,id))
            cnx.commit()
            return jsonify({"actualizado":"Correctamente"})
    
@app.route("/delete/<string:id>", methods=["DELETE"])
def delete(id):
    with cnx.cursor() as cursor:
        cursor.execute("DELETE FROM autos WHERE id = %s",(id,))
        cnx.commit()
        return jsonify({"mensaje":"Coche borrado"})

if __name__ == "__main__":
    app.run(debug=True)