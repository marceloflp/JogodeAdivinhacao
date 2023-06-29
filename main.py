import random

#lista com palavras para gerar um valor aleatório 
palavras = ['MERCURIO', 'VENUS', 'TERRA', 'MARTE', 'JUPITER', 'SATURNO', 'NETUNO', 'URANO', 'FUTEBOL','VOLEI', 'MUAY THAI', 'NATAÇAO', 'BASQUETE', 'AUTOMOBILISMO', 'BRASIL', 'INGLATERRA', 'ESTADOS UNIDOS', 'RUSSIA', 'CHINA', 'ITALIA', 'FRANÇA', 'EGITO']

def main(palavras):
  #APRESENTAÇÃO
  print('*'*70)
  print('SEJA BEM-VINDO!')
  print('O jogo consiste em adivinhar qual palavra foi gerada aleatoriamente.')
  print('BOA SORTE!')
  print('*'*70)
  print('')

  #SORTEANDO A PALAVRA
  def palavra():
    seq = random.choice(palavras)
    return seq

  #ATRIBUINDO A FUNÇÃO A UMA VARIÁVEL
  palavra_escolhida = palavra()

  #FUNÇÃO PARA DAR DICAS AO USUÁRIO SOBRE A PALAVRA ESCOLHIDA
  def dicas(palavra_escolhida):
    dica = ''
    if palavra_escolhida == 'BRASIL':
      dicas = 'PAÍS DO FUTEBOL', 'LOCALIZADO NA AMÉRICA DO SUL', 'CULTURA RICA E DIVERSIFICADA, COM INFLUÊNCIAS INDÍGENAS, AFRICANAS E EUROPEIAS'
      dica = random.choice(dicas)
    
    if palavra_escolhida == 'INGLATERRA':
      dicas = 'REVOLUÇÃO INDUSTRIAL', 'UMA DAS NAÇÕES QUE COMPÕEM O REINO UNIDO', 'CONHECIDA POR SUA MONARQUIA'
      dica = random.choice(dicas)

    if palavra_escolhida == 'ESTADOS UNIDOS':
      dicas = 'ESPORTE POPULAR: BASEBALL', 'LOCALIZADA NA AMÉRICA DO NORTE', 'TERCEIRO MAIOR PAÍS DO MUNDO EM ÁREA E POPULAÇÃO'
      dica = random.choice(dicas)

    if palavra_escolhida == 'RUSSIA':
      dicas = 'ANTIGA UNIÃO SOVIÉTICA', 'MAIOR PAÍS DO MUNDO EM ÁREA', 'INFLUÊNCIA SIGNIFICATIVA NA POLÍTICA GLOBAL E NAS ARTES'
      dica = random.choice(dicas)

    if palavra_escolhida == 'CHINA':
      dicas = 'KUNG FU', ' CONHECIDA POR SUAS INVENÇÕES HISTÓRICAS COMO A PÓLVORA, A BÚSSOLA E O PAPEL', 'ECONOMIA EM CRESCIMENTO RÁPIDO E É UMA DAS MAIORES POTÊNCIAS ECONÔMICAS'
      dica = random.choice(dicas)

    if palavra_escolhida == 'ITALIA':
      dicas = 'TORRE DE PISA', 'BERÇO DO IMPÉRIO ROMANO E DO RENASCIMENTO', 'LOCALIZADO NO SUL DA EUROPA'
      dica = random.choice(dicas)

    if palavra_escolhida == 'FRANÇA':
      dicas = 'TORRE EIFFEL', 'BERÇO DA GASTRONOMIA', 'LOCALIZADO NA EUROPA OCIDENTAL'
      dica = random.choice(dicas)

    if palavra_escolhida == 'EGITO':
      dicas = 'FARAÓS', 'CONHECIDO POR SUAS PIRÂMIDES, ESFINGE E O RIO NILO', 'LOCALIZADO NO NORDESTE DA ÁFRICA E TAMBÉM POSSUI UM TERRITÓRIO NO ORIENTE MÉDIO'
      dica = random.choice(dicas)

    if palavra_escolhida == 'VENUS':
      dicas = 'PLANETA MAIS QUENTE DO SISTEMA SOLAR', 'SEGUNDO PLANETA MAIS PRÓXIMO DO SOL', 'NÃO POSSUI LUAS'
      dica = random.choice(dicas)
    
    if palavra_escolhida == 'MERCURIO':
      dicas = 'PLANETA MAIS PRÓXIMO DO SOL', 'TEM UMA ÓRBITA ELÍPTICA E UM PERÍODO ORBITAL DE APROXIMADAMENTE 88 DIAS', 'EXTREMAMENTE QUENTE DURANTE O DIA E FRIO DURANTE A NOITE'
      dica = random.choice(dicas)

    if palavra_escolhida == 'TERRA':
      dicas = 'NOSSO LAR', 'TERCEIRO PLANETA DO NOSSO SISTEMA SOLAR', 'ATMOSFERA COMPOSTA PRINCIPALMENTE DE NITROGÊNIO E OXIGÊNIO'
      dica = random.choice(dicas)
      
    if palavra_escolhida == 'MARTE':
      dicas = 'PLANETA VERMELHO', 'ONDE ESTÁ A MAIOR MONTANHA CONHECIDA NO SISTEMA SOLAR', 'QUARTO PLANETA DO NOSSO SISTEMA SOLAR'
      dica = random.choice(dicas)

    if palavra_escolhida == 'JUPITER':
      dicas = 'MAIOR PLANETA DO SISTEMA SOLAR', 'GIGANTE GASOSO', 'EXERCE UMA FORTE INFLUÊNCIA GRAVITACIONAL NO SISTEMA SOLAR'
      dica = random.choice(dicas)

    if palavra_escolhida == 'SATURNO':
      dicas = 'PLANETA ANELADO', 'SEXTO PLANETA DO NOSSO SISTEMA SOLAR', 'POSSUI DEZENAS DE LUAS'
      dica = random.choice(dicas)

    if palavra_escolhida == 'NETUNO':
      dicas = 'PLANETA MAIS FRIO DO SISTEMA SOLAR', 'TEM LUAS, SENDO A MAIOR DELAS TRITÃO', 'PLANETA MAIS DISTANTE DO SOL'
      dica = random.choice(dicas)

    if palavra_escolhida == 'URANO':
      dicas = ' POSSUI 27 LUAS CONHECIDAS', 'PLANETA DESCOBERTO EM 1781 ', 'SÉTIMO PLANETA DO NOSSO SISTEMA SOLAR'
      dica = random.choice(dicas)
    
    if palavra_escolhida == 'FUTEBOL':
      dicas = 'BOLA NO CHÃO', 'ESPORTE QUE ENVOLVE DUAS EQUIPES', 'ESPORTE POPULAR'
      dica = random.choice(dicas)
    
    if palavra_escolhida == 'VOLEI':
      dicas = 'REDE NA QUADRA', 'ESPORTE OLÍMPICO POPULAR', 'JOGADO ENTRE DUAS EQUIPES DE SEIS JOGADORES CADA'
      dica = random.choice(dicas)

    if palavra_escolhida == 'MUAY THAI':
      dicas = 'ARTE MARCIAL TAILANDESA', 'ESPORTE DE COMBATE POPULAR', 'PRATICADO EM RINGUES'
      dica = random.choice(dicas)
      
    if palavra_escolhida == 'NATAÇAO':
      dicas = 'COMPETIÇÃO AQUÁTICA', 'POPULAR EM PISCINAS', 'ENVOLVE MOVIMENTAR-SE NA ÁGUA USANDO OS BRAÇOS, PERNAS OU AMBOS'
      dica = random.choice(dicas)

    if palavra_escolhida == 'BASQUETE':
      dicas = 'JOGADO EM UMA QUADRA COM UMA CESTA EM CADA EXTREMIDADE', 'ESPORTE JOGADO ENTRE DUAS EQUIPES DE CINCO JOGADORES CADA', 'ENVOLVE MARCAR PONTOS'
      dica = random.choice(dicas)

    if palavra_escolhida == 'AUTOMOBILISMO':
      dicas = 'F1 & F. INDY', 'REQUER HABILIDADES DE PILOTAGEM', 'ENVOLVE VEÍCULOS MOTORIZADOS'
      dica = random.choice(dicas)

    return dica

  
  dica = dicas(palavra_escolhida)

  #EXECUÇÃO DO JOGO
  def execucao(dica,sequencia):
    tentativas = 8
    defina = ''
    plv = []
    while True:
      acertos = 0
      print(f'Tentativas: {tentativas}')
      print(f'DICA - {dica}')
      for letra in palavra_escolhida: #FAZENDO UMA VARREDURA NA PALAVRA SORTEADA
        if letra in plv: #EXIBINDO LETRAS DA PALAVRA SORTEADA
          print(letra)        
        else: #ESPAÇO EM VAZIO SE A LETRA NÃO FOR CORRETA
          print('_')
          acertos +=1

      #MENSAGEM DE PARABENIZAÇÃO CASO A PALAVRA FOR ENCONTRADA E ENCERRAMENTO
      if (defina == palavra_escolhida) or (acertos == 0):
        print()
        print(f'PARABÉNS, VOCÊ ACERTOU!!! A PALAVRA CORRETA É {palavra_escolhida}.\n')
        print()
        break
        
      #INSERINDO LETRA OU PALAVRA
      defina = input('Digite uma letra ou nome correto: ').upper()
      print()
      if defina in palavra_escolhida:
        plv.append(defina)

      #MENSAGEM DE ERRO
      if len(defina) > 1 and len(defina) < len(palavra_escolhida):
        tentativas -= 1
        if tentativas == 0:
          print('LIMITE DE TENTATIVAS EXCEDIDO, VOCÊ PERDEU!')
          print()
          break
        print('Opção inválida, digite apenas uma letra ou a palavra completa!')
        print()
        continue

      #SUBTRAINDO NÚMERO DE TENTATIVAS CASO ESCOLHA SEJA INVÁLIDA
      if defina not in palavra_escolhida:
        tentativas -= 1
        if tentativas == 0:
          print('LIMITE DE TENTATIVAS EXCEDIDO, VOCÊ PERDEU!')
          print()
          break

  
  execucao(dica, palavras)

  #MENU DE OPÇÕES
  print('DESEJA CONTINUAR? \n1- SIM \n2- NÃO')      
  opcao = int(input('OPÇÃO: '))
  if opcao == 1:
    print()
    main(palavras)
  if opcao == 2:
    pass
  
main(palavras)