import libreria
while True:
    print("Menu de opciones ")
    print("1. Registrar")
    print("2. Reporte")
    print("3. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        print("Registro")

        nombres = input("Ingrese nombres: ")
        apellidos = input("Ingrese apellido: ")
        sueldo_hora = int(input("ingrese sueldo por hora : "))
        horas_trabajadas = int(input("Ingrese Horas trabajadas: "))
        tipo = ("Ingrese tipo de empleado: ")

        libreria.registrar_nuevo_empleado(
            nombres, apellidos, sueldo_hora, horas_trabajadas, tipo
        )

    if opcion == "2":
        print("Reporte")
        libreria.reporte()

    if opcion == "3":
        print("Gracias por todo")
        break

