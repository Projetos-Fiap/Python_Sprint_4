from datetime import datetime
import funcoes.extrato as extrato
import funcoes.reciclagens as reciclagem
import funcoes.recompensas as recompensa
import funcoes.tiposDeLixo as tipoDeLixo
import funcoes.usuario as usuario
import funcoes.escritaArquivo as escritaArquivo
import os
# Defininfo função que limpa a tela do terminal
limpa_a_tela = lambda: os.system('cls')
usuarioCorrente = ''

usuarios = escritaArquivo.carrega_usuarios()
# [
    # {'nome': 'Rena', 'email':'rena@gmail.com', 'senha': 'Pao123', 'pontos': 20.0, 'id': 0}
# ]

recompensas = escritaArquivo.carrega_recompensas()

# [
    # {'nome': 'Kit de papelaria', 'custo': 100, 'id': 0},
    # {'nome': 'Fone Bluetooth', 'custo': 1000, 'id': 1},
    # {'nome': 'Carregador portatil', 'custo': 800, 'id': 2},
    # {'nome': 'Sabao', 'custo': 400, 'id': 3}
# ]

tiposDeLixo = escritaArquivo.carrega_tipos_de_lixo()
# [
#     {'nome': 'vidro', 'valorKG': 250, 'id': 0},
#     {'nome': 'metal', 'valorKG': 100, 'id': 1},
#     {'nome': 'plastico', 'valorKG': 500, 'id': 2},
#     {'nome': 'papel', 'valorKG': 100, 'id': 3},
#     {'nome': 'pilha', 'valorKG': 1000, 'id': 4},
#     {'nome': 'oleo', 'valorKG': 400, 'id': 5}
# ]

reciclagens = escritaArquivo.carrega_reciclagens()
# [
#     {'idUser': 0, 'idTipoDeLixo': 3, 'quantidadeG': 300, 'data': '22h11-19/05/2023'},
#     {'idUser': 0, 'idTipoDeLixo': 1, 'quantidadeG': 400, 'data': '22h12-19/05/2023'},
#     {'idUser': 0, 'idTipoDeLixo': 2, 'quantidadeG': 100, 'data': '22h13-19/05/2023'}
# ]

trocasRecompensas = escritaArquivo.carrega_trocas_recompensas()
# [
#     {'idUser': 0, 'idRecompensa': 0, 'quantidade': 1, 'data': '22h17-19/05/2023'}
# ]


def converte_data_em_string(data):
    return f"{data.hour}h{data.minute}-{data.day}/{data.month}/{data.year}"

def mostra_tela_inicial():
    print('==========================')
    print('||    MENU PRINCIPAL    ||')
    print('==========================')
    print('1. Login')
    print('2. Cadastro')
    print('0. Finalizar programa')

def mostra_home_logado():
    print('==========================')
    print('||         HOME         ||')
    print('==========================')
    print(f"Usuário: {usuarioCorrente['nome']}\n")
    print(f"Pontos: {usuarioCorrente['pontos']}\n")
    print('1. Mostrar Extrato')
    print('2. Cadastrar Reciclagem')
    print('3. Trocar Pontos')
    print('4. Alterar Senha')
    print('0. Logout')




while True:
    mostra_tela_inicial()
    opcaoInicial = input('Insira a opção desejada: ')
    
    match opcaoInicial:

        case '1':
            usuarioCorrente = usuario.fluxo_login(usuarios)
            while True:
                mostra_home_logado()
                opcaoLogado = input('Informe a opção desejada: ')
                match opcaoLogado:
                    case '1':
                        extrato.mostra_extrato(reciclagens, trocasRecompensas, usuarioCorrente['id'], tiposDeLixo, recompensas, usuarios)
                    case '2':
                        reciclagem.fluxo_reciclagem(reciclagens, usuarios, tiposDeLixo, usuarioCorrente['id'], converte_data_em_string(datetime.now()))
                    case '3':
                        recompensa.fluxo_troca_recompensa(usuarioCorrente['id'], usuarios, trocasRecompensas, recompensas, converte_data_em_string(datetime.now()))
                    case '4':
                        usuario.fluxo_altera_senha(usuarioCorrente['id'], usuarios)
                    case '0':
                        usuarioCorrente = ''
                        limpa_a_tela()
                        break
                    case _:
                        limpa_a_tela()
                        print('Opção inválida, tente novamente!')
            
        case '2':
            usuario.cadastrar_usuario(usuarios)
        case '0':
            break
        case _:
            limpa_a_tela()
            print('Opção inválida, tente novamente!')
            
        


    