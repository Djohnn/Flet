from flet import *
from database import  add_dica, get_dicas, update_dica, delete_dica




def dicas_page(page: Page):
    page.title = "Dicas"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.scroll = "auto"

    if not page.session.contains_key("dicas_links"):
        page.session.set("dicas_links", [])

    input_link = TextField(label="Link do PDF", width=300)
    input_desc = TextField(label="Descrição do PDF", width=300)
    edit_id = None  # Índice do item sendo editado

    # Área de rolagem para os PDFs
    content_scroll = Container(
        content=Row(wrap=True, scroll=ScrollMode.ALWAYS, expand=True),
        height=500,
        padding=10,
        bgcolor=colors.with_opacity(0.1, Colors.BLACK),
    )

    def update_content():
        """Atualiza a interface com a lista de PDFs"""
        content_scroll.content.controls.clear()
        for dica_id, url, desc in get_dicas():
            content_scroll.content.controls.append(
                Container(
                    content=Column([
                        Icon(Icons.PICTURE_AS_PDF, size=40, color=Colors.WHITE),
                        Text(desc, size=16, color=Colors.WHITE),
                        Row([
                            IconButton(icons.EDIT, on_click=lambda e, id=dica_id: open_edit_modal(id, url, desc)),
                            IconButton(icons.DELETE, on_click=lambda e, id=dica_id: remove_dica(id))
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
                    on_click=lambda e, link=url: page.launch_url(link)
                )
            )
        page.update()

    def handle_close(e):
        """Salva ou edita um PDF na lista"""
        nonlocal edit_id
        link_text = input_link.value.strip()
        desc_text = input_desc.value.strip()

        if e.control.text == "Salvar" and (link_text and desc_text):
            # links = page.session.get("dicas_links")
            if edit_id is not None:
                update_dica(edit_id, link_text, desc_text)
                # links[edit_id] = {"url": link_text, "desc": desc_text}
                edit_id = None
            else:
                add_dica(link_text, desc_text)
                # links.append({"url": link_text, "desc": desc_text})
            #     links.append({"url": link_text, "desc": desc_text})
            # page.session.set("dicas_links", links)
            update_content()

        input_link.value = ""
        input_desc.value = ""
        page.close(dlg_modal)

    def open_edit_modal(dica_id, url, desc):
        """Abre o modal para edição de um PDF"""
        nonlocal edit_id
        edit_id = dica_id
        # item = page.session.get("dicas_links")[index]
        input_link.value = url
        input_desc.value = desc
        page.open(dlg_modal)
        page.update()

    def remove_dica(dica_id):
        """Exclui um PDF da lista"""
        delete_dica(dica_id)
        update_content()
        # links = page.session.get("dicas_links")
        # del links[index]
        # page.session.set("dicas_links", links)
        # update_content()

    dlg_modal = AlertDialog(
        modal=True,
        title=Text("Adicionar/Editar PDF"),
        content=Column([input_link, input_desc], tight=True),
        actions=[
            TextButton("Salvar", on_click=handle_close),
            TextButton("Cancelar", on_click=lambda e: page.close(dlg_modal)),
        ],
        actions_alignment=MainAxisAlignment.END,
    )

    # Layout principal
    fundo_img = Stack([
        Container(content=Image(src="src/assets/fundo.png", fit=ImageFit.COVER, expand=True), expand=True),
        Column([
            Text("Dicas de Treino", size=24, weight=FontWeight.BOLD, color=Colors.WHITE),
            Row([
                ElevatedButton("Voltar", on_click=lambda e: page.go("/")),
                ElevatedButton("Adicionar PDF", icon=icons.ADD, on_click=lambda e: page.open(dlg_modal)),
            ], alignment=MainAxisAlignment.CENTER),
            content_scroll
        ], expand=True)
    ], expand=True)

    page.views.append(View("/dicas", [fundo_img]))
    update_content()





# from flet import *

# def dicas_page(page: Page):
#     page.title = "Dicas"
#     page.vertical_alignment = MainAxisAlignment.CENTER
#     page.horizontal_alignment = CrossAxisAlignment.CENTER
#     page.scroll = "auto"

#     # Inicializar a sessão para armazenar os links
#     if not page.session.contains_key("dicas_links"):
#         page.session.set("dicas_links", [])

#     # Campos de entrada
#     input_link = TextField(label="Link do PDF", width=300)
#     input_desc = TextField(label="Descrição do PDF", width=300)

#     # Criar um contêiner para a rolagem horizontal e vertical
#     content_scroll = Container(
#         content=Row(
#             wrap=True,  # Permite quebra de linha quando não couber mais na tela
#             scroll=ScrollMode.ALWAYS,  # Rolagem horizontal sempre ativa
#             expand=True
#         ),
#         height=500,  # Ajuste conforme necessário
#         padding=10,
#         bgcolor=colors.with_opacity(0.1, Colors.BLACK),
#     )

#     # Atualizar a interface
#     def update_content():
#         content_scroll.content.controls.clear()  # Limpar antes de adicionar novos elementos

#         # Exibir PDFs salvos
#         for item in page.session.get("dicas_links"):
#             content_scroll.content.controls.append(
#                 Container(
#                     content=Column(
#                         [
#                             Icon(Icons.PICTURE_AS_PDF, size=40, color=Colors.WHITE),
#                             Text(item["desc"], size=16, color=Colors.WHITE),
#                         ],
#                         alignment=MainAxisAlignment.CENTER,
#                     ),
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

#     # Fechar o modal e salvar os dados
#     def handle_close(e):
#         if e.control.text == "Yes":
#             link_text = input_link.value.strip()
#             desc_text = input_desc.value.strip()

#             if link_text and desc_text:
#                 # Adicionar à sessão
#                 dicas_links = page.session.get("dicas_links")
#                 dicas_links.append({"url": link_text, "desc": desc_text})
#                 page.session.set("dicas_links", dicas_links)

#                 # Atualizar a interface
#                 update_content()

#             # Limpar os campos de entrada
#             input_link.value = ""
#             input_desc.value = ""

#         # Fechar o modal
#         page.close(dlg_modal)

#     # Modal de entrada
#     dlg_modal = AlertDialog(
#         modal=True,
#         title=Text("Adicionar PDF"),
#         content=Column([input_link, input_desc], tight=True),
#         actions=[
#             TextButton("Yes", on_click=handle_close),
#             TextButton("No", on_click=handle_close),
#         ],
#         actions_alignment=MainAxisAlignment.END,
#     )

#     # Fundo com imagem
#     fundo_img = Stack([
#         Container(
#             content=Image(
#                 src="src/assets/fundo.png",
#                 fit=ImageFit.COVER,
#                 expand=True
#             ),
#             expand=True
#         ),
#         Column(
#             [
#                 Text("Dicas de Treino", size=24, weight=FontWeight.BOLD, color=Colors.WHITE),
#                 Row([
#                     ElevatedButton("Voltar", on_click=lambda e: page.go("/")),
#                     ElevatedButton("Adicionar PDF", icon=icons.ADD, on_click=lambda e: page.open(dlg_modal)),
#                 ], alignment=MainAxisAlignment.CENTER),
#                 content_scroll  # Adicionando a área de rolagem
#             ],
#             expand=True
#         )
#     ], expand=True)

#     # Adicionar a view
#     page.views.append(View("/dicas", [fundo_img]))
#     update_content()











#nao apagar 

# from flet import *

# def dicas_page(page: Page):
#     page.title = "Dicas"
#     page.vertical_alignment = MainAxisAlignment.CENTER
#     page.horizontal_alignment = CrossAxisAlignment.CENTER
#     page.scroll = "auto"

#     # Inicializar a sessão para armazenar os links
#     if not page.session.contains_key("dicas_links"):
#         page.session.set("dicas_links", [])

#     # Campos de entrada
#     input_link = TextField(label="Link do PDF", width=300)
#     input_desc = TextField(label="Descrição do PDF", width=300)

#     # Conteúdo principal
#     content_column = Column(
#         scroll=ScrollMode.ALWAYS,
#         expand=True,
#         alignment=MainAxisAlignment.CENTER,
#         horizontal_alignment=CrossAxisAlignment.CENTER
#     )

#     # Atualizar a interface
#     def update_content():
#         content_column.controls.clear()

#         # Título e botões
#         content_column.controls.extend([
#             Text("Dicas de Treino", size=24, weight=FontWeight.BOLD, color=Colors.WHITE),
#             Row([
#                 ElevatedButton("Voltar", on_click=lambda e: page.go("/")),
#                 ElevatedButton("Adicionar PDF", icon=icons.ADD, on_click=lambda e: page.open(dlg_modal)),
#             ], alignment=MainAxisAlignment.CENTER),
#         ])

#         # Exibir PDFs salvos
#         for item in page.session.get("dicas_links"):
#             content_column.controls.append(
#                 Container(
#                     content=Column(
#                         [
#                             Icon(Icons.PICTURE_AS_PDF, size=40, color=Colors.WHITE),
#                             Text(item["desc"], size=16, color=Colors.WHITE),
#                         ],
#                         alignment=MainAxisAlignment.CENTER,
#                     ),
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

#     # Fechar o modal e salvar os dados
#     def handle_close(e):
#         if e.control.text == "Yes":
#             link_text = input_link.value.strip()
#             desc_text = input_desc.value.strip()

#             if link_text and desc_text:
#                 # Adicionar à sessão
#                 dicas_links = page.session.get("dicas_links")
#                 dicas_links.append({"url": link_text, "desc": desc_text})
#                 page.session.set("dicas_links", dicas_links)

#                 # Atualizar a interface
#                 update_content()

#             # Limpar os campos de entrada
#             input_link.value = ""
#             input_desc.value = ""

#         # Fechar o modal
#         page.close(dlg_modal)

#     # Modal de entrada
#     dlg_modal = AlertDialog(
#         modal=True,
#         title=Text("Adicionar PDF"),
#         content=Column([input_link, input_desc], tight=True),
#         actions=[
#             TextButton("Yes", on_click=handle_close),
#             TextButton("No", on_click=handle_close),
#         ],
#         actions_alignment=MainAxisAlignment.END,
#     )

#     # Fundo com imagem
#     fundo_img = Stack([
#         Container(
#             content=Image(
#                 src="src/assets/fundo.png",
#                 fit=ImageFit.COVER,
#                 expand=True
#             ),
#             expand=True
#         ),
#         content_column
#     ], expand=True)

#     # Adicionar a view
#     page.views.append(View("/dicas", [fundo_img]))
#     update_content()
