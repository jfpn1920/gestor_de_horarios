horarios = {
    "lunes": [],
    "martes": [],
    "miercoles": [],
    "jueves": [],
    "viernes": [],
    "sabado": [],
    "domingo": []
}
def agregar_actividad():
    dia = input("ingrese el dia de la semana: ").capitalize().strip()
    if dia not in horarios:
        print("dia invalido, intente nuevamente.")
        return
    actividad = input("ingrese la actividad: ").strip()
    horarios[dia].append(actividad)
    print(f"actividad '{actividad}' agregada al {dia}.")
def mostrar_horario():
    print("\n horario completo:")
    for dia, actividades in horarios.items():
        print(f"{dia}:")
        if actividades:
            for i, act in enumerate(actividades, 1):
                print(f"  {i}. {act}")
        else:
            print("no hay actividades registradas.")
def menu():
    while True:
        print("\n gestor de horarios ")
        print("1. agregar actividad")
        print("2. mostrar horario completo")
        print("3. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            agregar_actividad()
        elif opcion == "2":
            mostrar_horario()
        elif opcion == "3":
            print("saliendo del gestor de horarios.")
            break
        else:
            print("opcion invalida, intente nuevamente.")
menu()