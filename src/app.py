from flet import *


def main(page: Page):
    page.title = "Bem vindo ao Clan"
    page.window_width = 360
    page.window_height = 640
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER


    def confirmar(e):
        page.alert_dialog.open = True
        page.update()
    

    def cancelar(e):
        page.alert_dialog.open = False
        page.update()
    

    # Definir os campos de entrada
    input_link = TextField(label="Link do PDF", width=300)
    input_desc = TextField(label="Descrição do PDF", width=300)

    # Criar o AlertDialog APENAS UMA VEZ
    alerta_dialogo = AlertDialog(
        modal=True,
        title=Text("Adicionar PDF"),
        content=Column([input_link, input_desc], tight=True),
        actions=[
            TextButton("Adicionar", on_click=lambda e: confirmar(e)),
            TextButton("Cancelar", on_click=lambda e: cancelar(e)),
        ],
    )

    def abrir_modal(e):
        if not alerta_dialogo.open:
            page.dialog = alerta_dialogo
            alerta_dialogo.open = True
            print("nao abriu")
            page.update()
            
        else:
            page.dialog = alerta_dialogo
            alerta_dialogo.open = True
            
            print("else")
            page.update()
        

    page.add(
        Text(
            "Bem vindo ao Clan",
            size=30,
            color="blue",
            weight="bold",
            italic=True,
            ),
        ElevatedButton(
            "Dicas",
            on_click=lambda e: abrir_modal(e)),
            )

        

app = app(target=main)