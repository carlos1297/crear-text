nuevas_notas = {
    "messi" : 45,
     "carlos" : 23,
     "nexxuz" :53,   
      "hola" : 46
}

with open("datos_de_alumnos.txt", "a") as archivo:
    for nombre, notas in nuevas_notas.items():
        archivo.write(nombre + " - " + str(notas) + "\n")
