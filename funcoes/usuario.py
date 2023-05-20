import os
limpa_a_tela = lambda: os.system('cls')

def cadastrar_usuario(DbUsuarios):
    limpa_a_tela()
    nome = input('Digite o nome do usuário: ')
    email = input('Digite o email do usuário: ')
    for user in DbUsuarios:
        if user['email'] == email:
            print('Este email já está sendo usado!')
        
    while True:
        senha = input('Digite o senha do usuário: ')
        confirmeSenha = input('Confirme a senha do usuário: ')
        if(senha != confirmeSenha):
            limpa_a_tela()
            print('As Senhas não conferem! Tente novamente')
        else:
            break

    user = {
        'nome':  nome,
        'email': email,
        'senha': senha,
        'id': len(DbUsuarios),
        'pontos': 0
    }
    limpa_a_tela()
    print('Usuário criado com sucesso!')
    DbUsuarios.append(user)

def cadastra_troca_de_recompensa(DbTrocasRecompenas, DbUsers, DbRecompensas, idUser, idRecompensa, quantidade, data):
    custo = DbRecompensas['custo'] * quantidade
    DbUsers[idUser]['pontos'] -= custo
    troca = {
        'idUser': idUser,
        'idRecompensa': idRecompensa,
        'quantidade': quantidade,
        'data': data
    }
    DbTrocasRecompenas.append(troca)   

def fluxo_login(DbUsuarios):
    while True:
        email = input('Insira o email: ')
        senha = input('Inisra a senha: ')

        for user in DbUsuarios:
            if(user['email'] == email):
                if(user['senha'] == senha):
                    limpa_a_tela()
                    print('Logado com Sucesso!')
                    return user
                else:
                    limpa_a_tela()
                    print('Senha incorreta! Tente Novamente!')
                    break
        limpa_a_tela()
        print('Usuário não encontrado! Tente Novamente!')
        
def fluxo_altera_senha(idUser, DbUsers):
    limpa_a_tela()
    senhaAtual = input("Informe sua senha atual: ")
    if DbUsers[idUser]['senha'] != senhaAtual:
        print('Senha incorreta!')
    else:
        novaSenha = input('Informe uma nova senha: ')
        confirmaNovaSenha = input('Confirme a nova senha: ')
        if novaSenha != confirmaNovaSenha:
            limpa_a_tela()
            print('As senhas não conferem!')
        else:
            DbUsers[idUser]['senha'] = novaSenha
            limpa_a_tela()
            print('Nova senha cadastrada!')

