# DESENVOLVA UM PROGRAMA QUE O

# USUÁRIO IRÁ INFORMAR UMA
# PERGUNTA (UTILIZANDO

# EXATAMENTE AS PERGUNTAS NDO
# QUESTIONÁRIO ANTERIOR) E O
# SISTEMA DEVERÁ DAR A RESPOSTA.

menu = """
 ========================== Faça a pergunta =======================================
    [1] - "QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?",
    [2] - "QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?",
    [3] - "QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?",
    [4] - "COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?",
    [5] - "QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?",
    [6] - "QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DEBLACK MIRROR?",
    [7] - "O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE.")
    
    Digite: """

while True:
     opcao = input(menu)
     if opcao == "1":
        print("A reposta é: O nome da protagonista é Joan ")
     elif opcao == "2":
        print("A reposta é: A vida de joan ")
     elif opcao == "3":
        print("A reposta é: É o serviço de streaming")
     elif opcao == "4":
        print("A reposta é: No sofá de casa ")
     elif opcao == "5":
        print("A reposta é: Uma sensação de desespero.")
     elif opcao == "6":
        print("A reposta é: Traição, trabalho e emoção são os temas explorados.")
     elif opcao == "7":
        print("A reposta é: Não.")
     else:
        print("Erro! A opção é invalida")
        break

