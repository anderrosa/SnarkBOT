from chatbot.use_cases.response import GetResponseUseCase

def chatbot(use_case: GetResponseUseCase):
    print("O que você quer?\n")

    while True:
        prompt = input("> ")
        if prompt.lower() == "sair":
            print("Finalmente! Não aguento mais você!")
            break
        response = use_case.execute(prompt)
        print(response)
        print("\n")
