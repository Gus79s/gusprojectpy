import os
import time



def limpa_no_programa():
    time.sleep(3)
    os.system('cls')
def opcao1(opc1):
    if opc1==1:
        print ("você escolheu a opção 1")
        preferencias=input("Digite o que deseja para o site web:\n")
        print("Você escolheu a opção 1 e deseja um site com as seguintes preferências:", preferencias)
        limpa_no_programa()
        menu_principal()
        

def opcao2(opc2):
    if opc2==2:
        print ("você escolheu a opção 2")
        servico=input("Digite o serviço que deseja contatar:\n")
        print("Você escolheu a opção 2 e deseja contatar o seguinte serviço:", servico)
        limpa_no_programa()
        menu_principal()

def opcao3(opc3):
    if opc3==3:
        print ("você escolheu a opção 3")
        print("Número de Gus = +55 11 9 9999-9999")
        limpa_no_programa()
        menu_principal()

def encerramento():
    print("seção encerrada!")
def menu_principal():
    print("Olá como posso ajudar?")
    print("1-Desejo a criação de um site web.")
    print("2-Desejo contatar algum outro serviço.")
    print("3-Falar com Gus.")
    print("4-Encerrar programa.")
    primeira_ordem=int(input("Digite o número da opção desejada:\n"))

    try:
        if primeira_ordem==1:
             exibicao_cliente=opcao1(primeira_ordem)
             print(exibicao_cliente)
        elif primeira_ordem==2:
            exibicao_cliente=opcao2(primeira_ordem)
            print(exibacao_cliente)
        elif primeira_ordem==3:
            exibicao_cliente=opcao3(primeira_ordem)
            print(exibacao_cliente)
        elif primeira_ordem == 4:
            exibicao_cliente=encerramento()
    except:
        print("opção inválida, por favor reinicie o programa e escolha uma opção válida.")


    
print(menu_principal())