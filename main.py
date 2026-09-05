import sys
from app.config.settings import settings
from app.usuarios.gestor import registrar_usuario, listar_usuarios, buscar_usuario

def mostrar_menu():
    print(f"\n{'='*30}")
    print(f"  {settings.APP_NAME} v{settings.APP_VERSION}")
    print(f"{'='*30}")
    print("1. Registrar nuevo usuario")
    print("2. Listar todos los usuarios")
    print("3. Buscar usuario por nombre")
    print("4. Ver configuración (Admin)")
    print("5. Salir")
    return input("\nSeleccione una opción: ")

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Ingrese nombre: ")
            try:
                edad = int(input("Ingrese edad: "))
                email = input("Ingrese email: ")
                resultado = registrar_usuario(nombre, edad, email)
                print(resultado)
            except ValueError:
                print("Error: La edad debe ser un número entero.")

        elif opcion == "2":
            print(listar_usuarios())

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            print(buscar_usuario(nombre))

        elif opcion == "4":
            print(f"\nConfiguración del Sistema:")
            print(f"- Administrador: {settings.ADMIN_USER}")
            print(f"- Modo Debug: {settings.DEBUG}")

        elif opcion == "5":
            print("Saliendo del sistema...")
            sys.exit()

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
