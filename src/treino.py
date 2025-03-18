from flet import *

def treino_page(page: Page):
    page.title = "Treino"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.scroll = "auto"

    if not page.session.contains_key("treino_links"):
        page.session.set("treino_links", [])

    input_link = TextField(label="Link do Vídeo", width=300)
    input_desc = TextField(label="Descrição do Vídeo", width=300)
    edit_index = None  # Armazena o índice do item em edição

    content_scroll = Container(
        content=Row(wrap=True, scroll=ScrollMode.ALWAYS, expand=True),
        height=500,
        padding=10,
        bgcolor=colors.with_opacity(0.1, Colors.BLACK),
    )

    def update_content():
        content_scroll.content.controls.clear()
        for index, item in enumerate(page.session.get("treino_links")):
            content_scroll.content.controls.append(
                Container(
                    content=Column([
                        Icon(Icons.FITNESS_CENTER, size=40, color=Colors.WHITE),
                        Text(item["desc"], size=16, color=Colors.WHITE),
                        Row([
                            IconButton(icons.EDIT, on_click=lambda e, idx=index: open_edit_modal(idx)),
                            IconButton(icons.DELETE, on_click=lambda e, idx=index: delete_item(idx))
                        ], alignment=MainAxisAlignment.CENTER)
                    ], alignment=MainAxisAlignment.CENTER),
                    margin=10,
                    padding=10,
                    alignment=alignment.center,
                    width=200,
                    height=200,
                    border_radius=10,
                    ink=True,
                    bgcolor=colors.with_opacity(0.3, Colors.BLACK),
                    on_click=lambda e, url=item["url"]: page.launch_url(url)
                )
            )
        page.update()

    def handle_close(e):
        nonlocal edit_index
        link_text = input_link.value.strip()
        desc_text = input_desc.value.strip()

        if e.control.text == "Salvar":
            if link_text and desc_text:
                links = page.session.get("treino_links")
                if edit_index is not None:
                    links[edit_index] = {"url": link_text, "desc": desc_text}
                    edit_index = None
                else:
                    links.append({"url": link_text, "desc": desc_text})
                page.session.set("treino_links", links)
                update_content()

        input_link.value = ""
        input_desc.value = ""
        page.close(dlg_modal)

    def open_edit_modal(index):
        nonlocal edit_index
        edit_index = index
        item = page.session.get("treino_links")[index]
        input_link.value = item["url"]
        input_desc.value = item["desc"]
        page.open(dlg_modal)
        page.update()

    def delete_item(index):
        links = page.session.get("treino_links")
        del links[index]
        page.session.set("treino_links", links)
        update_content()

    dlg_modal = AlertDialog(
        modal=True,
        title=Text("Adicionar/Editar Vídeo"),
        content=Column([input_link, input_desc], tight=True),
        actions=[
            TextButton("Salvar", on_click=handle_close),
            TextButton("Cancelar", on_click=lambda e: page.close(dlg_modal)),
        ],
        actions_alignment=MainAxisAlignment.END,
    )

    fundo_img = Stack([
        Container(content=Image(src="src/assets/fundo.png", fit=ImageFit.COVER, expand=True), expand=True),
        Column([
            Text("Treinos Personalizados", size=24, weight=FontWeight.BOLD, color=Colors.WHITE),
            Row([
                ElevatedButton("Voltar", on_click=lambda e: page.go("/")),
                ElevatedButton("Adicionar Vídeo", icon=icons.ADD, on_click=lambda e: page.open(dlg_modal)),
            ], alignment=MainAxisAlignment.CENTER),
            content_scroll
        ], expand=True)
    ], expand=True)

    page.views.append(View("/treino", [fundo_img]))
    update_content()






# from flet import *

# def treino_page(page: Page):
#     page.title = "Treino"
#     page.vertical_alignment = MainAxisAlignment.CENTER
#     page.horizontal_alignment = CrossAxisAlignment.CENTER
#     page.scroll = "auto"

#     # Inicializar a sessão para armazenar os links
#     if not page.session.contains_key("treino_links"):
#         page.session.set("treino_links", [])

#     # Campos de entrada
#     input_link = TextField(label="Link do Vídeo", width=300)
#     input_desc = TextField(label="Descrição do Vídeo", width=300)

#     # Área de rolagem horizontal para vídeos
#     content_scroll = Container(
#         content=Row(
#             wrap=True,
#             scroll=ScrollMode.ALWAYS,
#             expand=True
#         ),
#         height=500,
#         padding=10,
#         bgcolor=colors.with_opacity(0.1, Colors.BLACK),
#     )

#     # Atualizar a interface
#     def update_content():
#         content_scroll.content.controls.clear()
#         for item in page.session.get("treino_links"):
#             content_scroll.content.controls.append(
#                 Container(
#                     content=Column([
#                         Icon(Icons.FITNESS_CENTER, size=40, color=Colors.WHITE),
#                         Text(item["desc"], size=16, color=Colors.WHITE),
#                     ], alignment=MainAxisAlignment.CENTER),
#                     margin=10,
#                     padding=10,
#                     alignment=alignment.center,
#                     width=150,
#                     height=150,
#                     border_radius=10,
#                     ink=True,
#                     bgcolor=colors.with_opacity(0.3, Colors.BLACK),
#                     on_click=lambda e, url=item["url"]: page.launch_url(url)
#                 )
#             )
#         page.update()

#     # Modal de adicionar vídeo
#     def handle_close(e):
#         if e.control.text == "Adicionar":
#             link_text = input_link.value.strip()
#             desc_text = input_desc.value.strip()
#             if link_text and desc_text:
#                 links = page.session.get("treino_links")
#                 links.append({"url": link_text, "desc": desc_text})
#                 page.session.set("treino_links", links)
#                 update_content()
#                 input_link.value = ""
#                 input_desc.value = ""
#         page.close(dlg_modal)

#     dlg_modal = AlertDialog(
#         modal=True,
#         title=Text("Adicionar Vídeo"),
#         content=Column([input_link, input_desc], tight=True),
#         actions=[
#             TextButton("Adicionar", on_click=handle_close),
#             TextButton("Cancelar", on_click=lambda e: page.close(dlg_modal)),
#         ],
#         actions_alignment=MainAxisAlignment.END,
#     )

#     # Layout principal
#     fundo_img = Stack([
#         Container(
#             content=Image(
#                 src="src/assets/fundo.png",
#                 fit=ImageFit.COVER,
#                 expand=True
#             ),
#             expand=True
#         ),
#         Column([
#             Text("Treinos Personalizados", size=24, weight=FontWeight.BOLD, color=Colors.WHITE),
#             Row([
#                 ElevatedButton("Voltar", on_click=lambda e: page.go("/")),
#                 ElevatedButton("Adicionar Vídeo", icon=icons.ADD, on_click=lambda e: page.open(dlg_modal)),
#             ], alignment=MainAxisAlignment.CENTER),
#             content_scroll
#         ], expand=True)
#     ], expand=True)

#     page.views.append(View("/treino", [fundo_img]))
#     update_content()
