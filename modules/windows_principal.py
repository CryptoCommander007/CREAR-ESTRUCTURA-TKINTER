import tkinter as tk
from modules.functions import (
    obtener_y_guardar_html,
    filtrar_archivo,
    limpiar_href,
    limpiar_y_guardar,
    cargar_rutas,
    mostrar_mensaje,
    eliminar_lineas_duplicadas
)

def listar_rutas():
    archivo = 'modules/rutas.txt'
    url = url_entry.get()
    if url:
        with open(archivo, 'a+') as file:
            file.write(url + '\n')
        print("Ruta creada: " + url)  # Mensaje de ruta creada
        url_entry.delete(0, tk.END)
        mostrar_mensaje("Ruta agregada")  # Mostrar ventana emergente con el mensaje
        
        # Obtener y guardar HTML
        obtener_y_guardar_html(url, 'archivo_html.html')
        
        # Filtrar archivo HTML y guardar las líneas filtradas temporalmente
        lineas_filtradas = filtrar_archivo('archivo_html.html')
        with open('salida_filtrada_a_href_videos.html', 'w', encoding='utf-8') as file:
            file.writelines(lineas_filtradas)
        
        # Limpiar href del archivo filtrado
        hrefs = limpiar_href('salida_filtrada_a_href_videos.html')
        
        # Guardar los hrefs en un archivo temporal para limpiar y guardar
        with open('href_salida.txt', 'w', encoding='utf-8') as file:
            for href in hrefs:
                file.write(href + '\n')
        
        # Limpiar y guardar las rutas finales
        lineas_limpias = limpiar_y_guardar('href_salida.txt')
        with open('rutas_finales.txt', 'w', encoding='utf-8') as file:
            for linea in lineas_limpias:
                file.write(linea + '\n')
        
        # Eliminar líneas duplicadas en el archivo final
        eliminar_lineas_duplicadas('rutas_finales.txt')

        print("Proceso completado. Las rutas finales se han guardado en 'rutas_finales.txt'.")
    else:
        print("Por favor ingrese una URL.")

    rutas = cargar_rutas(archivo)
    for ruta in rutas:
        print(ruta.strip())

def descargar_archivo():
    # Aquí irá la lógica para descargar el archivo desde la URL
    pass

def main():
    root = tk.Tk()
    root.title("Mi Proyecto Tkinter")
    root.geometry("800x600")
    # Evitar que la ventana se agrande
    root.resizable(width=False, height=False)

    # Establecer color de fondo para la ventana
    root.configure(bg="#f0f0f0")  # Gris claro

    # Campo de entrada para la URL
    global url_entry
    url_entry = tk.Entry(root, width=80, bg="#AAA100", bd=2, relief=tk.GROOVE, font=("Arial", 12))  # Ajusta el ancho, alto, color de fondo, borde, relieve y fuente del campo de entrada
    url_entry.grid(row=0, column=0, pady=10, padx=20)
    # Botón para listar
    listar_btn = tk.Button(root, text="Listar", command=listar_rutas, width=80, height=2)  # Ajusta el ancho y largo del botón
    listar_btn.grid(row=1, column=0, pady=10 , padx=120)

    # Botón para descargar
    descargar_btn = tk.Button(root, text="Descargar", width=80, height=2)  # Ajusta el ancho y largo del botón
    descargar_btn.grid(row=2, column=0, pady=10, padx=120)

    root.mainloop()

if __name__ == "__main__":
    main()
