import flet as ft
from dicas import dicas_page
from treino import treino_page
from video import video_page

def main(page: ft.Page):
    page.title = "Bem-vindo ao Clan"
    page.window_width = 650
    page.window_height = 550
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change(route):
        page.views.clear()

        routes = {
            "/dicas": dicas_page,
            "/treino": treino_page,
            "/video": video_page
        }

        if page.route in routes:
            routes[page.route](page)
        else:
            # Tela inicial
            page.views.append(
                ft.View(
                    "/",
                    controls=[
                        ft.Stack(
                            [
                                ft.Container(
                                    content=ft.Image(
                                        src="src/assets/fundo.png",
                                        fit=ft.ImageFit.COVER
                                    ),
                                    expand=True
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                "Bem-vindo ao App de Treino!", 
                                                size=24, 
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.RED_100,
                                                text_align=ft.TextAlign.CENTER
                                            ),
                                            ft.Column(  # Ícones organizados verticalmente
                                                [
                                                    create_icon_button("Dicas", ft.icons.BOOK, "/dicas"),
                                                    create_icon_button("Treino", ft.icons.FITNESS_CENTER, "/treino"),
                                                    create_icon_button("Vídeos", ft.icons.VIDEO_COLLECTION, "/video"),
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                    expand=True
                                )
                            ],
                            expand=True
                        )
                    ]
                )
            )
        page.update()

    def create_icon_button(label, icon, route):
        """Cria os botões da tela inicial organizados verticalmente."""
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(icon, size=50),  # Ícones um pouco maiores para mobile
                    ft.Text(label, size=22)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            margin=10,
            padding=15,
            width=180,  # Largura maior para toque mais fácil em mobile
            height=180,
            border_radius=15,
            ink=True,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.with_opacity(0.3, ft.Colors.BLACK),
            on_click=lambda _: page.go(route)
        )

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)



# import flet as ft
# from dicas import dicas_page
# from treino import treino_page
# from video import video_page

# def main(page: ft.Page):
#     page.title = "Bem vindo ao Clan"
#     page.window_width = 360
#     page.window_height = 640
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

#     def route_change(route):
#         page.views.clear()
        
#         # Tela inicial
#         if page.route == "/":
#             page.views.append(
#                 ft.View(
#                     "/",
#                     [
#                         ft.Stack(
#                             [
#                                 ft.Container(
#                                     content=ft.Image(
#                                         src="src/assets/fundo.png",
#                                         fit=ft.ImageFit.COVER,
                                        
#                                     ),
#                                     expand=True
#                                 ),
#                                 ft.Column(
#                                     [
#                                         ft.Text("Bem-vindo ao App de Treino!", 
#                                                 size=24, 
#                                                 weight=ft.FontWeight.BOLD,
#                                                 color=ft.Colors.RED_100),
#                                         ft.Column(
#                                             [
#                                                 ft.Container(
#                                                     content=ft.Column(
#                                                         [
#                                                             ft.Icon(ft.icons.BOOK, size=40),
#                                                             ft.Text("Dicas", size=20)
#                                                         ],
#                                                         alignment=ft.MainAxisAlignment.CENTER,
#                                                         horizontal_alignment=ft.CrossAxisAlignment.CENTER
#                                                     ),
#                                                     margin=10,
#                                                     padding=10,
#                                                     width=140,
#                                                     height=140,
#                                                     border_radius=10,
#                                                     ink=True,
#                                                     alignment=ft.alignment.center,
#                                                     bgcolor=ft.colors.with_opacity(0.3, ft.Colors.BLACK),
#                                                     on_click=lambda _: page.go("/dicas")
#                                                 ),
#                                                 ft.Container(
#                                                     content=ft.Column(
#                                                         [
#                                                             ft.Icon(ft.icons.FITNESS_CENTER, size=40),
#                                                             ft.Text("Treino", size=20)
#                                                         ],
#                                                         alignment=ft.MainAxisAlignment.CENTER,
#                                                         horizontal_alignment=ft.CrossAxisAlignment.CENTER
#                                                     ),
#                                                     margin=10,
#                                                     padding=10,
#                                                     width=140,
#                                                     height=140,
#                                                     border_radius=10,
#                                                     ink=True,
#                                                     alignment=ft.alignment.center,
#                                                     bgcolor=ft.colors.with_opacity(0.3, ft.Colors.BLACK),
#                                                     on_click=lambda _: page.go("/treino")
#                                                 ),
#                                                 ft.Container(
#                                                     content=ft.Column(
#                                                         [
#                                                             ft.Icon(ft.icons.VIDEO_COLLECTION, size=40),
#                                                             ft.Text("Vídeos", size=20)
#                                                         ],
#                                                         alignment=ft.MainAxisAlignment.CENTER,
#                                                         horizontal_alignment=ft.CrossAxisAlignment.CENTER
#                                                     ),
#                                                     margin=10,
#                                                     padding=10,
#                                                     width=140,
#                                                     height=140,
#                                                     border_radius=10,
#                                                     ink=True,
#                                                     alignment=ft.alignment.center,
#                                                     bgcolor=ft.colors.with_opacity(0.3, ft.Colors.BLACK),
#                                                     on_click=lambda _: page.go("/video")
#                                                 )
#                                             ],
#                                             alignment=ft.MainAxisAlignment.CENTER
#                                         )
#                                     ],
#                                     alignment=ft.MainAxisAlignment.CENTER,
#                                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                                     expand=True
#                                 )
#                             ],
#                             expand=True
#                         )
#                     ],
#                     expand=True
#                 )
#             )
        
#         # Telas secundárias
#         elif page.route == "/dicas":
#             dicas_page(page)
#         elif page.route == "/treino":
#             treino_page(page)
#         elif page.route == "/video":
#             video_page(page)

#         page.update()

#     page.on_route_change = route_change
#     page.go("/")

# ft.app(target=main)

