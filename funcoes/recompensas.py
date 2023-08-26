import os
# Defininfo função que limpa a tela do terminal
limpa_a_tela = lambda: os.system('cls')

def eh_numero(valor):
    if valor == '':
        return False

    numeros = '0123456789'

    for char in valor:
        if char not in numeros:
            return False
    return True

def cadastra_recompensa(DbRecompensas):
    nome = input('Digite o nome da recompensa: ')
    custo = input('Digite o custo da recompensa: ')
    id = len(DbRecompensas)
    recompensa = {
        'nome': nome,
        'custo': custo,
        id: id
    }
    DbRecompensas.append(recompensa)
    limpa_a_tela()
    print('Recompensa cadastrada!')

def custo_pontos_carrinho(carrinho, DbRecompensas):
    soma = 0
    for item in carrinho:
        soma += DbRecompensas[item['idRecompensa']]['custo']*item['quantidade']
    return soma

def mostrar_menu_continuar_carrinho():
    print('=========================================')
    print('||      DESEJA TROCAR MAIS ITENS?      ||')
    print('=========================================')
    print('1. SIM')
    print('2. FINALIZAR TROCAS')
    print('0. ESVAZIAR CARRINHO')

def mostra_carrinho(carrinho, DbRecompensas):
    if carrinho == []:
        print('>>> Carrinho Vazio <<<')
    else:
        print('==========================')
        print('||        Carrinho      ||')
        print('==========================')
        somaCarrinho = 0
        for item in carrinho:
            print(f"{item['quantidade']} x {DbRecompensas[item['idRecompensa']]['nome']}")
            somaCarrinho += DbRecompensas[item['idRecompensa']]['custo'] * item['quantidade']
        print(f"Custo do carrinho: {somaCarrinho} pontos ")
        print('\n')

def atualiza_recompensa(DbRecompensas, recompensa):
    DbRecompensas[recompensa["id"]]["nome"] = recompensa["nome"]
    DbRecompensas[recompensa["id"]]["custo"] = recompensa["custo"]
    limpa_a_tela()
    print('Sua recompensa foi atualizada!')

def mostra_recompensas(DbRecompensas):
    limpa_a_tela()
    print('==========================')
    print('||     Recompensas      ||')
    print('==========================')
    for item in DbRecompensas:
        print(f"{item['id']+1}. Nome: {item['nome']} Custo: {item['custo']}")
    print('=====================================\n')

def fluxo_troca_recompensa(idUser, DbUsers, DbTrocas, DbRecompensas, data):
    carrinho = []
    while True:
        mostra_recompensas(DbRecompensas)
        mostra_carrinho(carrinho, DbRecompensas)
        pontosUser = DbUsers[idUser]['pontos']
        print(f"Saldo de pontos: {pontosUser}")

        # Lendo e validando opcao de troca
        opcaoTroca = input('Informe a opção desejada: ')
        if not eh_numero(opcaoTroca):
            limpa_a_tela()
            print('Opcao de troca inválida! Tente novamente.')
            continue
        opcaoTroca = int(opcaoTroca)

        if opcaoTroca > len(DbRecompensas) or opcaoTroca < 1:
            limpa_a_tela()
            print(len(DbTrocas))
            print('Opcao de troca inválida! Tente novamente.')
            continue

        # Lendo e validando quantidade de troca
        quantidadeTroca = input('Informe a quantidade desejada: ')
        if not eh_numero(quantidadeTroca):
            limpa_a_tela()
            print('Quantidade de troca inválida! Tente novamente.')
            continue
        
        quantidadeTroca = int(quantidadeTroca)
        if (quantidadeTroca <= 0 ):
            limpa_a_tela()
            print('Quantidade de troca inválida! Tente novamente.')
        else: 

            novoItem = {
                'quantidade': quantidadeTroca,
                'idRecompensa': opcaoTroca-1
            }
            carrinho.append(novoItem)
            limpa_a_tela()
            print(f"Item adicionado ao carrinho!")
            mostra_carrinho(carrinho, DbRecompensas)
            mostrar_menu_continuar_carrinho()
            opcao = ''
            while True:
                opcao = input('Digite a opcao desejada: ')
                if not eh_numero(opcao):
                    print('Opção inválida! Tente novamente!')
                    continue
                if int(opcao) > len(DbRecompensas):
                    print('Opção inválida! Tente novamente!')
                    continue
                else:
                    break
                
            match opcao:
                case '1':
                    limpa_a_tela()
                    continue
                case '2':
                    custoCarrinho = custo_pontos_carrinho(carrinho, DbRecompensas)
                    if custoCarrinho > pontosUser:
                            limpa_a_tela()
                            print('Saldo de pontos insuficiente!')
                            break
                    for item in carrinho: 
                        troca = {
                            'idUser': idUser,
                            'idRecompensa': item['idRecompensa'],
                            'quantidade': item['quantidade'],
                            'data': data
                        }
                        DbTrocas.append(troca)
                    DbUsers[idUser]['pontos'] -= custoCarrinho
                    limpa_a_tela()
                    print('Troca por recompensa registrada!')
                    print('Pontos deduzidos do seu saldo!')
                    break
                case '0':
                    limpa_a_tela()
                    carrinho = []
                    print('Carrinho esvaziado!')
                    continue
                case _:
                    print('Opção inválida, tente novamente!')




