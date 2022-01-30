import os

#///////////////////////////////////////////////////////////////////////////////////////////////////////

def consultarItem(produto):
    try:
        arquivo = open(produto + ".txt", 'rt')
    except:
        print ('Erro')
    else:
        print (arquivo.read())

#///////////////////////////////////////////////////////////////////////////////////////////////////////

def editarItem(produto):
    # with is like your try .. finally block in this case
    with open(produto + ".txt", 'r') as file:
        # read a list of lines into data
        data = file.readlines()
        file.close()

    linha = int(input('Digite a linha que deseja Editar:'))
    produto_novo = input('Digite as informações que deseja sobrepor:')

    data[linha] = (produto_novo+'\n')

    # and write everything back
    with open(produto + ".txt", 'w') as file:
        file.writelines( data )
        file.close()
    

#///////////////////////////////////////////////////////////////////////////////////////////////////////

def criarProduto(produto):
    try:
        arquivo = open(produto + ".txt", 'at')
    except:
        print ('Erro')
    else:
        arquivo.writelines("\n" + input('\nCadastre um novo produto\n'))
        arquivo.close()

#///////////////////////////////////////////////////////////////////////////////////////////////////////

def deletarItem(produto):
    try:
        os.remove(produto + ".txt")
    except:
        print("Erro")

#///////////////////////////////////////////////////////////////////////////////////////////////////////