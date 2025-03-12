import flet as ft

def main(page: ft.Page):
    page.title = "App de Treino"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def open_link(url):
        page.launch_url(url)
    
    btn_dicas = ft.ElevatedButton("Dicas", on_click=lambda _: open_link("https://www.youtube.com/watch?v=wFtMbchQSNs"))  # Substitua '#' pelo link do PDF
    btn_treino = ft.ElevatedButton("Treino", on_click=lambda _: open_link("https://www.youtube.com/watch?v=wFtMbchQSNs"))  # Substitua '#' pelo link do treino
    btn_videos = ft.ElevatedButton("Vídeos", on_click=lambda _: open_link("https://www.youtube.com/watch?v=wFtMbchQSNs"))  # Substitua '#' pelo link dos vídeos
    
    page.add(
        ft.Column(
            controls=[btn_dicas, btn_treino, btn_videos],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    
ft.app(target=main)
