

def abrirItem(produto):
    try:
        a = open(produto, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def criarItem(produto):
    try:
        a = open(produto + ".txt", 'a')
        a.close()
    except:
        print ('Erro')
    else:
        print ( produto + ' ' + 'Criado com sucesso')

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def lerItem(produto):
    try:
        a = open(produto + ".txt", 'rt')
    except:
        print ('Erro')
    else:
        print (a.read())

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def editarItem(produto):
    try:
        a = open(produto + ".txt", 'a')
    except:
        print ('Erro')
    else:
        descricao = input("Digite a descrição do produto")
        a.writelines(descricao)