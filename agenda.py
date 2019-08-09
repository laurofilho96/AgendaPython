#Agenda telefonica
#Apenas para estudo,
#Criado e Editado com base no vídeo:
#https://www.youtube.com/watch?v=XCNvEV8oGvo

import os

lista = []
arq2 = open("agenda.csv", "r")
lista = arq2.readlines()
arq2.close()

def menu():
    print("Bem Vindo a Sua Agenda :)")
    print("\n", "=" * 30)
    print("1 - Criar Pessoa \n2 - Excluir Pessoa \n3 - Listar Pessoa \n4 - Sair")

def lista_agenda(nome, descricao, opcao):
    if(opcao ==1):
        pessoa = nome+ ";" +descricao+"\n"
        
        lista.append(pessoa) ##append - acrescentar informação
        lista.sort()

        print("Pessoa Adicionada!!")
        os.system("sleep 2s")
        print(lista)
    #Excluindo pessoa através do id
    if(opcao == 2):
        tam = len(lista)
        for i in range(tam):
            print(i," - ", lista[i])

        delete = int(input("Qual deseja Apagar? "))
        lista.pop(delete)
        print("Registro excluido")
        os.system("sleep 2s")
    ##Listando Pessoas
    if(opcao == 3):
        tam = len(lista)
        for i in range(tam):
            print(lista[i])
        os.system("sleep 2s")
    #Abrindo o arquivo e retornando o tamanho da lista.
    arq = open("agenda.csv", "w")
    tam = len(lista)

    for i in range(tam):
        arq.write(lista[i])
    arq.close()

o = 0
while True:
    os.system("Clear")
    
    menu()
    op = int(input("Opção: "))

    ##1 - Adicionando Pessoa
    if(op == 1):
        n = input("Digite um nome: ")
        desc = input("Digite uma descrição: ")
        lista_agenda(n, desc, 1)
    ##2 - Excluindo Pessoa
    if (op ==2):
        lista_agenda(0, 0, 2)        
    ##3 - Listando Pessoas
    if (op == 3):
        lista_agenda(0, 0, 3)
    ##Saindo da Agenda
    if (op == 4):
        break
