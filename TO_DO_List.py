def afiseaza_meniu():
    print("\n==== Meniu Task-uri ====")
    print("1 - Adauga task")
    print("2 - Afiseaza toate task-urile")
    print("3 - Sterge un task")
    print("4 - Marcheaz un task ca facut")
    print("5 - Iesire")


def adauga_task():
    text = input("Scrie task-ul: ")
    task = {"text": text, "status": False}
    taskuri.append(task)
    print("Task adaugat co succes!")


def afiseaza_taskuri():
    if not taskuri:
        print("Nu exista task-ri momentan")
        return
    print("\n==== Lista de task-uri ====")
    for i, task in enumerate(taskuri, start=1):
        simbol = "[x]" if task["status"] else "[]"
        print(f"{i}. {simbol} {task['text']}")


def sterge_task():
    afiseaza_taskuri()

    try:
        nr = int(input("Introdu numarul taskului de sters: "))
        if nr < 1 or nr > len(taskuri):
            print("Numar invalid!")
            return
        task_sters = taskuri.pop(nr - 1)
        print(f"Task sters: {task_sters['text']}")
    except ValueError:
        print("Trebuie sa introduci un numar!")


def marcheaza_task():
    afiseaza_taskuri()

    try:
        nr = int(input("Introdu numarul taskului de marcat ca facut: "))
        if nr < 1 or nr > len(taskuri):
            print("Numar invalid!")
            return
        taskuri[nr - 1]["status"] = True
        print(f"Task marcat ca facut: {taskuri[nr - 1]['text']}")
    except ValueError:
        print("Trebuie sa introduci un numar!")


taskuri = []

while True:
    afiseaza_meniu()
    optiune = input("Alege o optiune: ")

    if optiune == "1":
        adauga_task()
    elif optiune == "2":
        afiseaza_taskuri()
    elif optiune == "3":
        sterge_task()
    elif optiune == "4":
        marcheaza_task()
    elif optiune == "5":
        print("La revedere!")
        break
    else:
        print("Optiune invalida!")

