import os
# Defininfo função que limpa a tela do terminal
limpa_a_tela = lambda: os.system('cls')


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
    mostra_recompensas(DbRecompensas)
    pontosUser = DbUsers[idUser]['pontos']
    print(f"Saldo de pontos: {pontosUser}")

    opcaoTroca = int(input('Informe a opção desejada: '))
    quantidadeTroca = int(input('Informe a quantidade desejada: '))
    if (quantidadeTroca <= 0 ):
        limpa_a_tela()
        print('Valores inválidos! Tente novamente.')
    else: 
        recompensa = DbRecompensas[opcaoTroca-1]
        if recompensa['custo']*quantidadeTroca > pontosUser:
            limpa_a_tela()
            print('Saldo de pontos insuficiente!')
        else:
            troca = {
                'idUser': idUser,
                'idRecompensa': opcaoTroca-1,
                'quantidade': quantidadeTroca,
                'data': data
            }
            DbTrocas.append(troca)
            DbUsers[idUser]['pontos'] -= recompensa['custo']*quantidadeTroca
            limpa_a_tela()
            print('Troca por recompensa registrada!')
            print('Pontos deduzidos do seu saldo!')



