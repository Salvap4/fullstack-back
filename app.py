""" Guardar datos enviados por el usuario """
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/pizza", methods=['POST'])
def pizza():
    """ Recoge datos enviados por el usuario """
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    nacimiento = request.form.get("nacimiento")
    direccion = request.form.get("direccion")
    tamano = request.form.get("tamaño")
    i1 = request.form.get("i1")
    i2 = request.form.get("i2")
    i3 = request.form.get("i3")
    i4 = request.form.get("i4")

    # Mostramos los resultados en la consola Python
    print("-----DATOS DEL CLIENTE-----")
    print("Nombre: "+nombre)
    print("Apellidos: "+apellidos)
    print("Fecha de nacimiento: "+nacimiento)
    print("Dirección postal: "+direccion)

    print("-----DATOS DEL PEDIDO-----")
    print("Tamaño de la pizza: "+tamano)

    if i1 is None:
        check_i1 = "NO"
    else:
        check_i1 = "SÍ"
    print("Jamón York: " +check_i1)

    if i2 is None:
        check_i2 = "NO"
    else:
        check_i2 = "SÍ"
    print("Champiñones: " +check_i2)

    if i3 is None:
        check_i3 = "NO"
    else:
        check_i3 = "SÍ"
    print("Pepperoni: " +check_i3)

    if i4 is None:
        check_i4 = "NO"
    else:
        check_i4 = "SÍ"
    print("Aceitunas: " +check_i4)


    # Mostramos los resultados en el archivo "pedidos.txt"
    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()

    guardar_pedido1(nombre, apellidos, nacimiento)
    guardar_pedido2(direccion, tamano, check_i1)
    guardar_pedido3(check_i2, check_i3, check_i4)


    return redirect("http://localhost/solicita_pedido.html", code=302)

def guardar_pedido1(nombre, apellidos, nacimiento):
    """ Escribe en pedidos.txt los datos enviados por el ususario """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-----DATOS DEL CLIENTE-----\n")
        file.write("Nombre: " +nombre+ "\n")
        file.write("Apellidos : " +apellidos+ "\n")
        file.write("Nacimiento: " +nacimiento+ "\n")
        file.close()

def guardar_pedido2(direccion, tamano, i1):
    """ Escribe en pedidos.txt los datos enviados por el ususario """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("Dirección postal: " +direccion+ "\n")
        file.write("-----DATOS DEL PEDIDO-----\n")
        file.write("Tamño de la pizza: " +tamano+ "\n")
        file.write("Jamón York: " +i1+ "\n")
        file.close()

def guardar_pedido3(i2, i3, i4):
    """ Escribe en pedidos.txt los datos enviados por el ususario """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("Champiñones: " +i2+ "\n")
        file.write("Pepperoni: " +i3+ "\n")
        file.write("Aceitunas: " +i4+ "\n")
        file.close()
