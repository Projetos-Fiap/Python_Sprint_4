import os
# Defininfo função que limpa a tela do terminal
limpa_a_tela = lambda: os.system('cls')

def data_eh_menor(data1, data2):

    dataEHora1 = data1.split('-')
    horas1 = dataEHora1[0].split('h')
    hora1 = int(horas1[0])
    minuto1 = int(horas1[1])
    data1 = dataEHora1[1].split('/')
    dia1 = int(data1[0])
    mes1 = int(data1[1])
    ano1 = int(data1[2])
    
    dataEHora2 = data2.split('-')
    horas2 = dataEHora2[0].split('h')
    hora2 = int(horas2[0])
    minuto2 = int(horas2[1])
    data2 = dataEHora2[1].split('/')
    dia2 = int(data2[0])
    mes2 = int(data2[1])
    ano2 = int(data2[2])

    if ano1 > ano2:
        return False
    if ano1 < ano2:
        return True
    
    if mes1 > mes2:
        return False
    if mes1 < mes2:
        return True
    
    if dia1 > dia2:
        return False
    if dia1 < dia2:
        return True

    if hora1 > hora2:
        return False
    if hora1 < hora2:
        return True

    if minuto1 > minuto2:
        return False
    if minuto1 < minuto2:
        return True

    return True
    
def ordena_extrato(extrato):
    max = len(extrato)
    i = 0
    while i < max:
        j = 0
        while j < max-i-1:
            if not data_eh_menor(extrato[j]['data'], extrato[j+1]['data']):
                temp = extrato[j]
                extrato[j] = extrato[j+1]
                extrato[j+1] = temp
            
            j+=1
        i += 1

def mostra_extrato(DbReciclagens, DbTrocasRecompensas, idUser, DbTiposDeLixo, DbRecompensas, DbUsers):
    extratoUser = []

    for reciclagem in DbReciclagens:
        if (reciclagem['idUser'] == idUser):
            extratoUser.append(reciclagem)

    for troca in DbTrocasRecompensas:
        if(troca['idUser'] == idUser):
            extratoUser.append(troca)

    ordena_extrato(extratoUser)
    limpa_a_tela()
    print('==========================')
    print('          EXTRATO         ')
    print('==========================\n')
    for item in extratoUser:
        if 'idTipoDeLixo' in item.keys():
            print(f"Data: {item['data']} Quantidade em G: {item['quantidadeG']} Tipo de Lixo: {DbTiposDeLixo[item['idTipoDeLixo']]['nome']} \n+Pontos: {item['quantidadeG']*float(DbTiposDeLixo[item['idTipoDeLixo']]['valorKG'])/1000}\n")
        else:
            print(f"Data: {item['data']} Quantidade: {item['quantidade']} Recompensa: {DbRecompensas[item['idRecompensa']]['nome']} \n-Pontos: {item['quantidade']*float(DbRecompensas[item['idRecompensa']]['custo'])}\n")
    print('====================================\n')
    print(f"Total Pontos: {DbUsers[idUser]['pontos']}\n")


    


