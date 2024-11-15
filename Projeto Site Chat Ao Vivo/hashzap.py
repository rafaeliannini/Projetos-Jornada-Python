# Titulo: Hashzap
# Botão: Iniciar chat
    # popup/alert
        # titulo: Bem-Vindo ao Hashzap
        # campo de texto: escreva seu nome no chat
        # botão: entrar no chat
            # sumir com titulo e botão inicial
            # fechar o popup
            # criar o chat com a mesagem de nome do usuario entrou no chat
            # embaixo do chat:
                # campo de texto: Digite sua mensagem
                # botão enviar
                    # vai aparecer a mensagem no chat com o nome do usuario

# Flet -> aplicativos/sites/programas de computador
# pip install flet

# importar o flet
import flet as ft

# criar a função principal do seu sistema
def main (pagina):
    # criar os elementos
    titulo = ft.Text("Hashzap")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()
        

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    titulo_janela = ft.Text("Bem-Vindo ao Hashzap") 

    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"   
        
        # enviar mensagem no tunel
        pagina.pubsub.send_all(texto)
        texto_mensagem.value = ""
        pagina.update()
    
    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem) 
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    chat = ft.Column()

    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)

        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrou_chat)
        pagina.update()
    
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # adicionar os elementos inicias
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# executar o sistema
ft.app(main, view=ft.WEB_BROWSER)