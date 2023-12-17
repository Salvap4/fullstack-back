""" Edita pedidos.txt """
def guardar_pedido(nombre, apellidos):
    """ Edita pedidos.txt """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")
        file.close()
