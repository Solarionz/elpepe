def menu():
    print("Bienvenido al menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("Has seleccionado la opción 1.")
        # Aquí puedes colocar el código correspondiente a la opción 1

    elif opcion == "2":
        print("Has seleccionado la opción 2.")
        # Aquí puedes colocar el código correspondiente a la opción 2

    elif opcion == "3":
        print("Has seleccionado la opción 3.")
        # Aquí puedes colocar el código correspondiente a la opción 3

    elif opcion == "4":
        print("Saliendo del programa...")
        return

    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
        menu()

menu()
