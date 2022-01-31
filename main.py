import cadastro.cadastroProdutos as cadastro

print("--------Menu temporário--------")
print("1. Criar um produto")
print("2. Editar um produto")
print("3. Consultar um produto")
print("4. Excluir um produto")
print("5. Sair do programa")
print("------------------------")

menu = int(input("\nDigite a opção: "))
if menu == 1:
    print("")
    cadastro.criarProduto()
    print("Produto criado com sucesso:")
    cadastro.consultarItem()
elif menu == 2:
    print("Produtos:")
    cadastro.consultarItem()
    cadastro.editarItem()
    print("Produtos atualizados:")
    cadastro.consultarItem()
elif menu == 3:
    print("Produtos:")
    cadastro.consultarItem()
elif menu == 4:
    print("Produtos:")
    cadastro.consultarItem()
    print("")
    cadastro.deletarItem()
    print("Produtos atualizados:")
    cadastro.consultarItem()

elif menu == 5:
    exit()