import json

# usuarios
# recompensas
# tiposDeLixo
# reciclagens
# trocasRecompensas

def sobrescreve_usuarios(usuarios):

    with open('./bases/usuarios.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(usuarios, arquivo)

def sobrescreve_recompensas(recompensas):

    with open('./bases/recompensas.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(recompensas, arquivo)

def sobrescreve_tipos_de_lixo(tiposDeLixo):

    with open('./bases/tiposDeLixo.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(tiposDeLixo, arquivo)

def sobrescreve_reciclagens(reciclagens):

    with open('./bases/reciclagens.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(reciclagens, arquivo)

def sobrescreve_trocas_recompensas(trocasRecompensas):

    with open('./bases/trocasRecompensas.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(trocasRecompensas, arquivo)

def carrega_usuarios():
    try:
        with open('./bases/usuarios.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            usuarios = json.load(arquivo)
            return usuarios
    except FileNotFoundError:
        return ['arquivo n encontrado'] 

def carrega_recompensas():
    try:
        with open('./bases/recompensas.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            recompensas = json.load(arquivo)
            return recompensas
    except FileNotFoundError:
        return ['arquivo n encontrado']
    
def carrega_tipos_de_lixo():    
    try:
        with open('./bases/tiposDeLixo.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            tiposDeLixo = json.load(arquivo)
            return tiposDeLixo
    except FileNotFoundError:
        return ['arquivo n encontrado']
    
def carrega_reciclagens():    
    try:
        with open('./bases/reciclagens.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            reciclagens = json.load(arquivo)
            return reciclagens
    except FileNotFoundError:
        return ['arquivo n encontrado']
    
def carrega_trocas_recompensas():    
    try:
        with open('./bases/trocasRecompensas.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            trocasRecompensas = json.load(arquivo)
            return trocasRecompensas
    except FileNotFoundError:
        return ['arquivo n encontrado']
