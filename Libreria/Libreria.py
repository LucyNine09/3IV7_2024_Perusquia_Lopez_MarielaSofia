import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import random

ARCHIVO = "datos.txt"
libros = []

# Cargar datos desde el archivo
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) >= 7:
                    isbn = partes[0]
                    titulo = partes[1]
                    autor = partes[2]
                    editorial = partes[3]
                    año_publicacion = partes[4]
                    genero = partes[5]
                    precio = float(partes[6])
                    
                    libro = {
                        "ISBN": isbn,
                        "Título": titulo,
                        "Autor": autor,
                        "Editorial": editorial,
                        "Año": año_publicacion,
                        "Género": genero,
                        "Precio": precio
                    }
                    libros.append(libro)

# Guardar datos en el archivo
def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for libro in libros:
            f.write(f"{libro['ISBN']},{libro['Título']},{libro['Autor']},{libro['Editorial']},{libro['Año']},{libro['Género']},{libro['Precio']}\n")

# Generar un código ISBN automáticamente
def generar_isbn():
    isbn = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    messagebox.showinfo("ISBN Generado", f"ISBN generado: {isbn}")
    return isbn

# Función para validar entradas
def validar_entrada(texto, campo):
    if not texto:
        messagebox.showerror("Error", f"El campo '{campo}' no puede estar vacío.")
        return False
    return True

# Registrar un nuevo libro
def registrar_libro():
    # Crear ventana de registro
    registro_ventana = tk.Toplevel()
    registro_ventana.title("Registrar Libro")

    isbn_var = tk.StringVar()

    # Función para asignar el ISBN generado al campo
    def asignar_isbn():
        isbn_var.set(generar_isbn())

    tk.Label(registro_ventana, text="ISBN:").grid(row=0, column=0, padx=5, pady=5)
    isbn_entry = tk.Entry(registro_ventana, textvariable=isbn_var)
    isbn_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(registro_ventana, text="Generar ISBN", command=asignar_isbn).grid(row=0, column=2, padx=5, pady=5)

    titulo_var = tk.StringVar()
    tk.Label(registro_ventana, text="Título:").grid(row=1, column=0, padx=5, pady=5)
    tk.Entry(registro_ventana, textvariable=titulo_var).grid(row=1, column=1, padx=5, pady=5)

    autor_var = tk.StringVar()
    tk.Label(registro_ventana, text="Autor:").grid(row=2, column=0, padx=5, pady=5)
    tk.Entry(registro_ventana, textvariable=autor_var).grid(row=2, column=1, padx=5, pady=5)

    editorial_var = tk.StringVar()
    tk.Label(registro_ventana, text="Editorial:").grid(row=3, column=0, padx=5, pady=5)
    tk.Entry(registro_ventana, textvariable=editorial_var).grid(row=3, column=1, padx=5, pady=5)

    año_var = tk.StringVar()
    tk.Label(registro_ventana, text="Año de Publicación:").grid(row=4, column=0, padx=5, pady=5)
    tk.Entry(registro_ventana, textvariable=año_var).grid(row=4, column=1, padx=5, pady=5)

    genero_var = tk.StringVar()
    tk.Label(registro_ventana, text="Género:").grid(row=5, column=0, padx=5, pady=5)
    tk.Entry(registro_ventana, textvariable=genero_var).grid(row=5, column=1, padx=5, pady=5)

    precio_var = tk.StringVar()
    tk.Label(registro_ventana, text="Precio:").grid(row=6, column=0, padx=5, pady=5)
    tk.Entry(registro_ventana, textvariable=precio_var).grid(row=6, column=1, padx=5, pady=5)

    # Función para registrar el libro
    def guardar_libro():
        isbn = isbn_var.get()
        titulo = titulo_var.get()
        autor = autor_var.get()
        editorial = editorial_var.get()
        año = año_var.get()
        genero = genero_var.get()
        try:
            precio = float(precio_var.get())
            if precio < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número positivo.")
            return

        libro = {
            "ISBN": isbn,
            "Título": titulo,
            "Autor": autor,
            "Editorial": editorial,
            "Año": año,
            "Género": genero,
            "Precio": precio
        }

        libros.append(libro)
        guardar_datos()
        messagebox.showinfo("Éxito", "Libro registrado exitosamente")
        registro_ventana.destroy()

    tk.Button(registro_ventana, text="Guardar", command=guardar_libro).grid(row=7, column=1, pady=10)

# Consultar libros
def consultar_libros():
    consulta_ventana = tk.Toplevel()
    consulta_ventana.title("Consultar Libros")

    # Crear lista de libros
    lista_libros = tk.Listbox(consulta_ventana, width=100, height=20)
    lista_libros.pack(padx=10, pady=10)

    # Función para mostrar todos los libros
    def mostrar_libros():
        lista_libros.delete(0, tk.END)
        for libro in libros:
            texto = f"ISBN: {libro['ISBN']}, Título: {libro['Título']}, Autor: {libro['Autor']}, Editorial: {libro['Editorial']}, Año: {libro['Año']}, Género: {libro['Género']}, Precio: {libro['Precio']}"
            lista_libros.insert(tk.END, texto)

    # Buscar libro por ISBN o título
    def buscar_libro():
        termino = simpledialog.askstring("Buscar", "Ingrese el ISBN o Título del libro:")
        lista_libros.delete(0, tk.END)
        for libro in libros:
            if termino in libro['ISBN'] or termino.lower() in libro['Título'].lower():
                texto = f"ISBN: {libro['ISBN']}, Título: {libro['Título']}, Autor: {libro['Autor']}, Editorial: {libro['Editorial']}, Año: {libro['Año']}, Género: {libro['Género']}, Precio: {libro['Precio']}"
                lista_libros.insert(tk.END, texto)

    # Botones para mostrar y buscar libros
    tk.Button(consulta_ventana, text="Mostrar Todos", command=mostrar_libros).pack(pady=5)
    tk.Button(consulta_ventana, text="Buscar", command=buscar_libro).pack(pady=5)

# Actualizar libro
def actualizar_libro():
    actualizar_ventana = tk.Toplevel()
    actualizar_ventana.title("Actualizar Libro")

    # Buscar libro por ISBN
    isbn = simpledialog.askstring("Buscar", "Ingrese el ISBN del libro a actualizar:")
    libro_encontrado = next((libro for libro in libros if libro['ISBN'] == isbn), None)

    if not libro_encontrado:
        messagebox.showerror("Error", "Libro no encontrado.")
        actualizar_ventana.destroy()
        return

    # Crear campos de entrada para actualizar datos
    campos = ['Título', 'Autor', 'Editorial', 'Año', 'Género', 'Precio']
    entradas = {}
    fila = 0
    for campo in campos:
        tk.Label(actualizar_ventana, text=f"{campo}:").grid(row=fila, column=0, padx=5, pady=5)
        var = tk.StringVar(value=libro_encontrado[campo])
        entradas[campo] = var
        tk.Entry(actualizar_ventana, textvariable=var).grid(row=fila, column=1, padx=5, pady=5)
        fila += 1

    # Guardar cambios
    def guardar_cambios():
        for campo in campos:
            libro_encontrado[campo] = entradas[campo].get()

        # Validar Precio
        try:
            precio = float(libro_encontrado['Precio'])
            if precio < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número positivo")
            return

        guardar_datos()
        messagebox.showinfo("Éxito", "Libro actualizado exitosamente.")
        actualizar_ventana.destroy()

    tk.Button(actualizar_ventana, text="Guardar Cambios", command=guardar_cambios).grid(row=fila, columnspan=2, pady=10)

# Borrar libro
def borrar_libro():
    isbn = simpledialog.askstring("Buscar", "Ingrese el ISBN del libro a borrar:")
    libro_encontrado = next((libro for libro in libros if libro['ISBN'] == isbn), None)

    if not libro_encontrado:
        messagebox.showerror("Error", "Libro no encontrado.")
        return

    # Confirmar eliminación
    if messagebox.askyesno("Confirmar", f"¿Está seguro de borrar el libro '{libro_encontrado['Título']}'?"):
        libros.remove(libro_encontrado)
        guardar_datos()
        messagebox.showinfo("Éxito", "Libro borrado exitosamente.")

# Menú principal
def main():
    cargar_datos()
    ventana = tk.Tk()
    ventana.title("Gestión de Biblioteca")
    ventana.geometry("300x200")
    
    tk.Button(ventana, text="Registrar Libro", command=registrar_libro).pack(pady=10)
    tk.Button(ventana, text="Consultar Libros", command=consultar_libros).pack(pady=10)
    tk.Button(ventana, text="Actualizar Libro", command=actualizar_libro).pack(pady=10)
    tk.Button(ventana, text="Borrar Libro", command=borrar_libro).pack(pady=10)
    tk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=10)
    
    ventana.mainloop()

main()
