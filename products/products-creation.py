def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print("Arquivo {nome} criado com sucesso")