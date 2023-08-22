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

def mostra_carrinho(carrinho, DbTiposDeLixo):
    if carrinho == []:
        print('>>> Carrinho Vazio <<<')
    else:
        print('==========================')
        print('||        Carrinho      ||')
        print('==========================')
        for item in carrinho:
            print(f"Quantidade em G: {item['quantidadeG']} Tipo de Lixo: {DbTiposDeLixo[item['idTipoDeLixo']]['nome']}")
        print('\n')

def mostrar_menu_continuar_comprando():
    print('==============================================')
    print('||    CONTINUAR ADICIONANDO RECICLAGENS?    ||')
    print('==============================================')
    print('1. SIM')
    print('2. FINALIZAR REGISTRO DE RECICLAGEM')
    print('0. ESVAZIAR CARRINHO')

def fluxo_reciclagem(DbReciclagens, DbUsers, DbTiposDeLixo, idUser, data):
    carrinho = []
    while True:
        mostra_tipos_de_lixo(DbTiposDeLixo)
        mostra_carrinho(carrinho, DbTiposDeLixo)
        opcaoLixo = int(input('Insira o tipo de lixo que deseja reciclar: '))
        quantidadeG = float(input('Insira a quantidade em gramas: '))
        

        if(quantidadeG < 1 or opcaoLixo > len(DbTiposDeLixo)):
            limpa_a_tela()
            print('Valores inválidos, tente novamente!')
        else:
            novoItem = {
                'idTipoDeLixo': opcaoLixo-1,
                'quantidadeG': quantidadeG,
            }
            jaTinha = False
            for item in carrinho:
                if item['idTipoDeLixo'] == novoItem['idTipoDeLixo']:
                    item['quantidadeG'] += novoItem['quantidadeG']
                    jaTinha = True
            if not jaTinha:
                carrinho.append(novoItem)
            limpa_a_tela()
            print(f"Item adicionado ao carrinho!")
            mostra_carrinho(carrinho, DbTiposDeLixo)
            mostrar_menu_continuar_carrinho()
            entradaValida = True
            opcao = ''
            while entradaValida:
                opcao = input('Digite a opcao desejada: ')
                numbers = '0123456789'
                if opcao not in numbers:
                    print('Opção inválida! Tente novamente!')
                    continue
                else:
                    break
                
            match opcao:
                case '1':
                    limpa_a_tela()
                    continue
                case '2':
                    for item in carrinho:
                        reciclagem = {
                            'idUser': idUser,
                            'idTipoDeLixo': item['idTipoDeLixo'],
                            'quantidadeG': item['quantidadeG'],
                            'data': data
                        }
                        DbReciclagens.append(reciclagem)
                        pontos = DbTiposDeLixo[item['idTipoDeLixo']]['valorKG'] * item['quantidadeG'] / 1000
                        DbUsers[idUser]['pontos'] += pontos
                    break
                case '3':
                    limpa_a_tela()
                    carrinho = []
                    print('Carrinho esvaziado!')
                case _:
                    print('Opção inválida, tente novamente!')
            print('Lixo reciclado com sucesso!')
            print('Pontos Adicionados à sua conta!')



def mostrar_menu_continuar_carrinho():
    print('=========================================')
    print('||        CONTINUAR RECICLANDO?        ||')
    print('=========================================')
    print('1. SIM')
    print('2. FINALIZAR RECICLAGENS')
    print('0. ESVAZIAR CARRINHO')


item = {
    "idTipoLixo": 1,
    "quantidadeG": 3
}