from .validaciones import validar_nombre, validar_edad

# Lista en memoria para simular base de datos
usuarios = []

def registrar_usuario(nombre: str, edad: int, email: str):
    """Registra un nuevo usuario tras validar los datos."""
    try:
        validar_nombre(nombre)
        validar_edad(edad)

        nuevo_usuario = {
            "nombre": nombre.strip(),
            "edad": edad,
            "email": email.strip()
        }
        usuarios.append(nuevo_usuario)
        return f"Usuario '{nombre}' registrado exitosamente."
    except ValueError as e:
        return f"Error en el registro: {e}"

def listar_usuarios():
    """Retorna la lista de todos los usuarios."""
    if not usuarios:
        return "No hay usuarios registrados actualmente."

    output = "\nLista de Usuarios\n"
    for i, user in enumerate(usuarios, 1):
        output += f"{i}. Nombre: {user['nombre']} | Edad: {user['edad']} | Email: {user['email']}\n"
    return output

def buscar_usuario(nombre_busqueda: str):
    """Busca usuarios que coincidan parcialmente con el nombre."""
    resultados = [u for u in usuarios if nombre_busqueda.lower() in u['nombre'].lower()]

    if not resultados:
        return f"No se encontraron usuarios que coincidan con '{nombre_busqueda}'."

    output = f"\nResultados para '{nombre_busqueda}':\n"
    for user in resultados:
        output += f"Nombre: {user['nombre']} ({user['email']})\n"
    return output
