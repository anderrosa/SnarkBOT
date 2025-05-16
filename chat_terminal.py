from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
import requests
import textwrap

# Configurações
API_URL = "http://localhost:5000/api/chat"

# Largura máxima da linha
WRAP_WIDTH = 50

# Estilo do prompt
custom_style = Style.from_dict({
    'prompt': '#00ffff bold',
    'bot': 'ansimagenta italic',
    'error': 'ansired bold',
})

print("\n💬 SnarkBOT (digite 'sair' para encerrar)\n")

while True:
    try:
        user_input = prompt('[Você]: ', style=custom_style)

        if user_input.strip().lower() == "sair":
            print("\n👋 Tchau! Finalmente um descanso.")
            break

        response = requests.post(API_URL, json={"mensagem": user_input})

        if response.status_code == 200:
            bot_reply = response.json().get("resposta", "")

            wrapped_reply = textwrap.fill(bot_reply, width=WRAP_WIDTH)
            
            print(f"\n[\x1b[35m🤖 SnarkBOT\x1b[0m]: {wrapped_reply}\n")  
            # Estilo magenta simples se não tiver suporte ANSI
        else:
            print(f"\n[{custom_style['error']}]❌ Erro: Código {response.status_code} - {response.text}\n")

    except KeyboardInterrupt:
        print("\n\n❌ Interrompido pelo usuário.")
        break
    except Exception as e:
        print(f"\n[{custom_style['error']}]Erro inesperado: {e}\n")

