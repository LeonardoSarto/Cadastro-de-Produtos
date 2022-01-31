#///////////////////////////////////////////////////////////////////////////////////////////////////////

def consultarItem():
    try:
        arquivo = open("Cadastro_de_Produtos.txt", 'rt')
    except:
        print ('Erro')
    else:
        print (arquivo.read())

#///////////////////////////////////////////////////////////////////////////////////////////////////////

def editarItem():
    # with is like your try .. finally block in this case
    with open("Cadastro_de_Produtos.txt", 'r') as file:
        # read a list of lines into data
        data = file.readlines()
        file.close()

    linha = int(input('Digite a linha que deseja editar: '))
    produto_novo = input('Digite as informações que deseja sobrepor: ')

    data[linha] = (produto_novo+'\n')

    # and write everything back
    with open("Cadastro_de_Produtos.txt", 'w') as file:
        file.writelines( data )
        file.close()
    

#///////////////////////////////////////////////////////////////////////////////////////////////////////

def criarProduto():
    try:
        arquivo = open("Cadastro_de_Produtos.txt", 'at')
    except:
        print ('Erro')
    else:
        arquivo.writelines('\n' + input('Cadastre um novo produto: '))
        arquivo.close()

#///////////////////////////////////////////////////////////////////////////////////////////////////////

def deletarItem():
    try:
        with open("Cadastro_de_Produtos.txt", 'r') as file:
        # read a list of lines into data
            data = file.readlines()
            file.close()

        linha = int(input('Digite a linha que deseja excluir: '))

        data[linha] = " "

        # and write everything back
        with open("Cadastro_de_Produtos.txt", 'w') as file:
            file.writelines(data)
            file.close()
    except:
        print("Erro")

#///////////////////////////////////////////////////////////////////////////////////////////////////////