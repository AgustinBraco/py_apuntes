# Tema: “Gestor de tareas (CLI o consola)”
# Objetivo: Crear un programa de consola que permita gestionar tareas pendientes.

# Requisitos:
## Las tareas deben tener:
## ID (autoincremental)
## Título
## Descripción
## Estado (pendiente, en progreso, completada)
## Fecha de creación

# Funcionalidades mínimas:
## Agregar una tarea
## Listar todas las tareas
## Cambiar el estado de una tarea
## Eliminar una tarea


import datetime

# Lista para guardar las tareas
tasks = []

# Estados disponibles
statuses = ["pendiente", "en progreso", "completada"]

# Contador para el ID autoincremental
id_counter = 1

# Validar si hay tareas
def is_empty():
    if tasks:
        return False
    else:
        print("\nNo hay tareas.\n")
        return True
    


# Función para agregar tarea
def add_task():
    global id_counter

    title = input("Ingrese el título de la tarea: ")
    description = input("Ingrese la descripción de la tarea: ")
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    task = {
        "ID": id_counter,
        "Título": title,
        "Descripción": description,
        "Estado": "pendiente",
        "Fecha de creación": created_at
    }

    tasks.append(task)
    id_counter += 1

    print(f"Tarea agregada.\n")
    

# Función para listar tareas
def list_tasks():
    if is_empty():
        return

    for task in tasks:
        print("----------")
        for key, value in task.items():
            print(f"{key}: {value}")
        print("----------")
    return

# Función para cambiar estado
def update_status():
    if is_empty():
        return

    task_id = int(input("Ingrese el ID de la tarea que quiere actualizar: "))

    for task in tasks:
        if task["ID"] != task_id:
            continue
        
        print(f"Estados disponibles: {statuses}")
        new_status = input("Ingrese el nuevo estado: ").lower()

        if new_status not in statuses:
            print("Estado inválido.\n")
            return
        
        task["Estado"] = new_status
        print("Estado actualizado correctamente.\n")
        return

    print("Tarea no encontrada.\n")
    return

# Función para eliminar tarea
def delete_task():
    if is_empty():
        return
        
    task_id = int(input("Ingrese el ID de la tarea que quiere eliminar: "))

    for task in tasks:
        if task["ID"] == task_id:
            tasks.remove(task)
            print("Tarea eliminada correctamente.\n")
            return

    print("Tarea no encontrada.\n")
    return

# Función para ejecutar el script
def run():
    while True:
        print("--- Gestor de tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Cambiar estado de tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        option = input("\nSeleccione una opción: ")

        if option == "1":
            add_task()
        elif option == "2":
            list_tasks()
        elif option == "3":
            update_status()
        elif option == "4":
            delete_task()
        elif option == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.\n")

# Ejecutar script
run()