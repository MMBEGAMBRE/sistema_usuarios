def validar_nombre(nombre: str) -> bool:
    """Valida que el nombre no esté vacío y tenga al menos 3 caracteres."""
    if not nombre or len(nombre.strip()) < 3:
        raise ValueError("El nombre no puede estar vacío y debe tener al menos 3 caracteres.")
    return True

def validar_edad(edad: int) -> bool:
    """Valida que la edad sea un número positivo razonable."""
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    if edad > 120:
        raise ValueError("Por favor, ingrese una edad válida.")
    return True
