import flet as ft


def main(page: ft.Page):
    page.title="El arte va en la artería"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor=ft.Colors.BLACK
    
    pinturas = [
        {
            "titulo": "El Lógico",
            "autor": "TheLogicalDuck",
            "año": "2025",
            "descripcion": "La foto de perfil del pato logístico",
            "imagen": "src/assets/EL LOGICAL.png"
        },
        {
            "titulo": "Ojitos Wolsom",
            "autor": "Anónimo",
            "año": "2022",
            "descripcion": "Pintura que describe el miedo que puede sentir una persona sensible",
            "imagen": "src/assets/ojitos wolsom.png"
        },
        {
            "titulo": "Los pollos",
            "autor": "(Desconocido en Facebook)",
            "año": "2024",
            "descripcion": "Yo viendo como giran los pollos",
            "imagen": "src/assets/lospoyos.png"
        },
        {
            "titulo": "El de las recargas",
            "autor": "El.perrocalentero",
            "año": "2022",
            "descripcion": "Will Smith como el de las recargas",
            "imagen": "src/assets/recargas.png"
        },
        {
            "titulo": "Whatsapp",
            "autor": "Scorpion87",
            "año": "2007",
            "descripcion": "Photoshop de un carro de whatsapp",
            "imagen": "src/assets/wasap.png"
        },
        {
            "titulo": "Frutiger Gordon",
            "autor": "Frutiger Aereo: Aesthetics+",
            "año": "2025",
            "descripcion": "descripcion",
            "imagen": "src/assets/gordon.png"
        },
        {
            "titulo": "Meowl",
            "autor": "zhumaokele",
            "año": "2013",
            "descripcion": "Photoshop de un búho con cabeza de gato",
            "imagen": "src/assets/meowl.png"
        },
        {
            "titulo": "Cuarta transformación",
            "autor": "eldeforma",
            "año": "2019",
            "descripcion": "La transformación Super Saiyajin 4 de nuestro señor salvador AMLO",
            "imagen": "src/assets/cuarta.png"
        },
        {
            "titulo": "Factory",
            "autor": "Animan Studios",
            "año": "2021",
            "descripcion": "Get it together - Mustard on the beat, hoe",
            "imagen": "src/assets/animan.png"
        },
        {
            "titulo": "Recortalte",
            "autor": "Gentleman's barber shop",
            "año": "2023",
            "descripcion": "El chico quiere cambiar su estilo punk, por un ponkpadu",
            "imagen": "src/assets/enlaferia.png"
        },
    ]
    
    indice_actual=[0]

    contenedor=ft.Container(
        content=ft.Column([]),
        width=300,
        height=500,
        bgcolor=ft.Colors.BLACK,
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