# pytthon-sprint02
Repo destinado à entrega de python na sprint 2

grupo 2:
Alessandra Vaiano RM551497 ,
André Lambert RM99148 ,
Bryan Willian RM551305 ,
Lucas Feijó RM99727 ,
Vitor Maia RM99658 .

Explicação do Projeto:
O nosso projeto consiste em um site que mapeia os Ecopontos e os demais pontos de reciclagem de São Paulo, e também ONGs e empresas que coletam o material a domicílio. O site traz informações sobre reciclagem, o que é aceito em cada ponto de coleta, como separar e transportar o lixo a ser reciclado, além da informação de ponto de coleta mais próximo da localização fornecida. 

O site também contém uma área de cadastro e login onde serão contabilizados créditos sociais por usuário. Esses créditos serão atribuídos pelos locais de coleta em troca de material reciclado. Incentivaremos os usuários do nosso site a reciclar por meio de uma contabilização de créditos sociais que poderão ser convertidos em benefícios A comercialização dos créditos sociais será feita através do nosso site em parceria com a empresa Gooders. Nós vendemos o crédito social de nossos usuários para a empresa Gooders, que por sua vez vendem esses créditos para seus parceiros em troca de benefícios, que então nos será disponibilizado para podermos oferecer aos nossos usuários.

Descrição do programa feito em Python:
Levando isso em conta, criamos um programa que atende os requisitos da área de cadastro para os nossos usuários.
Aqui, os créditos sociais foram utilizados como pontuação.
As funcionalidades implementadas são:
- o usuário cria o seu cadastro, caso queira o usuário poderá trocar a senha posteriormente.
- o usuário faz login na sua área de cliente. Caso não tenha cadastro, não poderá fazer login.
- dentro da área de cliente o usuário pode:
    - visualizar sua pontuação, que são os créditos sociais.
    - cadastrar o lixo que irá reciclar por tipo de material e peso. Automaticamente, poderá ver a conversaos dessa quantidade de lixo reciclado para pontos em sua área de cliente.
    - ver quais as recompensas estão disponíveis para troca. Aqui o usuário pode trocar sua pontuação por um produto disponível. Caso tente uma recompensa que precise de mais pontuação que o usuário possui, irá ser notificado que não possui pontos suficientes.
    - poderá alterar sua senha.
    - poderá fazer o logout.
