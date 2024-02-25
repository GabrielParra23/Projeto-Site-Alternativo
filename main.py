#Criação da parte back-end do site

from flask import Flask, render_template #Estrutura para criar o site
from flask_socketio import SocketIO, send #Estrutura para criar o chat

app = Flask(__name__) #cria o site
app.config["SECRET"] = "alq1522" #criação da chave de segurança, pode ser oque quiser
app.config["DEBUG"] = True #para testar o codigo, no final será retirado
socketio = SocketIO(app, cors_allowed_origins ="*") #cria a conexao entre diferentes máquinas que estão no mesmo site

@socketio.on("message") #define que a função abaixo vai ser acionada quando o evento "message" acontecer
def gerenciar_mensagens(mensagem):
    print(f"Mensagem:{mensagem}")
    send(mensagem, broadcast=True) #envia a mensagem a todos que estão no site
    
@app.route("/") #cria a pagina do site
def home():
    return render_template("index.html") # essa pagina vai carregar o arquivo html que está aqui

if __name__ == "__main__":
    socketio.run(app, host="localhost") #ele define que o site ira rodar no meu servidor local que é a internet conectada ao computador
    

    
    
    
    
    