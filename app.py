import flet as ft

def main(page: ft.Page):
    page.title = "App de Treino"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def open_link(index):
        links = [
            "https://www.youtube.com/watch?v=wFtMbchQSNs",  # Substitua pelo link do PDF
            "https://www.youtube.com/watch?v=wFtMbchQSNs#",  # Substitua pelo link do treino
            "https://www.youtube.com/watch?v=wFtMbchQSNs"   # Substitua pelo link dos vídeos
        ]
        page.launch_url(links[index])
    
    navigation = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        expand=True,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.BOOK),
                label="Dicas",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.FITNESS_CENTER),
                label="Treinos",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.VIDEO_COLLECTION),
                label="Vídeos",
            ),
        ],
        on_change=lambda e: open_link(navigation.selected_index)
    )
    
    page.add(ft.Row([navigation], expand=True))
    
ft.app(target=main)
