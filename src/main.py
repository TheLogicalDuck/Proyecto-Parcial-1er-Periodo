import flet as ft


def main(page: ft.Page):
    page.title="El arte va en la artería"
    page.bgcolor=ft.Colors.BLUE_50
    
    pinturas = [
        {
            "titulo": "Pintrua1",
            "autor": "Autor1",
            "año": "año sin las comillas",
            "descripcion": "descripcion",
            "imagen":
        },
        {
            "titulo": "Pintrua2",
            "autor": "Autor2",
            "año": "año sin las comillas",
            "descripcion": "descripcion",
            "imagen":
        },
        {
            "titulo": "Pintrua3",
            "autor": "Autor3",
            "año": "año sin las comillas",
            "descripcion": "descripcion",
            "imagen":
        },
        {
            "titulo": "Pintrua4",
            "autor": "Autor4",
            "año": "año sin las comillas",
            "descripcion": "descripcion",
            "imagen":
        },
        {
            "titulo": "Pintrua45",
            "autor": "Autor45",
            "año": "año sin las comillas",
            "descripcion": "descripcion",
            "imagen":
        },
        {
            "titulo": "Pintrua5",
            "autor": "Autor5",
            "año": "año sin las comillas",
            "descripcion": "descripcion",
            "imagen":
        },
        {
            "titulo": "Pintrua6",
            "autor": "Autor6",
            "año": "año sin las comillas",
            "descripcion": "descripcion",
            "imagen":
        },
        {
            "titulo": "Pintrua7",
            "autor": "Autor7",
            "año": "año sin las comillas",
            "descripcion": "descripcion",
            "imagen":
        },
        {
            "titulo": "Pintrua8",
            "autor": "Autor8",
            "año": "año sin las comillas",
            "descripcion": "descripcion",
            "imagen":
        },
        {
            "titulo": "Pintrua9",
            "autor": "Autor9",
            "año": "año sin las comillas",
            "descripcion": "descripcion",
            "imagen":
        },
    ]
    
    indice_actual=[0]

    contenedor=ft.Containter(
        content=ft.Column([]),
        width=400,
        height=500,
        bgcolor=ft.Colors.BLUE_400,
        alignment=ft.alignment.center,
        padding=20
    )

    boton_siguiente=ft.ElevatedButton(text="Siguiente pintura")
    boton_siguiente=ft.ElevatedButton(text="Pintura anterior")

    def mostrar_pintura():
        pintura=pinturas[indice_actual[0]]
        contenedor.content=ft.Column([
            ft.Image(src=pintura["imagen"], width=300, height=300, fit=ft.ImageFit.CONTAIN),
            ft.Text(pintura["titulo"],size=20,weight=ft.FontWeight.BOLD),
            ft.Text(f"Autor: {pintura['autor']}",size=16),
            ft.Text(f"Año: {pintura['año']}",size=16),
            ft.Text(pintura["descripcion"],size=14,italic=True)
        ],alignment=ft.MainAxisAlignment.CENTER)
    
        if indice_actual[0]==len(pinturas)-1:
        boton_siguiente.text="Volver al inicio"
        else:
            boton_siguiente.text="Siguiente pintura"
        page.update()

    def siguiente_click(e):
        indice_actual[0]=(indice_actual[0]+1)%len(pinturas)
        mostrar_pintura()
    boton_siguiente.on_click=siguiente_click



    page.add(
        ft.Container(
            content=ft.Column([
                contenedor,
                boton_siguiente
            ],alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        ),
            alignment=ft.alignment.center,
            expand=True
        )
    )
    mostrar_pintura()


ft.app(main)