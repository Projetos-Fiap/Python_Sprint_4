import os
# Defininfo função que limpa a tela do terminal
limpa_a_tela = lambda: os.system('cls')


def cadastra_reciclagem(idUser,  idTipoDeLixo, quantidadeG, data, DbUsers, DbTiposDeLixo, DbReciclagens):
    reciclagem = {
        'idUser': idUser,
        'idTipoDeLixo': idTipoDeLixo,
        'quantidadeG': quantidadeG,
        'data': data
    }

    pontos = float(DbTiposDeLixo[idTipoDeLixo]['valorKg'] * quantidadeG / 1000)
    DbUsers[idUser][pontos] += pontos
    DbReciclagens.append(reciclagem)

def mostra_tipos_de_lixo(DbTiposDeLixo):
    limpa_a_tela()
    print('==========================')
    print('||    Tipos de Lixo      ||')
    print('==========================')
    for item in DbTiposDeLixo:
        print(f"{item['id']+1}. Nome: {item['nome']} Pontos/Kg: {item['valorKG']}")
    
    print('=====================================\n')

def fluxo_reciclagem(DbReciclagens, DbUsers, DbTiposDeLixo, idUser, data):
    mostra_tipos_de_lixo(DbTiposDeLixo)
    opcaoLixo = int(input('Insira o o tipo de lixo que deseja reciclar: '))
    quantidadeG = float(input('Insira a quantidade em gramas: '))
    if(quantidadeG < 1 or opcaoLixo >= len(DbTiposDeLixo)):
        limpa_a_tela()
        print('Valores inválidos, tente novamente!')
    else:
        reciclagem = {
            'idUser': idUser,
            'idTipoDeLixo': opcaoLixo-1,
            'quantidadeG': quantidadeG,
            'data': data
        }
        DbReciclagens.append(reciclagem)
        pontos = DbTiposDeLixo[opcaoLixo-1]['valorKG'] * quantidadeG / 1000
        DbUsers[idUser]['pontos'] += pontos
        limpa_a_tela()
        print('Lixo reciclado com sucesso!')
        print('Pontos Adicionados à sua conta!')
