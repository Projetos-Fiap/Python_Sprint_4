import funcoes.escritaArquivo as escritaArquivo
def cadastra_tipoDeLixo(DbTiposDeLixo):
    nome = input('Digite o nome da tipo de lixo: ')
    valorKg = input('Digite o valorKg da tipo de lixo: ')
    id = len(DbTiposDeLixo)
    tipoDeLixo = {
        'nome': nome,
        'valorKg': valorKg,
        id: id
    }
    DbTiposDeLixo.append(tipoDeLixo)
    escritaArquivo.sobrescreve_tipos_de_lixo(DbTiposDeLixo)

    print('Tipo de lixo cadastrado!')

def atualiza_tipoDeLixo(DbTiposDeLixo, tipoDeLixo):
    DbTiposDeLixo[tipoDeLixo["id"]]["nome"] = tipoDeLixo["nome"]
    DbTiposDeLixo[tipoDeLixo["id"]]["valorKg"] = tipoDeLixo["valorKg"]
    print('Seu tipo de lixo foi atualizado!')


